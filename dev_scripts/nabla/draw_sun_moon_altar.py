#!/usr/bin/env python3
"""Draws the NablaSunMoonAltar map (data/layouts/NablaSunMoonAltar/map.bin), a mirage of the Eon Flute.

The inner room of the Sealed Chamber (tilesets General and Cave), a hall of pillars: the bases of its pillars and of
the relief at the top have no braille, and its way out at the bottom is wall, like on its sides. Cosmog and Type: Null
wait in the hall (they come with the player); the altar stands in front of the relief, Necrozma appears next to it.
The player arrives at the bottom of the hall.

Running it again overwrites the map, including changes made in Porymap since.
Usage (from the repo root): python3 dev_scripts/nabla/draw_sun_moon_altar.py
"""
import struct

import reach

W, H = 21, 23
GIFTS = {"COSMOG": (10, 11), "TYPE_NULL": (17, 9)}
ALTAR, NECROZMA = (10, 5), (12, 5)
ARRIVAL = (10, 18)
BRAILLE, BASE = 0x237, 0x2f9                       # the base of a pillar, with and without braille
WAY_OUT = [(9, 20), (10, 20), (11, 20)]

src = open("data/layouts/SealedChamber_InnerRoom/map.bin", "rb").read()
src = [[struct.unpack_from("<H", src, 2 * (y * W + x))[0] for x in range(W)] for y in range(H)]
out = [row[:] for row in src]
for y in range(H):
    for x in range(W):
        if out[y][x] & 0x3FF == BRAILLE:
            out[y][x] = out[y][x] & ~0x3FF | BASE
# The way out: wall, like on its sides; the hole in front of it: floor
for x, y in WAY_OUT:
    out[y][x] = src[y][8]
out[19][10] = src[19][9]

# Every cell is reached without the objects and with them, and they can be reached on foot
OBJECTS = {ALTAR, NECROZMA, *GIFTS.values()}
cells, talked = reach.reach(out, ARRIVAL, OBJECTS)
alone, _ = reach.reach(out, ARRIVAL)
free = {(x, y) for y in range(H) for x in range(W) if not reach.blocked(out[y][x])}
assert free <= alone and alone - cells <= OBJECTS, (free - alone, alone - cells)
assert talked == OBJECTS, OBJECTS - talked
open("data/layouts/NablaSunMoonAltar/map.bin", "wb").write(struct.pack("<%dH" % (W * H), *[v for row in out for v in row]))
