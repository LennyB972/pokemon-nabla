#!/usr/bin/env python3
"""Draws the NablaKitakami map (data/layouts/NablaKitakami/map.bin), a mirage of the Eon Flute.

A clearing in the forest (tilesets General and Fortree), drawn from a plan like the Emerald Forest
(draw_emerald_forest.py): a field of tall grass to the north-west, where Okidogi waits, another to the south, where
Ogerpon waits, a grove of small trees to the west, and in the middle a square of grass with flowers and rocks around
the altar, like the Loyalty Plaza: Pecharunt appears next to it. Munkidori waits to the north, Fezandipiti to the
east, above a pond (pieces of Route 102's pond, like in the Flower Paradise). The player arrives at the south of the
clearing.

Running it again overwrites the map, including changes made in Porymap since.
Usage (from the repo root): python3 dev_scripts/nabla/draw_kitakami.py
"""
import struct
import sys

import draw_emerald_forest as forest
import reach

NAME = "NablaKitakami"
# One character = two columns: "#" forest trees, "%" small trees, "." grass, "T" tall grass
PLAN = [
    "####################",
    "####################",
    "#######.....########",
    "#####.........######",
    "###...TTT.......####",
    "##...TTTTT.%%....###",
    "##..TTTTT..%%.....##",
    "##..TTTT..........##",
    "##...............###",
    "##...............###",
    "##..%%...........###",
    "##..%%............##",
    "##................##",
    "###.......TTTT....##",
    "####.....TTTTTT..###",
    "#####.....TTTT..####",
    "#######........#####",
    "#########..#########",
    "####################",
    "####################",
]
W, H = 2 * len(PLAN[0]), len(PLAN)
LEGENDARIES = {"OKIDOGI": (10, 6), "MUNKIDORI": (16, 3), "FEZANDIPITI": (32, 8), "OGERPON": (24, 14)}
ALTAR, PECHARUNT = (20, 9), (22, 9)
ARRIVAL = (20, 16)
# The square around the altar: flowers at its corners, rocks on its sides
DETAILS = [("f", 17, 7), ("f", 23, 7), ("f", 17, 11), ("f", 23, 11), ("o", 16, 9), ("o", 25, 9)]
POND = (28, 10, 5, 2)                                  # x, y, width, height of the water

if not forest.draw(NAME, PLAN, DETAILS, [], forest.BIG_TREES_BORDER, start=ARRIVAL):
    sys.exit(1)
path = "data/layouts/%s/map.bin" % NAME
raw = open(path, "rb").read()
out = [[struct.unpack_from("<H", raw, 2 * (y * W + x))[0] for x in range(W)] for y in range(H)]
GRASS = forest.block(0x001)
route102 = open("data/layouts/Route102/map.bin", "rb").read()
pond = lambda x, y: struct.unpack_from("<H", route102, 2 * (y * 50 + x))[0]
px, py, pw, ph = POND
for y in range(py, py + ph + 1):
    for x in range(px, px + pw):
        assert out[y][x] == GRASS, (x, y)
        side = 0 if x == px else 2 if x == px + pw - 1 else 1
        out[y][x] = pond(41, 7) if y == py + ph else ((pond(40, 2), pond(41, 2), pond(43, 2)) if y == py
                                                     else (pond(40, 3), pond(41, 3), pond(43, 3)))[side]

# Every cell reached without the objects is reached with them, and they can be reached on foot
OBJECTS = {ALTAR, PECHARUNT, *LEGENDARIES.values()}
cells, talked = reach.reach(out, ARRIVAL, OBJECTS)
alone, _ = reach.reach(out, ARRIVAL)
assert alone - cells <= OBJECTS, alone - cells
assert talked == OBJECTS, OBJECTS - talked
open(path, "wb").write(struct.pack("<%dH" % (W * H), *[v for row in out for v in row]))
