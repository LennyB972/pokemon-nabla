#!/usr/bin/env python3
"""Draws the NablaFlowerParadise map (data/layouts/NablaFlowerParadise/map.bin), a mirage of the Eon Flute.

A clearing in the forest (tilesets General and Mauville), drawn from a plan like the Emerald Forest
(draw_emerald_forest.py): in its middle, a field of the flowers of Route 117's beds (pink and yellow, without
their fences) where Shaymin waits; to the east, a corner of jungle (tall grass and small trees) where Zarude waits;
to the west, a pond (pieces of Route 102's pond). The player arrives at the south of the clearing.

Running it again overwrites the map, including changes made in Porymap since.
Usage (from the repo root): python3 dev_scripts/nabla/draw_flower_paradise.py
"""
import struct
import sys

import draw_emerald_forest as forest
import reach

NAME = "NablaFlowerParadise"
# One character = two columns: "#" forest trees, "%" small trees, "." grass, "T" tall grass
PLAN = [
    "##################",
    "##################",
    "##################",
    "#######....#######",
    "#####........#####",
    "###............###",
    "###............###",
    "##..............##",
    "##..............##",
    "##.........TT%%.##",
    "##........TTT%%T##",
    "##........TTTTTT##",
    "##.........TTTT.##",
    "###............###",
    "###............###",
    "#####........#####",
    "#######....#######",
    "########..########",
    "##################",
    "##################",
]
W, H = 2 * len(PLAN[0]), len(PLAN)
LEGENDARIES = {"SHAYMIN": (14, 8), "ZARUDE": (27, 12)}
ARRIVAL = (17, 16)
FLOWERS = (14, 8, 7.5, 3.6)                    # the field of flowers: an ellipse (x, y, half width, half height) on grass
POND = (6, 11, 4, 2)                                   # x, y, width, height of the water
SMALL_FLOWERS = [(5, 7), (6, 9), (11, 14), (12, 14), (20, 14), (22, 13), (24, 6), (25, 7)]

if not forest.draw(NAME, PLAN, [], [], forest.BIG_TREES_BORDER, start=ARRIVAL):
    sys.exit(1)
path = "data/layouts/%s/map.bin" % NAME
raw = open(path, "rb").read()
out = [[struct.unpack_from("<H", raw, 2 * (y * W + x))[0] for x in range(W)] for y in range(H)]
GRASS = forest.block(0x001)

# The flowers of Route 117's beds: pink (0x208-0x20f) and yellow (0x210-0x217) in turn, their variants mixed
route117 = open("data/layouts/Route117/map.bin", "rb").read()
bed = struct.unpack_from("<H", route117, 2 * (4 * 60 + 9))[0] & ~0x3FF  # collision and elevation of a bed
cx, cy, rx, ry = FLOWERS
for y in range(H):
    for x in range(W):
        if ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 <= 1 and out[y][x] == GRASS:
            out[y][x] = bed | (0x208 if (x + y) % 2 else 0x210) + (x + 3 * y) % 8
for x, y in SMALL_FLOWERS:
    assert out[y][x] == GRASS, (x, y)
    out[y][x] = forest.block(0x004)
# The pond of Route 102
route102 = open("data/layouts/Route102/map.bin", "rb").read()
pond = lambda x, y: struct.unpack_from("<H", route102, 2 * (y * 50 + x))[0]
px, py, pw, ph = POND
for y in range(py, py + ph + 1):
    for x in range(px, px + pw):
        assert out[y][x] == GRASS, (x, y)
        side = 0 if x == px else 2 if x == px + pw - 1 else 1
        out[y][x] = pond(41, 7) if y == py + ph else ((pond(40, 2), pond(41, 2), pond(43, 2)) if y == py
                                                     else (pond(40, 3), pond(41, 3), pond(43, 3)))[side]

# Every cell reached without the legendaries is reached with them, and they can be reached on foot
cells, talked = reach.reach(out, ARRIVAL, LEGENDARIES.values())
alone, _ = reach.reach(out, ARRIVAL)
assert alone - cells <= set(LEGENDARIES.values()), alone - cells
assert talked == set(LEGENDARIES.values()), set(LEGENDARIES.values()) - talked
open(path, "wb").write(struct.pack("<%dH" % (W * H), *[v for row in out for v in row]))
