#!/usr/bin/env python3
"""Raises the levels of the ordinary trainers, wild Pokémon and static Pokémon of Hoenn (step 4.3).

Each part of the adventure (between two badges) gets a factor: the new level cap divided by the level
of the strongest Pokémon of the original Gym Leader. A level is multiplied by the factor of the part of
the adventure where it is met: that of its map (MAP_PARTS), or, for a trainer, that of its original
level if it is later (trainers reached with Surf, rematches). Wild Pokémon met with Surf, Rock Smash or
a rod also start at the part where these are obtained.

Trainers' Pokémon evolve when the new level reaches their evolution level (level 40 for the evolutions
that need more than a level: trade, item, friendship...). Wild Pokémon evolve in the game itself
(GetNablaWildEvolution in src/wild_encounter.c).

The script always starts from the original levels (trainers of pokeemerald-expansion, wild tables
before step 4.3), so it can be run again after changing a factor. It rewrites the trainers it handles:
a manual change to one of them is lost (the trainers of step 4.2 are left out, see EXCLUDED).

Usage (from the repo root): python3 dev_scripts/nabla/scale_levels.py (also rewrites docs/nabla/levels.md)
"""
import glob
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import coverage as cv
import safari_tables as st

TRAINERS_REV = "87cc74b5ec"  # pokeemerald-expansion before Pokémon Nabla
WILD_REV = "476e2584ec"      # wild tables of step 4.1, before step 4.3
DOC = "docs/nabla/levels.md"

# Parts of the adventure: (name, original Gym Leader, new level cap); the factor is new / original.
PARTS = [
    ("Avant le 1er badge", 15, 16),
    ("1er → 2e badge", 19, 20),
    ("2e → 3e badge", 24, 27),
    ("3e → 4e badge", 29, 34),
    ("4e → 5e badge", 31, 35),
    ("5e → 6e badge", 33, 41),
    ("6e → 7e badge", 42, 51),
    ("7e → 8e badge", 46, 59),
    ("Route Victoire", 50, 70),  # factor 1.4, set on the Elite Four (Sidney 46 -> 66)
]
VICTORY_ROAD = len(PARTS) - 1

# Part of the adventure of each map (prefixes of the folders of data/maps), when its trainers and wild
# Pokémon are meant to be met. None: left as it is (after the League, Safari Zone, Nabla zones).
MAP_PARTS = [
    (0, "LittlerootTown OldaleTown Route101 Route102 Route103 Route104 PetalburgWoods PetalburgCity "
        "RustboroCity Route116"),
    (1, "RusturfTunnel DewfordTown GraniteCave Route106"),
    (2, "Route109 SlateportCity Route110 MauvilleCity Route117 Route111"),
    (3, "Route112 Route113 Route114 Route115 FallarborTown MeteorFalls_1F_1R MtChimney JaggedPass "
        "LavaridgeTown FieryPath NewMauville"),
    (4, "PetalburgCity_Gym MirageTower"),
    (5, "Route105 Route107 Route108 AbandonedShip Route118 Route119 Route120 ScorchedSlab FortreeCity"),
    (6, "Route121 Route122 MtPyre Route123 LilycoveCity MagmaHideout AquaHideout Route124 Route125 "
        "MossdeepCity Route126 Route127 Route128 ShoalCave"),
    (7, "MossdeepCity_SpaceCenter SeafloorCavern Route129 Route130 Route131 Route132 Route133 Route134 "
        "PacifidlogTown SootopolisCity CaveOfOrigin SkyPillar Underwater"),
    (8, "VictoryRoad EverGrandeCity MeteorFalls_1F_2R MeteorFalls_B1F"),
    (None, "SSTidal MeteorFalls_StevensCave BattleFrontier TrainerHill ArtisanCave DesertUnderpass TerraCave "
           "MarineCave AlteringCave SafariZone NavelRock BirthIsland FarawayIsland SouthernIsland Nabla"),
]
# Wild Pokémon met with Surf (5th badge), Rock Smash (3rd badge) and the rods (Old Rod in Dewford,
# Good Rod on Route 118, Super Rod in Mossdeep)
AREA_PARTS = {"water_mons": 5, "rock_smash_mons": 3}
ROD_PARTS = {"old_rod": 1, "good_rod": 5, "super_rod": 6}
# Non-legendary static Pokémon of the story: (script, species)
STATIC_POKEMON = [
    ("data/maps/NewMauville_Inside/scripts.inc", "VOLTORB"),
    ("data/maps/AquaHideout_B1F/scripts.inc", "ELECTRODE"),
    ("data/maps/Route120/scripts.inc", "KECLEON"),
    ("data/scripts/kecleon.inc", "KECLEON"),
]
STATIC_PARTS = {"NewMauville_Inside": 3, "AquaHideout_B1F": 6, "Route120": 5, "kecleon.inc": 5}
# Tables added by Pokémon Nabla to original maps: the table whose original levels they take
LEVELS_FROM = {"gScorchedSlab": "gRoute120"}
# Trainers of step 4.2 (and the Gym Leaders' rematches, after the League)
EXCLUDED = re.compile(r"TRAINER_((ROXANNE|BRAWLY|WATTSON|FLANNERY|NORMAN|WINONA|TATE_AND_LIZA|JUAN)_\d"
                      r"|SIDNEY|PHOEBE|GLACIA|DRAKE|WALLACE|STEVEN|(MAY|BRENDAN|WALLY)_\w+"
                      r"|ARCHIE|MATT|MAXIE_\w+|SHELLY_\w+|TABITHA_\w+|NABLA_\w+)$")

