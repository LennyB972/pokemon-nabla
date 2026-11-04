#!/usr/bin/env python3
"""Wires a mirage of the Eon Flute whose layout is drawn (data/layouts/<Map>/map.bin, in layouts.json): its map, its
region map section, its legendary Pokémon (one object, one script and one flag each, data/scripts/nabla/mirages.inc),
its items on the ground, and its entry in the list of the Eon Flute (docs/nabla/postgame.md).

Used from a short script, once per mirage:
    import add_mirage
    add_mirage.add(map_name="NablaFlowerParadise", place="FLOWER PARADISE", arrival=(17, 16), music="MUS_VERDANTURF",
                   legendaries=[("SHAYMIN", 14, 8, 0x35), ...], items=[("ITEM_X", x, y, flag), ...],
                   unlocked_by=["SPECIES_UXIE", ...], comment="Flower Paradise: Shaymin in the flowers...")
A mirage with hidden Pokémon also gets an altar: altar=(x, y), hidden=[("KELDEO", x, y, flag, ["COBALION", ...])]
(the Pokémon asked for in the party, checked in turn at the altar) and altar_waits, the text of the altar while it
waits for them (data/text/nabla/mirages.inc).
Flags are given as numbers of FLAG_UNUSED_* flags, which get their Nabla names.
"""
import json
import os
import re


def rep(path, old, new):
    s = open(path, encoding="utf-8").read()
    assert s.count(old) == 1, (path, old[:70])
    open(path, "w", encoding="utf-8").write(s.replace(old, new))


def append(path, text):
    s = open(path, encoding="utf-8").read()
    open(path, "w", encoding="utf-8").write(s.rstrip("\n") + "\n" + text + "\n")


def camel(name):
    return "".join(w.capitalize() for w in name.split("_"))


def name_flag(number, name):
    path = "include/constants/flags.h"
    s = open(path, encoding="utf-8").read()
    m = re.search(r"^#define FLAG_UNUSED_0x0*%X +0x%X +// Unused Flag$" % (number, number), s, re.M)
    assert m, "flag 0x%X is not free" % number
    open(path, "w", encoding="utf-8").write(s[:m.start()] + "#define %s 0x%X" % (name, number) + s[m.end():])


def altar_script(short, upper, first, hidden):
    """The script of the altar: the first hidden Pokémon not caught nor there whose Pokémon are all in the party appears
    behind it (cry, white flash); otherwise the altar waits, or is quiet once they are all caught or there."""
    lines = ["", "Nabla_%s_EventScript_Altar::" % short, "\tlock"]
    for k, (species, x, y, flag, required) in enumerate(hidden):
        skip = "Nabla_%s_EventScript_AltarNot%s" % (short, camel(species))
        temp = "FLAG_TEMP_%d" % (11 + first + k)
        lines += ["\tgoto_if_set FLAG_NABLA_%s_CAUGHT, %s" % (species, skip), "\tgoto_if_unset %s, %s" % (temp, skip)]
        for r in required:
            lines += ["\tsetvar VAR_0x8004, SPECIES_%s" % r, "\tspecialvar VAR_RESULT, NablaMirage_PartyHasSpecies",
                      "\tgoto_if_eq VAR_RESULT, FALSE, %s" % skip]
        lines += ["\tmsgbox Nabla_Text_%sAltarAwakens%s, MSGBOX_DEFAULT" % (short, camel(species)), "\tclosemessage",
                  "\tplaymoncry SPECIES_%s, CRY_MODE_ENCOUNTER" % species, "\tfadescreenswapbuffers FADE_TO_WHITE",
                  "\tclearflag " + temp, "\taddobject LOCALID_%s_%s" % (upper, species),
                  "\tfadescreenswapbuffers FADE_FROM_WHITE", "\twaitmoncry", "\trelease", "\tend", skip + ":"]
    for k, (species, *_) in enumerate(hidden):
        lines.append("\tgoto_if_unset FLAG_TEMP_%d, Nabla_%s_EventScript_AltarQuiet" % (11 + first + k, short))
    for species, *_ in hidden:
        lines.append("\tgoto_if_unset FLAG_NABLA_%s_CAUGHT, Nabla_%s_EventScript_AltarWaits" % (species, short))
    lines += ["Nabla_%s_EventScript_AltarQuiet:" % short, "\tmsgbox Nabla_Text_AncientAltar, MSGBOX_DEFAULT", "\trelease",
              "\tend", "", "Nabla_%s_EventScript_AltarWaits:" % short,
              "\tmsgbox Nabla_Text_%sAltarWaits, MSGBOX_DEFAULT" % short, "\trelease", "\tend"]
    return lines


