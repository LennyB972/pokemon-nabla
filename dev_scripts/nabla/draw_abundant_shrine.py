#!/usr/bin/env python3
"""Draws the NablaAbundantShrine map (data/layouts/NablaAbundantShrine/map.bin), a mirage of the Eon Flute.

The summit of Mt. Pyre (tilesets General and Facility), without its graves (grass) and its stairs down (its ridge
goes on; the path below them is grass). Its shrine of the orbs, at the top, is the altar: Landorus and Enamorus
appear in front of it. Tornadus and Thundurus wait in the maze, to the west and to the east. As on Mt. Pyre, the
lanes along the slopes and the foot of the summit are seen but not reached.

Running it again overwrites the map, including changes made in Porymap since.
Usage (from the repo root): python3 dev_scripts/nabla/draw_abundant_shrine.py
"""
import struct

import reach

W, H = 50, 37
LEGENDARIES = {"TORNADUS": (10, 22), "THUNDURUS": (36, 23)}
HIDDEN = {"LANDORUS": (21, 5), "ENAMORUS": (25, 5)}
ALTAR = (23, 4)                                    # the bottom of the shrine, read from below
ARRIVAL = (23, 29)
GRAVES = (0x324, 0x325, 0x326)

src = open("data/layouts/MtPyre_Summit/map.bin", "rb").read()
src = [[struct.unpack_from("<H", src, 2 * (y * W + x))[0] for x in range(W)] for y in range(H)]
GRASS, RIDGE = src[2][19], src[31][17]             # 0x001, 0x079

out = [row[:] for row in src]
for y in range(H):
    for x in range(W):
        if out[y][x] & 0x3FF in GRAVES:
            out[y][x] = GRASS
# The stairs down: the ridge goes on; the path down the mountain below them: grass
for x in (22, 23, 24):
    out[31][x] = RIDGE
for y in range(32, H):
    for x in range(21, 26):
        out[y][x] = GRASS

# Every cell reached without the Pokémon is reached with them, they can be reached on foot, and so can the altar
OBJECTS = {*LEGENDARIES.values(), *HIDDEN.values()}
cells, talked = reach.reach(out, ARRIVAL, OBJECTS)
alone, _ = reach.reach(out, ARRIVAL)
assert alone - cells <= OBJECTS, alone - cells
assert talked == OBJECTS, OBJECTS - talked
assert (ALTAR[0], ALTAR[1] + 1) in cells and reach.blocked(out[ALTAR[1]][ALTAR[0]])
assert all(0 < x < W - 1 and 0 < y < H - 1 for x, y in alone), "reaches the edge of the map"
open("data/layouts/NablaAbundantShrine/map.bin", "wb").write(struct.pack("<%dH" % (W * H), *[v for row in out for v in row]))