OTHER_EVOLUTIONS_LEVEL = 40  # NABLA_OTHER_EVOLUTIONS_LEVEL
# Conditions that choose between evolutions; the others are requirements, met from level 40
BRANCH_CONDITIONS = {"IF_GENDER", "IF_TIME", "IF_NOT_TIME", "IF_ATK_GT_DEF", "IF_ATK_EQ_DEF", "IF_ATK_LT_DEF",
                     "IF_PID_UPPER_MODULO_10_GT", "IF_PID_UPPER_MODULO_10_EQ", "IF_PID_UPPER_MODULO_10_LT",
                     "IF_NATURE", "IF_AMPED_NATURE", "IF_LOW_KEY_NATURE", "IF_PID_MODULO_100_GT",
                     "IF_PID_MODULO_100_EQ", "IF_PID_MODULO_100_LT", "IF_REGION", "IF_NOT_REGION"}


def factor(part):
    return PARTS[part][2] / PARTS[part][1]


def scale(level, part):
    return min(100, max(level, int(level * factor(part) + 0.5)))


def level_part(level):
    # Part of the adventure of an original level (that of the next Gym Leader)
    for i, (_, leader, _) in enumerate(PARTS[:VICTORY_ROAD]):
        if level <= leader:
            return i
    return VICTORY_ROAD


def map_part(folder):
    best, part = "", None
    for p, prefixes in MAP_PARTS:
        for prefix in prefixes.split():
            if folder.startswith(prefix) and len(prefix) > len(best):
                best, part = prefix, p
    if not best:
        raise SystemExit("scale_levels.py: map %s is missing from MAP_PARTS" % folder)
    return part


def git_show(rev, path):
    return subprocess.run(["git", "show", "%s:%s" % (rev, path)], capture_output=True, text=True, check=True).stdout


# --- Evolutions (same rule as GetNablaWildEvolution)

def region_ok(conditions, regions):
    for c in conditions:
        if c[0] == "IF_REGION" and c[1] not in regions:
            return False
        if c[0] == "IF_NOT_REGION" and c[1] in regions:
            return False
    return True


def is_level_evolution(method, param, conditions):
    return method == "EVO_LEVEL" and param.isdigit() and int(param) > 0 \
        and all(c[0] in BRANCH_CONDITIONS for c in conditions)


def other_evolutions(evos, name, level, regions):
    # Evolutions that need more than a level, available from level 40
    if level < OTHER_EVOLUTIONS_LEVEL:
        return []
    return [(target, conditions) for method, param, target, conditions in evos.get(name, [])
            if method not in ("EVO_NONE", "EVO_SPLIT_FROM_EVO") and region_ok(conditions, regions)
            and not (method in ("EVO_LEVEL", "EVO_LEVEL_BATTLE_ONLY") and param.isdigit() and int(param) > level)]


def wild_forms(evos, name, level, regions=("REGION_HOENN",)):
    # Species a wild Pokémon of this level can be met as (several when the evolution depends on its gender,
    # nature, time... or is picked at random)
    forms, always = set(), False
    for method, param, target, conditions in evos.get(name, []):
        if is_level_evolution(method, param, conditions) and int(param) <= level and region_ok(conditions, regions):
            forms |= wild_forms(evos, target, level, regions)
            if not any(c[0] in BRANCH_CONDITIONS - {"IF_REGION", "IF_NOT_REGION"} for c in conditions):
                always = True
                break
    if not always:
        for target, conditions in other_evolutions(evos, name, level, regions):
            forms |= wild_forms(evos, target, level, regions)
            always = always or not any(c[0] in BRANCH_CONDITIONS - {"IF_REGION", "IF_NOT_REGION"} for c in conditions)
    return forms if always else forms | {name}