def add(map_name, place, arrival, legendaries, music, comment, items=(), unlocked_by=(), weather="WEATHER_NONE",
        map_type="MAP_TYPE_ROUTE", allow_cycling=True, altar=None, hidden=(), altar_waits=""):
    short = map_name[len("Nabla"):]                                   # FlowerParadise
    upper = re.sub(r"(?<!^)(?=[A-Z])", "_", short).upper()            # FLOWER_PARADISE
    mapsec = "MAPSEC_NABLA_" + upper

    # The place: a destination of the Eon Flute, its region map section, its map in the group of Nabla
    rep("src/nabla_eon_flute.c", "\n};\n\nbool8 NablaEonFlute_IsAtDestination", "\n    %s,\n};\n\nbool8 NablaEonFlute_IsAtDestination" % mapsec)
    rep("src/data/region_map/region_map_sections.json", "    }\n  ]\n}",
        '    },\n    {\n      "id": "%s",\n      "name": "%s"\n    }\n  ]\n}' % (mapsec, place))
    s = open("data/maps/map_groups.json", encoding="utf-8").read()
    i = s.index('"gMapGroup_Nabla": [')
    j = s.index("\n  ]", i)
    open("data/maps/map_groups.json", "w", encoding="utf-8").write(s[:j] + ',\n    "%s"' % map_name + s[j:])
    s = open("data/event_scripts.s", encoding="utf-8").read()
    last = list(re.finditer(r'^\t\.include "data/maps/Nabla\w+/scripts\.inc"\n', s, re.M))[-1]
    s = s[:last.end()] + '\t.include "data/maps/%s/scripts.inc"\n' % map_name + s[last.end():]
    open("data/event_scripts.s", "w", encoding="utf-8").write(s)
    for path in ("src/data/region_map/region_map_sections.json", "data/maps/map_groups.json"):
        json.load(open(path))

    # The map: one object per legendary, hidden by a temporary flag until set up (the hidden ones until the altar calls
    # them), the altar and the items
    objects = []
    for i, (species, x, y, flag) in enumerate([*legendaries, *(h[:4] for h in hidden)]):
        name_flag(flag, "FLAG_NABLA_%s_CAUGHT" % species)
        objects.append({"local_id": "LOCALID_%s_%s" % (upper, species), "graphics_id": "OBJ_EVENT_GFX_SPECIES(%s)" % species,
                        "x": x, "y": y, "elevation": 3, "movement_type": "MOVEMENT_TYPE_WALK_SLOWLY_IN_PLACE_DOWN",
                        "movement_range_x": 0, "movement_range_y": 0, "trainer_type": "TRAINER_TYPE_NONE",
                        "trainer_sight_or_berry_tree_id": "0", "script": "Nabla_%s_EventScript_%s" % (short, camel(species)),
                        "flag": "FLAG_TEMP_%d" % (11 + i)})
    if altar:
        objects.append({"local_id": "LOCALID_%s_ALTAR" % upper, "graphics_id": "OBJ_EVENT_GFX_TRICK_HOUSE_STATUE",
                        "x": altar[0], "y": altar[1], "elevation": 3, "movement_type": "MOVEMENT_TYPE_FACE_DOWN",
                        "movement_range_x": 0, "movement_range_y": 0, "trainer_type": "TRAINER_TYPE_NONE",
                        "trainer_sight_or_berry_tree_id": "0", "script": "Nabla_%s_EventScript_Altar" % short, "flag": "0"})
    for item, x, y, flag in items:
        flag_name = "FLAG_NABLA_ITEM_%s_%s" % (upper, item[len("ITEM_"):])
        name_flag(flag, flag_name)
        objects.append({"graphics_id": "OBJ_EVENT_GFX_ITEM_BALL", "x": x, "y": y, "elevation": 3,
                        "movement_type": "MOVEMENT_TYPE_LOOK_AROUND", "movement_range_x": 0, "movement_range_y": 0,
                        "trainer_type": "TRAINER_TYPE_NONE", "trainer_sight_or_berry_tree_id": item,
                        "script": "Common_EventScript_FindItem", "flag": flag_name})
    m = {"id": "MAP_NABLA_" + upper, "name": map_name, "layout": "LAYOUT_NABLA_" + upper, "music": music,
         "region": "REGION_HOENN", "region_map_section": mapsec, "requires_flash": False, "weather": weather,
         "map_type": map_type, "allow_cycling": allow_cycling, "allow_escaping": False, "allow_running": True,
         "show_map_name": True, "battle_scene": "MAP_BATTLE_SCENE_NORMAL", "connections": None, "object_events": objects,
         "warp_events": [], "coord_events": [], "bg_events": []}
    os.makedirs("data/maps/" + map_name, exist_ok=True)
    open("data/maps/%s/map.json" % map_name, "w", encoding="utf-8").write(json.dumps(m, indent=2, ensure_ascii=False) + "\n")
    open("data/maps/%s/scripts.inc" % map_name, "w", encoding="utf-8").write(
        "%s_MapScripts::\n\tmap_script MAP_SCRIPT_ON_TRANSITION, %s_OnTransition\n\t.byte 0\n\n"
        "%s_OnTransition:\n\tcall Nabla_%s_EventScript_SetUp\n\tend\n" % (map_name, map_name, map_name, short))

    # The scripts of the legendaries
    every = [*legendaries, *(h[:4] for h in hidden)]
    lines = ["", "@ " + comment, "Nabla_%s_EventScript_SetUp::" % short, "\tsetflag FLAG_TEMP_HIDE_FOLLOWER"]
    lines += ["\tsetflag FLAG_TEMP_%d  @ %s" % (11 + i, camel(s)) for i, (s, *_) in enumerate(every)]
    lines += ["\tcall_if_unset FLAG_NABLA_%s_CAUGHT, Nabla_%s_EventScript_Show%s" % (s, short, camel(s)) for s, *_ in legendaries]
    lines.append("\treturn")
    for i, (species, *_) in enumerate(legendaries):
        lines += ["", "Nabla_%s_EventScript_Show%s:" % (short, camel(species)), "\tclearflag FLAG_TEMP_%d" % (11 + i), "\treturn"]
    for species, *_ in every:
        lines += ["", "Nabla_%s_EventScript_%s::" % (short, camel(species)), "\tsetvar VAR_0x8004, SPECIES_%s" % species,
                  "\tcall Nabla_EventScript_MirageLegendary", "\tsetflag FLAG_NABLA_%s_CAUGHT" % species, "\trelease", "\tend"]
    if altar:
        lines += altar_script(short, upper, len(legendaries), hidden)
        lines_of_text = altar_waits.split("\n")
        texts = ["", "Nabla_Text_%sAltarWaits:" % short, '\t.string "An ancient altar.\\p"']
        texts += ['\t.string "%s\\n"' % line for line in lines_of_text[:-1]] + ['\t.string "%s$"' % lines_of_text[-1]]
        for species, *_, required in hidden:
            names = [r.replace("_", " ") for r in required]
            who = names[0] if len(names) == 1 else "%s and %s" % (", ".join(names[:-1]), names[-1])
            texts += ["", "Nabla_Text_%sAltarAwakens%s:" % (short, camel(species)), '\t.string "%s\\n"' % who,
                      '\t.string "%s to the altar!$"' % ("reacts" if len(names) == 1 else "react")]
        append("data/text/nabla/mirages.inc", "\n".join(texts))
    append("data/scripts/nabla/mirages.inc", "\n".join(lines))

    # The list of the Eon Flute: the next number, under conditions if the mirage is unlocked by caught Pokémon
    path = "data/scripts/nabla/eon_flute.inc"
    s = open(path, encoding="utf-8").read()
    number = max(int(n) for n in re.findall(r"^\tcase (\d+), Nabla_EventScript_EonFluteTo", s, re.M)) + 1
    text = "Nabla_Text_" + short
    push = ("\tcall Nabla_EventScript_EonFluteList%s\n" % short) if unlocked_by else "\tdynmultipush %s, %d\n" % (text, number)
    s = s.replace("\tdynmultistack 0, 0, FALSE", push + "\tdynmultistack 0, 0, FALSE", 1)
    last_case = list(re.finditer(r"^\tcase \d+, Nabla_EventScript_EonFluteTo\w+\n", s, re.M))[-1]
    s = s[:last_case.end()] + "\tcase %d, Nabla_EventScript_EonFluteTo%s\n" % (number, short) + s[last_case.end():]
    scripts = ""
    if unlocked_by:
        scripts += "Nabla_EventScript_EonFluteList%s:\n" % short
        for species in unlocked_by:
            scripts += "\tgetcaughtmon %s\n\tgoto_if_eq VAR_RESULT, FALSE, Nabla_EventScript_EonFluteListNothing\n" % species
        scripts += "\tdynmultipush %s, %d\n\treturn\n\n" % (text, number)
    scripts += ("Nabla_EventScript_EonFluteTo%s:\n\tspecial NablaEonFlute_SaveReturnPoint\n\twarp MAP_NABLA_%s, %d, %d\n"
                "\twaitstate\n\treleaseall\n\tend\n\n" % (short, upper, arrival[0], arrival[1]))
    s = s.replace("Nabla_EventScript_EonFluteGoBack:", scripts + "Nabla_EventScript_EonFluteGoBack:", 1)
    open(path, "w", encoding="utf-8").write(s)
    append("data/text/nabla/eon_flute.inc", '\n%s:\n\t.string "%s$"' % (text, place))
    return number
