#!/usr/bin/env python3
"""Draws the NablaBurnedTower map (data/layouts/NablaBurnedTower/map.bin), a mirage of the Eon Flute.

The hall of Mt. Pyre's first floor (tilesets General and Facility), with its graves, without the stairs to the upper
floor and the two exits. The player arrives in the corridor to the south; Raikou waits at the end of the wing to the
west, Entei in front of the wall where the stairs were, Suicune to the east.

Running it again overwrites the map, including changes made in Porymap since.
Usage (from the repo root): python3 dev_scripts/nabla/draw_burned_tower.py
"""
import struct

import reach

W, H = 22, 19
LEGENDARIES = {"RAIKOU": (4, 5), "ENTEI": (11, 3), "SUICUNE": (20, 9)}
ARRIVAL = (17, 16)

src = open("data/layouts/MtPyre_1F/map.bin", "rb").read()
src = [[struct.unpack_from("<H", src, 2 * (y * W + x))[0] for x in range(W)] for y in range(H)]
WALL_TOP, WALL_BOTTOM = src[0][9], src[1][9]       # 0x2ef, 0x2f7
FLOOR, FLOOR_BY_WALL = src[6][5], src[2][9]        # 0x2e6, 0x2e7 (shadow of the wall)

out = [row[:] for row in src]
# The stairs to the upper floor: wall, and the floor at their sides
out[0][10:13] = [WALL_TOP] * 3
out[1][10:13] = [WALL_BOTTOM] * 3
out[2][10] = out[2][12] = FLOOR_BY_WALL
# The exits to the west and to the south: floor
out[6][3] = out[6][4] = FLOOR
out[18][17], out[18][18] = src[17][17], src[17][18]

# Every cell reached without the legendaries is reached with them, and they can be reached on foot
cells, talked = reach.reach(out, ARRIVAL, LEGENDARIES.values())
alone, _ = reach.reach(out, ARRIVAL)
assert alone - cells <= set(LEGENDARIES.values()), alone - cells
assert talked == set(LEGENDARIES.values()), set(LEGENDARIES.values()) - talked
for x, y in [ARRIVAL, *LEGENDARIES.values()]:
    assert out[y][x] & 0x3FF in (FLOOR & 0x3FF, FLOOR_BY_WALL & 0x3FF), (x, y)
open("data/layouts/NablaBurnedTower/map.bin", "wb").write(struct.pack("<%dH" % (W * H), *[v for row in out for v in row]))