def trainer_evolution(evos, name, old_level, level):
    # A trainer's Pokémon evolves when the raise of its level makes it reach its evolution level (an
    # original Pokémon that could already evolve stays as it is); the first evolution of the list when
    # there are several
    for method, param, target, conditions in evos.get(name, []):
        if is_level_evolution(method, param, conditions) and region_ok(conditions, ("REGION_HOENN",)):
            if int(param) <= old_level:
                return None
            if int(param) <= level:
                return target
    if old_level < OTHER_EVOLUTIONS_LEVEL:
        others = other_evolutions(evos, name, level, ("REGION_HOENN",))
        if others:
            return others[0][0]
    return None


# --- Trainers

ALIASES = dict(re.findall(r"^\s*SPECIES_(\w+) = SPECIES_(\w+),", open("include/constants/species.h").read(), re.M))


def species_constant(name):
    name = name.replace("♂", "_M").replace("♀", "_F").replace("é", "e").replace("'", "").replace("’", "")
    return re.sub(r"[^A-Z0-9]+", "_", name.upper()).strip("_")


def parse_party(text):
    # {label: [(header, [mon blocks])]} (a label has one entry per difficulty)
    trainers = {}
    for block in re.split(r"\n(?==== )", text):
        m = re.match(r"=== (TRAINER_\w+) ===\n", block)
        if not m:
            continue
        parts = block.rstrip("\n").split("\n\n")
        trainers.setdefault(m.group(1), []).append((parts[0], [p for p in parts[1:] if p.strip()]))
    return trainers


MON_FIRST_LINE = re.compile(r"^(?:(?P<nick>.+?) \((?P<sp1>[^()]+)\)|(?P<sp2>[^@()]+?))(?P<rest>(?: \([MF]\))?(?: @ .+)?)$")


def mon_species(mon):
    m = MON_FIRST_LINE.match(mon.split("\n")[0].strip())
    return (m.group("sp1") or m.group("sp2")).strip()


def trainer_maps():
    # Maps where each trainer is fought: battle scripts, and the rematch table
    maps = {}
    for f in glob.glob("data/maps/*/scripts.inc"):
        folder = f.split("/")[2]
        if folder.endswith("_Frlg"):
            continue
        for t in re.findall(r"\bTRAINER_\w+", open(f).read()):
            maps.setdefault(t, set()).add(folder)
    folders = {json.load(open(f))["id"]: f.split("/")[2] for f in glob.glob("data/maps/*/map.json")}
    for m in re.finditer(r"REMATCH\(([^)]*)\)", open("src/battle_setup.c").read()):
        args = [a.strip() for a in m.group(1).split(",")]
        if args[-1] not in folders:
            continue  # the macro itself
        for t in args[:-1]:
            maps.setdefault(t, set()).add(folders[args[-1]])
    return maps


def scale_trainers(evos, bodies, names, report):
    current_text = open("src/data/trainers.party").read()
    current = parse_party(current_text)
    original = parse_party(git_show(TRAINERS_REV, "src/data/trainers.party"))
    maps = trainer_maps()
    new_parties = {}
    for label, entries in original.items():
        if EXCLUDED.match(label) or label not in current or len(current[label]) != 1 or len(entries) != 1:
            continue
        mons = entries[0][1]
        if not mons:
            continue
        folders = maps.get(label, set())
        parts = [map_part(f) for f in folders]
        if not folders or None in parts:
            continue  # not fought in Hoenn's adventure (unused, or after the League)
        old_levels = [int(re.search(r"^Level: (\d+)", m, re.M).group(1)) for m in mons]
        part = max(parts + [level_part(max(old_levels))])
        new_mons = []
        for mon, old in zip(mons, old_levels):
            level = scale(old, part)
            name = mon_species(mon)
            const = species_constant(name)
            const = ALIASES.get(const, const)
            if const not in evos:
                raise SystemExit("scale_levels.py: unknown species %s (%s)" % (name, label))
            target = const
            while True:
                nxt = trainer_evolution(evos, target, old, level)
                if not nxt:
                    break
                target = nxt
            lines = mon.split("\n")
            lines = [re.sub(r"^Level: \d+", "Level: %d" % level, line) for line in lines]
            if target != const:
                lines[0] = lines[0].replace(name, names[target], 1)
                report["evolutions"].append((label, name, old, names[target], level))
                ability = [line for line in lines if line.startswith("Ability: ")]
                abilities = re.search(r"\.abilities = \{([^}]*)\}", bodies[target]).group(1)
                if ability and "ABILITY_" + species_constant(ability[0][9:]) not in abilities:
                    lines = [line for line in lines if not line.startswith("Ability: ")]
            new_mons.append("\n".join(lines))
        new_parties[label] = new_mons
        report["trainers"].append((label, sorted(folders), part, old_levels, [scale(o, part) for o in old_levels]))
    out = []
    for block in re.split(r"\n(?==== )", current_text):
        m = re.match(r"=== (TRAINER_\w+) ===\n", block)
        if m and m.group(1) in new_parties:
            header = block.split("\n\n")[0]
            block = header + "\n\n" + "\n\n".join(new_parties[m.group(1)]) + "\n"
        out.append(block)
    text = "\n".join(out)
    if not text.endswith("\n"):
        text += "\n"
    open("src/data/trainers.party", "w").write(text)


