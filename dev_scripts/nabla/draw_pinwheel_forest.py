#!/usr/bin/env python3
"""Draws the NablaPinwheelForest map (data/layouts/NablaPinwheelForest/map.bin), a mirage of the Eon Flute.

Petalburg Woods (tilesets General and Rustboro), closed: its three exits (a gate and its path out of the woods) are
trees, which follow the rules of the forest trees (draw_emerald_forest.py: a top, rows in turn, side pieces next to
the grass), and its two signs are grass (the cuttable trees are objects of Petalburg Woods: they are not here).
Cobalion, Terrakion and Virizion wait in three corners of the woods; in the clearing to the north, where the north
exit was, stands the altar of Keldeo, which appears behind it.

Running it again overwrites the map, including changes made in Porymap since.
Usage (from the repo root): python3 dev_scripts/nabla/draw_pinwheel_forest.py
"""
import collections
import struct

import reach

W, H = 48, 44
LEGENDARIES = {"COBALION": (44, 22), "TERRAKION": (6, 30), "VIRIZION": (41, 12)}
ALTAR, KELDEO = (14, 7), (14, 6)
ARRIVAL = (16, 36)

src = open("data/layouts/PetalburgWoods/map.bin", "rb").read()
src = [[struct.unpack_from("<H", src, 2 * (y * W + x))[0] for x in range(W)] for y in range(H)]
# Each metatile with the collision and elevation it has in Petalburg Woods (its tree tops cannot be walked on)
values = collections.defaultdict(collections.Counter)
for row in src:
    for v in row:
        values[v & 0x3FF][v] += 1
tree = lambda m: values[m].most_common(1)[0][0]
GRASS = tree(0x001)

out = [row[:] for row in src]
# The north exit: its path between the trees (columns 14-15) becomes trees, rows in turn down to their foot (row 4),
# and its gate (row 5) grass; the trees at its sides lose their side pieces
for y in range(5):
    out[y][14], out[y][15] = (tree(0x1e4), tree(0x1e5)) if y == 4 else \
        (tree(0x1dc), tree(0x1dd)) if y % 2 == 0 else (tree(0x1d4), tree(0x1d5))
out[4][13], out[4][16] = tree(0x1e5), tree(0x1e4)
for x in range(12, 18):
    out[5][x] = GRASS
# The two south exits: their gate (row 38) becomes grass and their path (rows 39-43) trees, from a top (row 39)
# down to the edge of the map; the trees at their sides lose their side pieces
for gate in (16, 36):
    for x in range(gate - 2, gate + 4):
        out[38][x] = GRASS
    out[39][gate], out[39][gate + 1] = src[39][gate - 2], src[39][gate - 1]   # tops, like their neighbours
    for y in range(40, H):
        left, right = (0x1d4, 0x1d5) if y % 2 == 0 else (0x1dc, 0x1dd)
        out[y][gate], out[y][gate + 1] = tree(left), tree(right)
    out[40][gate - 1], out[40][gate + 2] = tree(0x1d5), tree(0x1d4)
# The signs: grass
for x, y in [(11, 8), (14, 32)]:
    out[y][x] = GRASS

# Every cell reached without the Pokémon and the altar is reached with them, and they can be reached on foot
OBJECTS = {ALTAR, KELDEO, *LEGENDARIES.values()}
jumps = reach.ledges(out, "gTileset_General", "gTileset_Rustboro")
cells, talked = reach.reach(out, ARRIVAL, OBJECTS, jumps)
alone, _ = reach.reach(out, ARRIVAL, (), jumps)
assert alone - cells <= OBJECTS, alone - cells
assert talked == OBJECTS, OBJECTS - talked
open("data/layouts/NablaPinwheelForest/map.bin", "wb").write(struct.pack("<%dH" % (W * H), *[v for row in out for v in row]))
