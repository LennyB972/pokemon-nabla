#!/usr/bin/env python3
"""Lists the wild encounters of Hoenn, map by map in the order of the adventure, in docs/nabla/rencontres.md.

For each table: the share of each species (encounter slots added up), its levels, what it is met as in the
game (wild Pokémon evolve with their level), and the changes since Pokémon Emerald. The Safari Zone's
region tables are listed in docs/nabla/safari.md.

Usage (from the repo root): python3 dev_scripts/nabla/list_encounters.py
"""
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import coverage as cv
import safari_tables as st
import scale_levels as sl

DOC = "docs/nabla/rencontres.md"
ENCOUNTERS = "src/data/wild_encounters.json"
AREAS = [("land_mons", "Herbes"), ("water_mons", "Surf"), ("rock_smash_mons", "Éclate-Roc"), ("fishing_mons", "Pêche")]
RODS = {"old_rod": "Canne", "good_rod": "Super Canne", "super_rod": "Méga Canne"}


def map_name(folder):
    # "GraniteCave_B1F" -> "Granite Cave B1F"
    return re.sub(r"(?<=[a-z])(?=[A-Z0-9])", " ", folder).replace("_", " ")


def title(name):
    return "-".join(p.capitalize() for p in name.split("_"))


def summary(mons, rates, evos):
    # "Zigzagoon 40 % (2-3)" for each species, the most common first
    shares = {}
    for mon, rate in zip(mons, rates):
        name = mon["species"][8:]
        share, low, high = shares.get(name, (0, 100, 0))
        shares[name] = (share + rate, min(low, mon["min_level"]), max(high, mon["max_level"]))
    parts = []
    for name, (share, low, high) in sorted(shares.items(), key=lambda s: -s[1][0]):
        text = "%s %d %% (%s)" % (title(name), share, low if low == high else "%d-%d" % (low, high))
        forms = set().union(*(sl.wild_forms(evos, name, level) for level in range(low, high + 1)))
        others = sorted(forms - {name})
        if others:
            text += " → en jeu : %s%s" % (", ".join(title(o) for o in others), " (selon le niveau)" if name in forms else "")
        parts.append(text)
    return " · ".join(parts)


def species_of(table, slots=None):
    return {m["species"][8:] for i, m in enumerate(table["mons"]) if slots is None or i in slots}


def main():
    bodies = {name: body for name, body in st.species_entries()}
    evos = {name: cv.evolutions(body) for name, body in bodies.items()}
    folders = {json.load(open(f))["id"]: f.split("/")[2] for f in glob.glob("data/maps/*/map.json")}
    group = json.load(open(ENCOUNTERS))["wild_encounter_groups"][0]
    original = {e["base_label"]: e for e in json.loads(sl.git_show(sl.TRAINERS_REV, ENCOUNTERS))["wild_encounter_groups"][0]["encounters"]}
    rates = {f["type"]: f["encounter_rates"] for f in group["fields"]}
    rods = [f for f in group["fields"] if f["type"] == "fishing_mons"][0]["groups"]

    tables = []
    for e in group["encounters"]:
        label = e["base_label"]
        folder = folders.get(e["map"], "")
        if label.endswith(("_FireRed", "_LeafGreen")) or folder.startswith("SafariZone") or "Unused" in folder or not folder:
            continue
        part = sl.map_part(folder)
        order = len(sl.PARTS) if part is None else part
        tables.append((order, folder, label, e))
    tables.sort(key=lambda t: (t[0], t[1], t[2]))

    changed = 0
    lines = ["# Rencontres des Pokémon sauvages", "",
             "Généré par `python3 dev_scripts/nabla/list_encounters.py` : ne pas modifier à la main (pour changer "
             "des rencontres, écrire les changements dans le chat ou dans une fiche à part).", "",
             "- Pour chaque espèce : sa part des rencontres de la zone (emplacements additionnés) et ses niveaux. "
             "« → en jeu » : les Pokémon sauvages évoluent selon leur niveau (échange, objet, bonheur… à partir du "
             "niveau %d)." % sl.OTHER_EVOLUTIONS_LEVEL,
             "- Emplacements d'une zone d'herbes : 20, 20, 10, 10, 10, 10, 5, 5, 4, 4, 1, 1 % ; Surf et Éclate-Roc : "
             "60, 30, 5, 4, 1 % ; Canne : 70, 30 % ; Super Canne : 60, 20, 20 % ; Méga Canne : 40, 40, 15, 4, 1 %.",
             "- « Nuit » : table utilisée la nuit (sinon la même table jour et nuit).",
             "- Changements depuis Émeraude : espèces ajoutées (+) et retirées (−) dans chaque zone.",
             "- Le Safari a ses propres tables par région : `docs/nabla/safari.md`. Barpau : cases spéciales de la "
             "Route 119, niveaux 20-25.", ""]
    current_part = None
    for order, folder, label, e in tables:
        if order != current_part:
            current_part = order
            lines += ["## " + (sl.PARTS[order][0] if order < len(sl.PARTS) else "Hors aventure (après la Ligue, zones Nabla)"), ""]
        name = map_name(folder) + (" (nuit)" if label.endswith("_Night") else "")
        if folder == "AlteringCave":
            name += " (table %s)" % re.search(r"(\d+)$", label).group(1)
        before = original.get(label) or (original.get(label[:-len("_Night")]) if label.endswith("_Night") else None)
        lines.append("### " + name)
        if before is None:
            lines.append("- *Table ajoutée par Nabla.*")
        for area, area_name in AREAS:
            if area not in e:
                continue
            table = e[area]
            groups = [(RODS[rod], slots) for rod, slots in rods.items()] if area == "fishing_mons" else [(area_name, None)]
            for group_name, slots in groups:
                mons = [m for i, m in enumerate(table["mons"]) if slots is None or i in slots]
                group_rates = [r for i, r in enumerate(rates[area]) if slots is None or i in slots]
                text = "- **%s** : %s" % (group_name, summary(mons, group_rates, evos))
                if before is not None:
                    old = species_of(before[area], slots) if area in before else set()
                    new = species_of(table, slots)
                    diff = ["+" + title(s) for s in sorted(new - old)] + ["−" + title(s) for s in sorted(old - new)]
                    if diff:
                        text += " — *changé : %s*" % ", ".join(diff)
                        changed += 1
                lines.append(text)
        lines.append("")
    open(DOC, "w").write("\n".join(lines))
    print("%d tables, %d zones changed since Emerald: %s" % (len(tables), changed, DOC))


if __name__ == "__main__":
    main()
