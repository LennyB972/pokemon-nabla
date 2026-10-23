#!/usr/bin/env python3
"""Reports which Pokémon can be obtained in Pokémon Nabla, in docs/nabla/couverture.md.

A species is obtainable if it can be caught or received (wild encounters, Safari Zone regions,
gifts, static encounters, trades), hatched from an obtainable species, or evolved from one with
an obtainable item. Cosmetic forms count with their species; regional forms count apart.
Evolutions with a condition that the script can't check (battles, moves...) are listed to be
checked in the game.

Usage (from the repo root): python3 dev_scripts/nabla/coverage.py
"""
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import safari_tables as st

DOC = "docs/nabla/couverture.md"
SAFARI_LABEL = re.compile(r"_(%s)$" % "|".join(st.SAFARI_REGIONS))
NOT_SPECIES = ("_MEGA", "_GMAX", "_TOTEM", "_PRIMAL")
# Conditions the game handles and the player can meet (time, friendship, battles...)
# Regions of the regional evolutions in each Safari Zone region (sSafariZoneRegions, src/nabla_safari_zone.c)
SAFARI_EVOLUTION_REGIONS = {"Kanto": ("REGION_KANTO",), "Johto": ("REGION_JOHTO",), "Sinnoh": ("REGION_SINNOH",),
                            "Unova": ("REGION_UNOVA",), "Kalos": ("REGION_KALOS",), "Alola": ("REGION_ALOLA",),
                            "Galar": ("REGION_GALAR", "REGION_HISUI"), "Paldea": ("REGION_PALDEA",)}
CHECK_IN_GAME = {"IF_RECOIL_DAMAGE_GE", "IF_CRITICAL_HITS_GE", "IF_CURRENT_DAMAGE_GE", "IF_MIN_OVERWORLD_STEPS",
                 "IF_MIN_BEAUTY", "IF_WEATHER", "IF_IN_MAP", "IF_IN_MAPSEC", "IF_DEFEAT_X_WITH_ITEMS"}


def split_top(text, sep=","):
    # Splits on the separators that are not inside brackets
    parts, depth, start = [], 0, 0
    for i, c in enumerate(text):
        depth += c in "([{"
        depth -= c in ")]}"
        if c == sep and depth == 0:
            parts.append(text[start:i].strip())
            start = i + 1
    return parts + [text[start:].strip()]


def evolutions(body):
    # [(method, param, target, [(condition, args...)])] of a species
    m = re.search(r"\.evolutions = EVOLUTION\(", body)
    if not m:
        return []
    depth, i = 1, m.end()
    while depth:
        depth += body[i] == "("
        depth -= body[i] == ")"
        i += 1
    text = "\n".join(line for line in body[m.end():i - 1].split("\n") if not line.strip().startswith("#"))
    result = []
    for entry in split_top(text):
        fields = split_top(entry.strip(" ,")[1:-1]) if entry.strip(" ,").startswith("{") else []
        if len(fields) < 3:
            continue
        conditions = []
        if len(fields) > 3 and fields[3].startswith("CONDITIONS("):
            conditions = [tuple(split_top(c.strip()[1:-1])) for c in split_top(fields[3][len("CONDITIONS("):-1])]
        result.append((fields[0], fields[1], fields[2].replace("SPECIES_", ""), conditions))
    return result


def place(map_id):
    return re.sub(r"(\D)(\d)", r"\1 \2", map_id[4:].replace("_", " ").title())


def emerald_scripts():
    files = [f for f in glob.glob("data/maps/*/scripts.inc") if not f.split("/")[2].endswith("_Frlg")]
    files += [f for f in re.findall(r'\.include "(data/scripts/[^"]+)"', open("data/event_scripts.s").read())
              if "frlg" not in f and not f.endswith("debug.inc")]
    return {f: open(f).read() for f in files}


