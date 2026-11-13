#!/usr/bin/env python3
"""Draws the NablaAreaZero map (data/layouts/NablaAreaZero/map.bin), a mirage of the Eon Flute.

The end of the Marine Cave (tilesets General and Cave), the bottom of a crater with a lake: its way out is wall, like
at its side, and its hole is floor; the water of the lake, where Kyogre sleeps and which can't be crossed in Emerald,
is surfed (its rocky rims still block). Koraidon waits in the middle room, Miraidon by the lake; the altar stands on
the shore, and Terapagos appears in the lake, where Kyogre was (the player surfs to it). The player arrives at the
top, where the way out was.

Running it again overwrites the map, including changes made in Porymap since.
Usage (from the repo root): python3 dev_scripts/nabla/draw_area_zero.py
"""
import struct

import reach

W, H = 27, 30
LEGENDARIES = {"KORAIDON": (10, 11), "MIRAIDON": (20, 21)}
ALTAR, TERAPAGOS = (9, 26), (9, 22)
ARRIVAL = (20, 3)
WATER = (0x14e, 0x14f, 0x170)                      # the lake, deep and shallow, without its rims

src = open("data/layouts/MarineCave_End/map.bin", "rb").read()
src = [[struct.unpack_from("<H", src, 2 * (y * W + x))[0] for x in range(W)] for y in range(H)]
out = [row[:] for row in src]
for x in (19, 20, 21):                             # the way out: wall
    out[5][x] = src[5][18]
out[4][20] = src[4][19]                            # its hole: floor
for y in range(H):
    for x in range(W):
        if out[y][x] & 0x3FF in WATER:
            out[y][x] &= ~(3 << 10)

# Every cell reached without the objects is reached with them, and they can be reached, Terapagos surfing (the cave
# to the east is seen, not reached, like in Emerald)
OBJECTS = {ALTAR, TERAPAGOS, *LEGENDARIES.values()}
cells, talked = reach.reach(out, ARRIVAL, OBJECTS)
alone, _ = reach.reach(out, ARRIVAL)
assert alone - cells <= OBJECTS, alone - cells
assert talked == OBJECTS, OBJECTS - talked
assert reach.elevation(out[TERAPAGOS[1]][TERAPAGOS[0]]) == 1, "Terapagos is in the water"
open("data/layouts/NablaAreaZero/map.bin", "wb").write(struct.pack("<%dH" % (W * H), *[v for row in out for v in row]))
