#!/usr/bin/env python3
"""Draws the NablaShrineOfRuin map (data/layouts/NablaShrineOfRuin/map.bin), a mirage of the Eon Flute.

The first floor of the Mirage Tower (tilesets General and MirageTower), a ring of sand around a mound: its ladder
and its way out are wall, like at their side, and the mat of its way out is sand. The four Treasures of Ruin wait at
the four corners of the ring, like their four shrines. The player arrives at the bottom of the ring.

Running it again overwrites the map, including changes made in Porymap since.
Usage (from the repo root): python3 dev_scripts/nabla/draw_shrine_of_ruin.py
"""
import struct

import reach

W, H = 21, 17
LEGENDARIES = {"WO_CHIEN": (4, 4), "CHIEN_PAO": (17, 5), "TING_LU": (3, 12), "CHI_YU": (16, 12)}
ARRIVAL = (10, 13)

src = open("data/layouts/MirageTower_1F/map.bin", "rb").read()
src = [[struct.unpack_from("<H", src, 2 * (y * W + x))[0] for x in range(W)] for y in range(H)]
out = [row[:] for row in src]
out[1][15] = src[1][14]                            # the ladder, in the wall
out[2][15] = src[2][14]                            # its foot
out[15][9], out[15][10] = src[15][8], src[15][11]  # the way out, in the wall
out[14][10] = src[14][9]                           # its mat

# Every cell is reached without the objects and with them, and they can be reached on foot (the top of the mound is
# seen, not reached, like in Emerald)
OBJECTS = set(LEGENDARIES.values())
cells, talked = reach.reach(out, ARRIVAL, OBJECTS)
alone, _ = reach.reach(out, ARRIVAL)
assert alone - cells <= OBJECTS, alone - cells
assert talked == OBJECTS, OBJECTS - talked
assert len(alone) == 110, len(alone)                # the whole ring
open("data/layouts/NablaShrineOfRuin/map.bin", "wb").write(struct.pack("<%dH" % (W * H), *[v for row in out for v in row]))
