#!/usr/bin/env python3
"""Draws the NablaThreeLakes map (data/layouts/NablaThreeLakes/map.bin), a mirage of the Eon Flute.

An island above the sea taken from Southern Island's map (tilesets General and Rustboro): its cliffs, terraces and
stairs, without the dock and its stairs; the forest stays at the back of the island, and on the plateau cleared in
front of it lie three ponds (pieces of Route 102's pond), with Uxie, Mesprit and Azelf on their banks. The player
arrives on the terrace to the south and goes up to the plateau by the stairs to the east. The sea cannot be crossed.

Running it again overwrites the map, including changes made in Porymap since.
Usage (from the repo root): python3 dev_scripts/nabla/draw_three_lakes.py
"""
import struct

import coast
import reach

W, H = 33, 24                 # Southern Island's map, without the last rows of sea
LEGENDARIES = {"UXIE": (8, 9), "MESPRIT": (14, 10), "AZELF": (21, 10)}
ARRIVAL = (15, 16)
PONDS = [(6, 7, 5, 2), (13, 7, 4, 3), (19, 7, 5, 3)]   # x, y, width, height of the water
FLOWERS = [(5, 8), (5, 9), (11, 8), (12, 9), (17, 9), (18, 8), (25, 8), (25, 9)]

src = open("data/layouts/SouthernIsland_Exterior/map.bin", "rb").read()
src = [[struct.unpack_from("<H", src, 2 * (y * W + x))[0] for x in range(W)] for y in range(30)]
route102 = open("data/layouts/Route102/map.bin", "rb").read()
pond = lambda x, y: struct.unpack_from("<H", route102, 2 * (y * 50 + x))[0]
mt = lambda v: v & 0x3FF
TREE, TREE_BOTTOM, GRASS = src[3][10], src[6][4], src[7][13]       # 0x0c6, 0x016, 0x001
SEA, WATERLINE, CLIFF_BASE, FACE = src[25][0], src[20][19], src[19][13], src[18][13]  # 0x170, 0x189, 0x0a9, 0x07c
FOREST = (0x0c6, 0x016, 0x307, 0x30f, 0x317, 0x00e, 0x003, 0x2c0, 0x0ce)  # trees, the path inside, bushes
# The pond of Route 102: corners and sides of the water, and the grass below it with its bank
POND_TOP, POND_MIDDLE = (pond(40, 2), pond(41, 2), pond(43, 2)), (pond(40, 3), pond(41, 3), pond(43, 3))
BANK = pond(41, 7)

out = [row[:] for row in src[:H]]
# The forest (and the path to the inside of the island) stays at the back of the island, down to row 5 (its trunks);
# the plateau in front of it (rows 6 to 10) is cleared, with the trunks of its trees below. Lower, the trees hide the tops of cliffs: they stay
for y in range(H):
    for x in range(W):
        if mt(out[y][x]) in FOREST and y <= 10:
            out[y][x] = TREE if y < 5 else TREE_BOTTOM if y == 5 else GRASS
for x in [8] + list(range(18, 23)):
    out[11][x] = GRASS
# The tops of the trees seen from the plateau: rounded, like the bushes next to them
for x in range(9, 15):
    out[11][x] = src[11][15]                                         # 0x00e
# The dock and its stairs: cliff and sea
out[18][15] = out[18][16] = FACE
for x in range(14, 18):
    out[19][x] = CLIFF_BASE
for x in range(14, 19):
    out[20][x] = WATERLINE
for y in range(21, H):
    out[y] = [SEA] * W

# The ponds
for px, py, pw, ph in PONDS:
    for y in range(py, py + ph + 1):
        for x in range(px, px + pw):
            assert out[y][x] == GRASS, (x, y)
            side = 0 if x == px else 2 if x == px + pw - 1 else 1
            out[y][x] = BANK if y == py + ph else (POND_TOP if y == py else POND_MIDDLE)[side]
# Flowers on the plateau
for x, y in FLOWERS:
    assert out[y][x] == GRASS, (x, y)
    out[y][x] = coast.block(0x04)

# Every cell reached without the legendaries is reached with them, and they can be reached on foot
cells, talked = reach.reach(out, ARRIVAL, LEGENDARIES.values())
alone, _ = reach.reach(out, ARRIVAL)
assert alone - cells <= set(LEGENDARIES.values()), alone - cells
assert talked == set(LEGENDARIES.values()), set(LEGENDARIES.values()) - talked
assert out[ARRIVAL[1]][ARRIVAL[0]] == GRASS
open("data/layouts/NablaThreeLakes/map.bin", "wb").write(struct.pack("<%dH" % (W * H), *[v for row in out for v in row]))
