#!/usr/bin/env python3
"""Draws the NablaPowerPlant map (data/layouts/NablaPowerPlant/map.bin), a mirage of the Eon Flute.

New Mauville's inside (tilesets General and BikeShop), an abandoned power plant: its electric barriers, which buttons
on the floor turn on and off in Emerald (data/maps/NewMauville_Inside/scripts.inc), are all off (the open state of
those scripts), the buttons are floor, and its door is wall (blocks found so that each pair of neighbours occurs in
Emerald's maps). The player arrives in front of the old door. Genesect waits to the west, Magearna in the middle,
Meltan in the room to the south (it comes with the player); the altar stands in front of the generator, Melmetal
appears next to it; the Magearnite lies to the east.

Running it again overwrites the map, including changes made in Porymap since.
Usage (from the repo root): python3 dev_scripts/nabla/draw_new_mauville.py
"""
import struct

import reach

W, H = 41, 41
LEGENDARIES = {"GENESECT": (2, 7), "MAGEARNA": (16, 16), "MELTAN": (17, 38)}
ALTAR, MELMETAL = (33, 6), (35, 7)
ITEMS = {"MAGEARNITE": (38, 24)}
ARRIVAL = (32, 34)
BARRIERS = [(10, 0), (10, 16), (10, 24), (21, 2), (23, 34), (28, 22), (37, 33)]   # the top of each barrier
BUTTONS = [(30, 38), (18, 36), (4, 26), (16, 22), (25, 18), (2, 11), (6, 11), (13, 10), (17, 10), (33, 6)]
# METATILE_BikeShop_*: Barrier_Hidden_Top, Barrier_Hidden_Bottom (in the wall), Floor_Shadow_Top, Wall_Edge_Top
BARRIER_OFF = (0x269 | 1 << 10, 0x271 | 1 << 10, 0x26d, 0x281)
FLOOR = 0x210                                      # under the buttons
DOOR = {(31, 32): 0x21f, (32, 32): 0x21f, (33, 32): 0x21f, (31, 33): 0x227, (32, 33): 0x227, (33, 33): 0x227}

src = open("data/layouts/NewMauville_Inside/map.bin", "rb").read()
src = [[struct.unpack_from("<H", src, 2 * (y * W + x))[0] for x in range(W)] for y in range(H)]
out = [row[:] for row in src]
level = lambda v: v & ~0xFFF                       # the elevation of a block
for x, y in BARRIERS:
    for i, metatile in enumerate(BARRIER_OFF):
        out[y + i][x] = level(src[y + 2][x - 1]) | metatile
for x, y in BUTTONS:
    out[y][x] = level(src[y][x]) | FLOOR
for (x, y), metatile in DOOR.items():
    out[y][x] = level(src[y][x]) | 1 << 10 | metatile

# Every cell is reached without the objects and with them, and they can be reached on foot
OBJECTS = {ALTAR, MELMETAL, *LEGENDARIES.values(), *ITEMS.values()}
cells, talked = reach.reach(out, ARRIVAL, OBJECTS)
alone, _ = reach.reach(out, ARRIVAL)
free = {(x, y) for y in range(H) for x in range(W) if not reach.blocked(out[y][x])}
assert free <= alone and alone - cells <= OBJECTS, (free - alone, alone - cells)
assert talked == OBJECTS, OBJECTS - talked
open("data/layouts/NablaPowerPlant/map.bin", "wb").write(struct.pack("<%dH" % (W * H), *[v for row in out for v in row]))
