#!/usr/bin/env python3
"""Draws the NablaDiamondMine map (data/layouts/NablaDiamondMine/map.bin), a mirage of the Eon Flute.

The lower part of the deepest floor of Granite Cave (tilesets General and Cave), the part the player walks without
ladders: its rooms above, which Emerald reaches by the floor above, are left out (the map starts on the top of the
wall that closes them), and its ladders are floor. Hoopa waits on the mound in the middle, Diancie in the sand pit,
in front of the rock; the Diancite lies in the corner to the south-west. The player arrives where the ladder to the
east was.

Running it again overwrites the map, including changes made in Porymap since.
Usage (from the repo root): python3 dev_scripts/nabla/draw_diamond_mine.py
"""
import struct

import reach

SRC_W, SRC_H, TOP = 32, 26, 8                      # Granite Cave B2F, and its first row kept
W, H = SRC_W, SRC_H - TOP
LEGENDARIES = {"DIANCIE": (21, 10), "HOOPA": (17, 4)}
ITEMS = {"DIANCITE": (3, 13)}
ARRIVAL = (29, 5)
LADDERS = {(29, 5): (28, 5), (28, 13): (27, 13)}   # each ladder, and the floor next to it

src = open("data/layouts/GraniteCave_B2F/map.bin", "rb").read()
src = [[struct.unpack_from("<H", src, 2 * (y * SRC_W + x))[0] for x in range(SRC_W)] for y in range(TOP, SRC_H)]
out = [row[:] for row in src]
for (x, y), (fx, fy) in LADDERS.items():
    out[y][x] = src[fy][fx]

# Every cell is reached without the objects and with them, and they can be reached on foot
OBJECTS = {*LEGENDARIES.values(), *ITEMS.values()}
jumps = reach.ledges(out, "gTileset_General", "gTileset_Cave")
cells, talked = reach.reach(out, ARRIVAL, OBJECTS, jumps)
alone, _ = reach.reach(out, ARRIVAL, (), jumps)
free = {(x, y) for y in range(H) for x in range(W) if not reach.blocked(out[y][x])}
assert free <= alone and alone - cells <= OBJECTS, (free - alone, alone - cells)
assert talked == OBJECTS, OBJECTS - talked
open("data/layouts/NablaDiamondMine/map.bin", "wb").write(struct.pack("<%dH" % (W * H), *[v for row in out for v in row]))