def main():
    species = st.load_species()
    bodies = {name: body for name, body in st.species_entries()}
    evos = {name: evolutions(body) for name, body in bodies.items()}
    scripts = emerald_scripts()

    def node(name):
        return (species[name]["dex"], st.region_of(name, species[name]))

    def is_species(name):
        return name in species and species[name]["dex"] is not None and not any(x in name for x in NOT_SPECIES)

    # --- Pokémon sources
    sources = {}
    wild = set()

    def add(name, source):
        if is_species(name):
            sources.setdefault(name, source)
    # Wild Pokémon evolve with their level (see scale_levels.wild_forms); the Safari Zone's levels follow the badges
    import scale_levels as sl
    for e in json.load(open("src/data/wild_encounters.json"))["wild_encounter_groups"][0]["encounters"]:
        label = e["base_label"]
        if label.endswith(("_FireRed", "_LeafGreen")):
            continue
        region = SAFARI_LABEL.search(label)
        if e["map"].startswith("MAP_SAFARI_ZONE") and not region:
            continue  # the Safari Zone always uses a region table
        regions = SAFARI_EVOLUTION_REGIONS.get(region.group(1), ("REGION_HOENN",)) if region else ("REGION_HOENN",)
        for kind, table in e.items():
            if kind.endswith("_mons"):
                for mon in table["mons"]:
                    if region:
                        levels = [5] if region.group(1) == "Starters" else range(5, 73)
                    else:
                        levels = range(mon["min_level"], mon["max_level"] + 1)
                    for name in set().union(*(sl.wild_forms(evos, mon["species"][8:], level, regions) for level in levels)):
                        add(name, "Safari " + region.group(1) if region else place(e["map"]))
                        wild.add(name)
    add("FEEBAS", "Route 119")
    wild.add("FEEBAS")
    for f, text in scripts.items():
        for cmd, name in re.findall(r"^\s*(givemon|giveegg|setwildbattle)\s+SPECIES_(\w+)", text, re.M):
            add(name, ("fixe" if cmd == "setwildbattle" else "cadeau") + " (" + f.split("/")[-2 if "maps" in f else -1] + ")")
    trades = open("include/constants/trade.h").read().split("// FRLG")[0]
    trade_data = open("src/data/trade.h").read()
    for trade in re.findall(r"INGAME_TRADE_(\w+),", trades):
        add(re.search(r"\[INGAME_TRADE_%s\] =.*?\.species = SPECIES_(\w+)" % trade, trade_data, re.S).group(1), "échange")
    add("LATIAS", "vagabond")

    # --- Item sources
    items = {}
    for f, text in scripts.items():
        for line in text.split("\n"):
            if re.search(r"giveitem|finditem|\.2byte ITEM_", line):
                for item in re.findall(r"ITEM_\w+", line):
                    items.setdefault(item, "boutique ou script (" + f.split("/")[-2 if "maps" in f else -1] + ")")
    for f in glob.glob("data/maps/*/map.json"):
        if not f.split("/")[2].endswith("_Frlg"):
            for item in re.findall(r"ITEM_\w+", open(f).read()):
                items.setdefault(item, "au sol (" + f.split("/")[2] + ")")
    pickup = open("src/battle_script_commands.c").read().split("sPickupTable[] =", 1)[1].split("};", 1)[0]
    for item in re.findall(r"ITEM_\w+", pickup):
        items.setdefault(item, "Ramassage")
    for item in re.findall(r"ITEM_\w+", open("data/maps/BattleFrontier_ExchangeServiceCorner/scripts.inc").read()):
        items.setdefault(item, "Échange de PCo")

    # Evolutions triggered by a script of the game (Runerigus: Route 111 carvings)
    triggers = {t for text in scripts.values() for t in re.findall(r"tryspecialevo (EVO_TRIGGER_\w+)", text)}

    # --- Obtainable species: sources, then breeding and evolutions until nothing changes
    reached = {name: source for name, source in sources.items()}
    special = {}
    changed = True
    while changed:
        changed = False
        # Held items of wild Pokémon (Thief, Covet)
        for name in [n for n in wild if n in reached]:
            for item in re.findall(r"\.item(?:Common|Rare) = (ITEM_\w+)", bodies.get(name, "")):
                if item not in items:
                    items[item] = "tenu par " + name.title() + " sauvage"
                    changed = True
        for name in list(reached):
            # Breeding gives the first stage of the line
            base = name
            while species[base]["pre"]:
                base = species[base]["pre"]
            if is_species(base) and base not in reached and "EGG_GROUP_NO_EGGS_DISCOVERED" not in bodies[name] and not species[name]["legend"]:
                reached[base] = "œuf de " + name.title()
                changed = True
            for method, param, target, conditions in evos.get(name, []):
                if not is_species(target) or target in reached:
                    continue
                needed = [param] if method == "EVO_ITEM" else []
                needed += ["ITEM_LINKING_CORD"] if method == "EVO_TRADE" else []
                needed += ["ITEM_POKE_BALL"] if method == "EVO_SPLIT_FROM_EVO" else []
                needed += [c[1] for c in conditions if c[0] in ("IF_HOLD_ITEM", "IF_BAG_ITEM_COUNT")]
                if method == "EVO_NONE" or (method == "EVO_SCRIPT_TRIGGER" and param not in triggers) or any(i not in items for i in needed):
                    continue
                if any(c[0] in ("IF_TRADE_PARTNER_SPECIES",) for c in conditions):
                    continue
                if any(c[0] == "IF_SPECIES_IN_PARTY" and c[1].replace("SPECIES_", "") not in reached for c in conditions):
                    continue
                moves = [c[1] for c in conditions if c[0] in ("IF_KNOWS_MOVE", "IF_USED_MOVE_X_TIMES")]
                learnset = level_up_moves(bodies, species, name)
                checks = [c for c in conditions if c[0] in CHECK_IN_GAME] + [("move",) + (m,) for m in moves if m not in learnset]
                if [c for c in checks if c[0] == "move"]:
                    special[(name, target)] = checks
                    continue
                if checks or method in ("EVO_SPIN", "EVO_BATTLE_END", "EVO_SCRIPT_TRIGGER"):
                    special[(name, target)] = checks + ([(method,) + ((param,) if method == "EVO_SCRIPT_TRIGGER" else ())] if method in ("EVO_SPIN", "EVO_BATTLE_END", "EVO_SCRIPT_TRIGGER") else [])
                reached[target] = "évolution de " + name.title()
                changed = True

    # --- Report by node (a species and its cosmetic forms)
    all_nodes, reached_nodes, legend_nodes, names = set(), set(), set(), {}
    for name in species:
        if not is_species(name):
            continue
        nd = node(name)
        all_nodes.add(nd)
        names.setdefault(nd, name)
        if species[name]["legend"]:
            legend_nodes.add(nd)
        if name in reached:
            reached_nodes.add(nd)
    missing = sorted(all_nodes - reached_nodes - legend_nodes, key=lambda nd: (nd[0], str(nd[1])))
    missing_legends = sorted(legend_nodes - reached_nodes, key=lambda nd: (nd[0], str(nd[1])))
    blocked = {}
    for name in species:
        if is_species(name) and node(name) in missing:
            for pre in [p for p in species if any(t == name for _, _, t, _ in evos.get(p, []))]:
                if pre in reached:
                    for method, param, target, conditions in evos[pre]:
                        if target == name:
                            blocked[node(name)] = f"évolution de {pre.title()} impossible ({method}, {param}, {conditions})"
    evo_items = sorted({i for name in reached for method, param, _, conditions in evos.get(name, [])
                        for i in ([param] if method == "EVO_ITEM" else []) + [c[1] for c in conditions if c[0] in ("IF_HOLD_ITEM", "IF_BAG_ITEM_COUNT")]})

    lines = ["# Couverture des Pokémon", "",
             "Généré par `python3 dev_scripts/nabla/coverage.py`. Une espèce (formes cosmétiques comprises) est obtenable si on",
             "peut la capturer ou la recevoir, la faire éclore ou y faire évoluer une espèce obtenable avec un objet trouvable.",
             "",
             f"- **Espèces obtenables** : {len(reached_nodes - legend_nodes)} / {len(all_nodes - legend_nodes)} hors légendaires et fabuleux.",
             f"- **Légendaires et fabuleux** : {len(legend_nodes & reached_nodes)} / {len(legend_nodes)} (les autres : phase 7).",
             "", "## Espèces manquantes (hors légendaires)", ""]
    lines += [f"- {names[nd].title()}" + (f" : {blocked[nd]}" if nd in blocked else " : aucune source") for nd in missing] or ["Aucune."]
    lines += ["", "## Légendaires et fabuleux obtenables", "",
              ", ".join(sorted(names[nd].title() for nd in legend_nodes & reached_nodes)), "",
              "## Évolutions à vérifier en jeu", "",
              "Conditions que le script ne peut pas vérifier (combat, pas, météo, lieu, capacité hors niveau).", ""]
    labels = {"move": "capacité absente de ses capacités par niveau", "EVO_SPIN": "tourner sur soi-même",
              "EVO_BATTLE_END": "fin de combat", "EVO_SCRIPT_TRIGGER": "script"}
    shown = {}  # one line per species, whatever its form
    for (name, target), checks in sorted(special.items()):
        what = ", ".join(labels.get(c[0], c[0]) + (" " + " ".join(c[1:]) if len(c) > 1 else "") for c in checks)
        shown.setdefault((names[node(name)], names[node(target)]), what)
    lines += [f"- {name.title()} → {target.title()} : {what}" for (name, target), what in shown.items()]
    lines += ["", "## Objets d'évolution", "", "| Objet | Où |", "|---|---|"]
    lines += [f"| {i[5:].replace('_', ' ').title()} | {items.get(i, '**introuvable**')} |" for i in evo_items]
    open(DOC, "w").write("\n".join(lines) + "\n")
    print(f"{len(reached_nodes - legend_nodes)} / {len(all_nodes - legend_nodes)} species, {len(missing)} missing, {len(shown)} to check: {DOC}")


def level_up_moves(bodies, species, name):
    # Level-up moves of the species and of its pre-evolutions
    moves = set()
    while name:
        learnset = re.search(r"\.levelUpLearnset = (\w+)", bodies.get(name, ""))
        if learnset:
            moves |= LEARNSETS.get(learnset.group(1), set())
        name = species[name]["pre"]
    return moves


# Level-up learnsets of the generation chosen by P_LVL_UP_LEARNSETS
LEARNSETS_GEN = re.search(r"#define P_LVL_UP_LEARNSETS\s+GEN_(\w+)", open("include/config/pokemon.h").read()).group(1)
LEARNSETS = {label: set(re.findall(r"MOVE_\w+", body)) for label, body in re.findall(
    r"(s\w+LevelUpLearnset)\[\] = \{(.*?)\};", open(f"src/data/pokemon/level_up_learnsets/gen_{'9' if LEARNSETS_GEN == 'LATEST' else LEARNSETS_GEN}.h").read(), re.S)}

if __name__ == "__main__":
    main()