# --- Wild Pokémon

def scale_wild(report):
    folders = {json.load(open(f))["id"]: f.split("/")[2] for f in glob.glob("data/maps/*/map.json")}
    path = "src/data/wild_encounters.json"
    data = json.load(open(path))
    original = {e["base_label"]: e for e in json.loads(git_show(WILD_REV, path))["wild_encounter_groups"][0]["encounters"]}
    group = data["wild_encounter_groups"][0]
    rods = {i: rod for rod, slots in [f for f in group["fields"] if f["type"] == "fishing_mons"][0]["groups"].items() for i in slots}
    for e in group["encounters"]:
        label = e["base_label"]
        if label.endswith(("_FireRed", "_LeafGreen")) or e["map"] not in folders:
            continue
        part = map_part(folders[e["map"]])
        if part is None:
            continue
        # A night table added after step 4.1 has the levels of the day table of its map
        before = (original.get(label) or original.get(LEVELS_FROM.get(label))
                  or (original.get(label[:-len("_Night")]) if label.endswith("_Night") else None))
        for area, table in e.items():
            if not area.endswith("_mons"):
                continue
            ranges = []
            for i, mon in enumerate(table["mons"]):
                try:
                    old = before[area]["mons"][i]
                except (TypeError, KeyError, IndexError):
                    report["unmatched"].append((label, area, i))
                    continue
                p = max(part, AREA_PARTS.get(area, 0), ROD_PARTS[rods[i]] if area == "fishing_mons" else 0)
                mon["min_level"] = scale(old["min_level"], p)
                mon["max_level"] = max(mon["min_level"], scale(old["max_level"], p))
                ranges.append((old["min_level"], old["max_level"], mon["min_level"], mon["max_level"]))
            if ranges:
                report["wild"].append((folders[e["map"]], label, area, ranges))
    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def scale_static(report):
    for path, name in STATIC_POKEMON:
        part = STATIC_PARTS[path.split("/")[-2] if "maps" in path else path.split("/")[-1]]
        old = int(re.search(r"setwildbattle SPECIES_%s, (\d+)" % name, git_show(TRAINERS_REV, path)).group(1))
        text = open(path).read()
        text = re.sub(r"(setwildbattle SPECIES_%s, )\d+" % name, r"\g<1>%d" % scale(old, part), text)
        open(path, "w").write(text)
        report["static"].append((path, name, old, scale(old, part)))


# --- Review sheet

