#!/usr/bin/env python3
"""Draws the NablaStarkMountain map (data/layouts/NablaStarkMountain/map.bin), a mirage of the Eon Flute.

The summit of Mt. Chimney (tilesets General and Lavaridge), down to the edge of its plateau: the crater of lava, the
plateau below it and the two ledges at its sides, without the machine of Team Magma by the lava; the two ways down
from the plateau are closed by its edge. The player arrives on the plateau. Heatran waits at the tip of the ledge to
the west, by the lava, Volcanion on the ledge to the east; the Heatranite lies at the west of the plateau.

Running it again overwrites the map, including changes made in Porymap since.
Usage (from the repo root): python3 dev_scripts/nabla/draw_stark_mountain.py
"""
import struct

import reach

W, H = 40, 23                       # Mt. Chimney's map, down to the edge of the plateau
SRC_H = 47
LEGENDARIES = {"HEATRAN": (14, 6), "VOLCANION": (31, 6)}
ITEMS = {"HEATRANITE": (10, 16)}
ARRIVAL = (21, 19)

src = open("data/layouts/MtChimney/map.bin", "rb").read()
src = [[struct.unpack_from("<H", src, 2 * (y * W + x))[0] for x in range(W)] for y in range(SRC_H)]
EDGE = src[22][20]                  # 0x274, the edge of the plateau
LAVA_SIDE = src[4][14]              # 0x31c, the west side of the lava

out = [row[:] for row in src[:H]]
# The machine of Team Magma, at the tip of the ledge that goes into the lava: the side of the lava above it, like
# higher, and the ledge going on to its tip (no block of Emerald joins these neighbours: the machine is the only one,
# but these join well to the eye)
out[5][14], out[6][14] = LAVA_SIDE, src[6][13]
# The ways down from the plateau (a path and stairs): its edge, in one piece
for x in range(16, 20):
    out[22][x] = EDGE
out[22][25] = EDGE

# Every cell reached without the Pokémon and the items is reached with them, and they can be reached on foot
OBJECTS = {*LEGENDARIES.values(), *ITEMS.values()}
cells, talked = reach.reach(out, ARRIVAL, OBJECTS)
alone, _ = reach.reach(out, ARRIVAL)
assert alone - cells <= OBJECTS, alone - cells
assert talked == OBJECTS, OBJECTS - talked
assert all(0 < x < W - 1 and 0 < y < H - 1 for x, y in alone), "reaches the edge of the map"
open("data/layouts/NablaStarkMountain/map.bin", "wb").write(struct.pack("<%dH" % (W * H), *[v for row in out for v in row]))
