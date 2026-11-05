#!/usr/bin/env python3
"""Draws the NablaDragonspiral map (data/layouts/NablaDragonspiral/map.bin), a mirage of the Eon Flute.

The plateau around the Sky Pillar (tilesets General and Pacifidlog), seen from outside: the tower is the Dragonspiral
Tower. The ways into the cave of its mound and into the cliff below are rock, like around them. In Emerald, the
shadow of the tower on the sand to the east blocks the player (invisible walls): it can be walked, like on the west of
the shadow; a rock opens the nook of sand to the north-west. Reshiram waits to the west of the tower, Zekrom to the east; the altar
stands before the door of the tower, and Kyurem appears next to it. The player arrives below the mound.

Running it again overwrites the map, including changes made in Porymap since.
Usage (from the repo root): python3 dev_scripts/nabla/draw_dragonspiral.py
"""
import struct

import reach

W, H = 28, 23
LEGENDARIES = {"RESHIRAM": (9, 8), "ZEKROM": (21, 4)}
ALTAR, KYUREM = (14, 6), (16, 7)
ARRIVAL = (15, 15)
SHADOW = (0x2a6, 0x2b9, 0x2ba, 0x2bb, 0x2bc)       # the shadow of the tower on the sand

src = open("data/layouts/SkyPillar_Outside/map.bin", "rb").read()
src = [[struct.unpack_from("<H", src, 2 * (y * W + x))[0] for x in range(W)] for y in range(H)]
out = [row[:] for row in src]
# The way into the cave of the mound, and the one at the foot of the cliff below the plateau: rock, like at their side
out[12][17], out[13][17] = src[12][16], src[13][16]
out[19][15], out[20][15] = src[19][14], src[20][14]
# The shadow of the tower on the sand: walked on everywhere (sand of elevation 3)
for y in range(1, 10):
    for x in range(17, 24):
        if out[y][x] & 0x3FF in SHADOW:
            out[y][x] = out[y][x] & 0x3FF | 3 << 12
# The rock that closes the nook of sand to the north-west: sand
out[5][11] = src[4][11]

# Every cell reached without the Pokémon and the altar is reached with them, and they can be reached on foot
OBJECTS = {ALTAR, KYUREM, *LEGENDARIES.values()}
cells, talked = reach.reach(out, ARRIVAL, OBJECTS)
alone, _ = reach.reach(out, ARRIVAL)
assert alone - cells <= OBJECTS, alone - cells
assert talked == OBJECTS, OBJECTS - talked
assert all(0 < x < W - 1 and 0 < y < H - 1 for x, y in alone), "reaches the edge of the map"
open("data/layouts/NablaDragonspiral/map.bin", "wb").write(struct.pack("<%dH" % (W * H), *[v for row in out for v in row]))
