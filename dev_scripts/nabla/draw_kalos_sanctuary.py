#!/usr/bin/env python3
"""Draws the NablaKalosSanctuary map (data/layouts/NablaKalosSanctuary/map.bin), a mirage of the Eon Flute.

The outer room of the Sealed Chamber (tilesets General and Cave), a hall of ruins: the way into its inner room is
wall, like on its sides, its tablets have no braille, and the dark water of its pool, which leads up to the sea in
Emerald, is plain water. Xerneas waits to the west of the pool, Yveltal to the east; the altar stands at the top of
the hall, Zygarde appears next to it; the Zygardite lies on the edge of the pool. The player arrives above the pool.

Running it again overwrites the map, including changes made in Porymap since.
Usage (from the repo root): python3 dev_scripts/nabla/draw_kalos_sanctuary.py
"""
import struct

import reach

W, H = 21, 23
LEGENDARIES = {"XERNEAS": (5, 18), "YVELTAL": (15, 18)}
ALTAR, ZYGARDE = (10, 3), (12, 3)
ITEMS = {"ZYGARDITE": (13, 19)}
ARRIVAL = (10, 16)
BRAILLE, TABLET = 0x235, 0x219                     # the front of a tablet, with and without braille
DIVE, WATER = 0x147, 0x156                         # the dark water of the pool, and the water around it

src = open("data/layouts/SealedChamber_OuterRoom/map.bin", "rb").read()
src = [[struct.unpack_from("<H", src, 2 * (y * W + x))[0] for x in range(W)] for y in range(H)]
out = [row[:] for row in src]
# The way into the inner room, with its frame: wall, like on its sides
for y in (1, 2):
    for x in range(8, 13):
        out[y][x] = src[y][7]
for y in range(H):
    for x in range(W):
        if out[y][x] & 0x3FF == BRAILLE:
            out[y][x] = out[y][x] & ~0x3FF | TABLET
        elif out[y][x] & 0x3FF == DIVE:
            out[y][x] = out[y][x] & ~0x3FF | WATER

# Every cell is reached without the objects and with them, and they can be reached on foot
OBJECTS = {ALTAR, ZYGARDE, *LEGENDARIES.values(), *ITEMS.values()}
cells, talked = reach.reach(out, ARRIVAL, OBJECTS)
alone, _ = reach.reach(out, ARRIVAL)
free = {(x, y) for y in range(H) for x in range(W) if not reach.blocked(out[y][x]) and reach.elevation(out[y][x]) == 3}
assert free <= alone and alone - cells <= OBJECTS, (free - alone, alone - cells)
assert talked == OBJECTS, OBJECTS - talked
open("data/layouts/NablaKalosSanctuary/map.bin", "wb").write(struct.pack("<%dH" % (W * H), *[v for row in out for v in row]))
