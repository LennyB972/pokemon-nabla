#!/usr/bin/env python3
"""Prints the Markdown tables of every Nabla item placed on a map, for docs/nabla/items.md.

Usage (from the repo root): python3 dev_scripts/nabla/list_items.py
"""
import glob
import json

hidden, visible = [], []
for path in sorted(glob.glob("data/maps/*/map.json")):
    map_json = json.load(open(path))
    name = path.split("/")[2]
    for event in map_json.get("bg_events") or []:
        if event.get("flag", "").startswith("FLAG_NABLA_"):
            hidden.append((name, event["x"], event["y"], event["item"], event["flag"]))
    for event in map_json.get("object_events") or []:
        if event.get("flag", "").startswith("FLAG_NABLA_ITEM_"):
            visible.append((name, event["x"], event["y"], event["trainer_sight_or_berry_tree_id"], event["flag"]))

for title, rows in (("Objets cachés", hidden), ("Objets au sol", visible)):
    print(f"### {title}\n\n| Map | Case (x, y) | Objet | Flag |\n|---|---|---|---|")
    for row in rows:
        print("| {} | {}, {} | `{}` | `{}` |".format(*row))
    print()