def write_doc(report):
    def rng(levels):
        return "%d-%d" % (min(levels), max(levels)) if min(levels) != max(levels) else str(levels[0])
    lines = ["# Niveaux des dresseurs ordinaires et des Pokémon sauvages (étape 4.3)", "",
             "Généré par `python3 dev_scripts/nabla/scale_levels.py` : ne pas modifier à la main. "
             "Pour rééquilibrer une étape de l'aventure, changer son facteur (`PARTS`) ou la place d'une map "
             "(`MAP_PARTS`) dans le script et le relancer : il repart toujours des niveaux d'origine.", "",
             "## Facteurs", "",
             "Un niveau est multiplié par le facteur de l'étape où on le rencontre (arrondi). Facteur = level cap "
             "Nabla ÷ niveau du Pokémon le plus fort du Champion d'origine.", "",
             "| Étape | Champion d'origine → cap | Facteur |", "|---|---|---|"]
    for i, (name, leader, cap) in enumerate(PARTS):
        ref = "Conseil 4 : Damien 46 → 66" if i == VICTORY_ROAD else "%d → %d" % (leader, cap)
        lines.append("| %s | %s | ×%.2f |" % (name, ref, factor(i)))
    lines += ["", "- Un dresseur prend l'étape de sa map, ou celle de son niveau d'origine si elle est plus tardive "
              "(dresseurs en Surf, revanches).",
              "- Pokémon sauvages : au plus tôt l'étape où on les rencontre (Surf : 5ᵉ badge, Éclate-Roc : 3ᵉ, "
              "Canne : 1er, Super Canne : 5ᵉ, Méga Canne : 6ᵉ).",
              "- Évolutions : un Pokémon de dresseur évolue quand le relèvement lui fait atteindre son niveau "
              "d'évolution ; les évolutions par échange, objet, bonheur… se font au niveau %d. Les Pokémon sauvages "
              "évoluent dans le jeu, selon leur niveau (même règle)." % OTHER_EVOLUTIONS_LEVEL,
              "- Non touchés : dresseurs de l'étape 4.2, revanches des Champions, après la Ligue, Safari (niveaux "
              "selon les badges), zones Nabla (réglées avec les zones voisines), légendaires et cadeaux.", ""]
    lines += ["## Étape de chaque map", "", "| Étape | Maps |", "|---|---|"]
    for part, prefixes in MAP_PARTS:
        lines.append("| %s | %s |" % (PARTS[part][0] if part is not None else "Non touchées", ", ".join(prefixes.split())))
    lines += ["", "## Pokémon fixes", "", "| Script | Pokémon | Avant | Après |", "|---|---|---|---|"]
    for path, name, old, new in report["static"]:
        lines.append("| `%s` | %s | %d | %d |" % (path, name.title(), old, new))
    lines += ["", "## Évolutions des Pokémon de dresseurs", "", "| Dresseur | Avant | Après |", "|---|---|---|"]
    for label, name, old, target, level in report["evolutions"]:
        lines.append("| `%s` | %s %d | %s %d |" % (label, name, old, target, level))
    lines += ["", "## Dresseurs", "", "| Dresseur | Map | Étape | Avant | Après |", "|---|---|---|---|---|"]
    for label, folders, part, old, new in sorted(report["trainers"], key=lambda t: (t[2], t[1], t[0])):
        lines.append("| `%s` | %s | %s | %s | %s |" % (label, ", ".join(folders), PARTS[part][0], rng(old), rng(new)))
    names = {"land_mons": "herbes", "water_mons": "Surf", "rock_smash_mons": "Éclate-Roc", "fishing_mons": "pêche"}
    lines += ["", "## Pokémon sauvages", "", "| Map | Table | Zone | Avant | Après |", "|---|---|---|---|---|"]
    for folder, label, area, ranges in report["wild"]:
        lines.append("| %s | `%s` | %s | %d-%d | %d-%d |" % (folder, label, names[area], min(r[0] for r in ranges),
                     max(r[1] for r in ranges), min(r[2] for r in ranges), max(r[3] for r in ranges)))
    if report["unmatched"]:
        lines += ["", "## Emplacements sans niveau d'origine (laissés tels quels)", ""]
        lines += ["- `%s` %s, emplacement %d" % u for u in report["unmatched"]]
    open(DOC, "w").write("\n".join(lines) + "\n")


def main():
    species = st.load_species()
    bodies = {name: body for name, body in st.species_entries()}
    evos = {name: cv.evolutions(body) for name, body in bodies.items()}
    names = {}
    for name, body in bodies.items():
        m = re.search(r'\.speciesName = _\("([^"]+)"\)', body)
        shown = m.group(1) if m else name
        names[name] = shown if species_constant(shown) == name else "-".join(p.capitalize() for p in name.split("_"))
    report = {"trainers": [], "evolutions": [], "wild": [], "static": [], "unmatched": []}
    scale_trainers(evos, bodies, names, report)
    scale_wild(report)
    scale_static(report)
    write_doc(report)
    print("%d trainers, %d evolutions, %d wild tables, %d static Pokémon; %d slots without original levels"
          % (len(report["trainers"]), len(report["evolutions"]), len(report["wild"]), len(report["static"]),
             len(report["unmatched"])))


if __name__ == "__main__":
    main()
