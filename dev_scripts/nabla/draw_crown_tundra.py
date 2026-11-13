#!/usr/bin/env python3
"""Draws the NablaCrownTundra map (data/layouts/NablaCrownTundra/map.bin), a mirage of the Eon Flute.

The ice room of Shoal Cave at low tide (tilesets General and Cave), without its sliding: its ice (MB_ICE), the edges
of the ice and the marks on it are the speckled ice floor of the room, so that every cell is walked, and its ladder
is floor (its top, in the wall, is wall). Calyrex waits on the top of the plateau, Glastrier in the ice field to the
north-west, Spectrier in the passage to the east. The player arrives where the ladder was.

Running it again overwrites the map, including changes made in Porymap since.
Usage (from the repo root): python3 dev_scripts/nabla/draw_crown_tundra.py
"""
import struct

import reach

W, H = 20, 30
LEGENDARIES = {"CALYREX": (8, 8), "GLASTRIER": (5, 4), "SPECTRIER": (16, 22)}
ARRIVAL = (17, 10)
FLOOR = 0x385                                      # the speckled ice floor
SLIDING = (0x38d, 0x38c, 0x38e, 0x38f, 0x387)      # the ice, and its edges on the floor
MARK, LADDER, LADDER_TOP = 0x28f, 0x37f, 0x377    # the top of the ladder is in the wall

src = open("data/layouts/ShoalCave_LowTideIceRoom/map.bin", "rb").read()
src = [[struct.unpack_from("<H", src, 2 * (y * W + x))[0] for x in range(W)] for y in range(H)]
out = [row[:] for row in src]
for y in range(H):
    for x in range(W):
        if out[y][x] & 0x3FF in (*SLIDING, MARK, LADDER):
            out[y][x] = FLOOR | 3 << 12
        elif out[y][x] & 0x3FF == LADDER_TOP:
            out[y][x] = src[y][x - 1]                  # the wall on its left

# Every cell is reached without the objects and with them, and they can be reached on foot
OBJECTS = set(LEGENDARIES.values())
jumps = reach.ledges(out, "gTileset_General", "gTileset_Cave")
cells, talked = reach.reach(out, ARRIVAL, OBJECTS, jumps)
alone, _ = reach.reach(out, ARRIVAL, (), jumps)
free = {(x, y) for y in range(H) for x in range(W) if not reach.blocked(out[y][x])}
assert free <= alone and alone - cells <= OBJECTS, (free - alone, alone - cells)
assert talked == OBJECTS, OBJECTS - talked
open("data/layouts/NablaCrownTundra/map.bin", "wb").write(struct.pack("<%dH" % (W * H), *[v for row in out for v in row]))
