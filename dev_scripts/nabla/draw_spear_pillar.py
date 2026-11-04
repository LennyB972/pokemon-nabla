#!/usr/bin/env python3
"""Draws the NablaSpearPillar map (data/layouts/NablaSpearPillar/map.bin), a mirage of the Eon Flute.

The roof of the Sky Pillar (tilesets General and Pacifidlog), with its rubble, in the sky. Its cracked floor and
its holes are plain floor (there is no floor below to fall to), the door to the floor below is wall, and the sky
above the roof is blocked. The rubble that closed the middle of the roof (the way to Rayquaza) is opened in a few
places, so that the whole roof and the ledge below it can be walked; single cells closed by rubble are blocked.
The player arrives on the ledge and goes up by the stairs. Dialga waits on the west of the roof, Palkia on the
east, Giratina at the end of the ledge; the altar stands in the middle of the roof, and Arceus appears behind it.

Running it again overwrites the map, including changes made in Porymap since.
Usage (from the repo root): python3 dev_scripts/nabla/draw_spear_pillar.py
"""
import struct

import reach

W, H = 27, 24
LEGENDARIES = {"DIALGA": (4, 7), "PALKIA": (20, 7), "GIRATINA": (26, 16)}
ALTAR, ARCEUS = (14, 5), (14, 4)
ARRIVAL = (12, 16)
# Rubble opened: between the middle of the roof and its west, its east, the north-west of the middle, the two
# cells next to Arceus, and along the ledge
OPENED = [(8, 12), (20, 12), (10, 6), (13, 4), (15, 4), (6, 16), (17, 16), (20, 17), (22, 17)]

src = open("data/layouts/SkyPillar_Top/map.bin", "rb").read()
src = [[struct.unpack_from("<H", src, 2 * (y * W + x))[0] for x in range(W)] for y in range(H)]
mt = lambda v: v & 0x3FF
FLOOR = src[5][2]                                  # 0x234
RUBBLE = (0x20f, 0x21f, 0x217)

out = [row[:] for row in src]
for y in range(H):
    for x in range(W):
        if mt(out[y][x]) in (0x236, 0x237):        # cracked floor, hole
            out[y][x] = FLOOR
        if y <= 3:                                 # the sky and the rim of the roof
            out[y][x] |= 1 << 10
# The door to the floor below: wall
for x in (15, 16, 17):
    out[13][x], out[14][x] = src[13][14], src[14][14]
for x, y in OPENED:
    assert mt(out[y][x]) in RUBBLE, (x, y)
    out[y][x] = FLOOR
# Single cells closed by rubble: blocked
cells, _ = reach.reach(out, ARRIVAL)
for y in range(H):
    for x in range(W):
        if not reach.blocked(out[y][x]) and (x, y) not in cells:
            out[y][x] |= 1 << 10

# Every cell reached without the Pokémon and the altar is reached with them, and they can be reached on foot
OBJECTS = {ALTAR, ARCEUS, *LEGENDARIES.values()}
cells, talked = reach.reach(out, ARRIVAL, OBJECTS)
alone, _ = reach.reach(out, ARRIVAL)
assert alone - cells <= OBJECTS, alone - cells
assert talked == OBJECTS, OBJECTS - talked
for x, y in OBJECTS | {ARRIVAL}:
    assert out[y][x] == FLOOR or mt(out[y][x]) == 0x234, (x, y)
open("data/layouts/NablaSpearPillar/map.bin", "wb").write(struct.pack("<%dH" % (W * H), *[v for row in out for v in row]))
