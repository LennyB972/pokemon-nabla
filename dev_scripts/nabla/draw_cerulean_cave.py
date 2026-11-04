#!/usr/bin/env python3
"""Draws the NablaCeruleanCave map (data/layouts/NablaCeruleanCave/map.bin), a mirage of the Eon Flute.

A cave taken from Meteor Falls' lower floor (tilesets General and MeteorFalls): its lake with a peninsula in the
middle, without the ladders, the entrance of the cave to the north and the exit to the south.
Mewtwo waits on the peninsula, in front of its rock; its two Mega Stones lie on the plateau and on a platform. The player arrives
on the plateau, to the south-west, and walks to them; from the shore at the left of the lake, they can surf to the
shores of the north and of the south.

Running it again overwrites the map, including changes made in Porymap since.
Usage (from the repo root): python3 dev_scripts/nabla/draw_cerulean_cave.py
"""
import struct

import reach

W, H = 29, 38
MEWTWO = (17, 16)
ITEMS = {"MEWTWONITE_X": (7, 7), "MEWTWONITE_Y": (3, 22)}  # on the plateau, on the platform at the bottom
ARRIVAL = (12, 23)

src = open("data/layouts/MeteorFalls_B1F_1R/map.bin", "rb").read()
src = [[struct.unpack_from("<H", src, 2 * (y * W + x))[0] for x in range(W)] for y in range(H)]
WALL, BOTTOM_WALL, BOX_FACE = src[2][13], src[37][16], src[14][17]  # 0x244, 0x286, 0x219
floor = lambda e: src[16][7] & 0x3FF | e << 12                     # 0x201, no collision

out = [row[:] for row in src]
# The entrance of the cave to the north: wall
for x in (16, 17, 18):
    out[2][x] = out[3][x] = WALL
# The exit to the south: wall, and its mat: floor
out[37][19:22] = [BOTTOM_WALL] * 3
out[36][20] = floor(3)
# The ladders: floor (and the face of the rock of the peninsula)
out[5][5], out[6][5] = src[5][4], floor(4)
out[10][7] = out[11][7] = floor(5)
out[22][3] = out[23][3] = floor(5)
out[14][18], out[15][18] = BOX_FACE, floor(4)
# The floor left out of the walls, at the left edge: wall
for y in range(28, H):
    out[y][0] = src[28][1]
# Two cells of floor closed by rocks: blocked, so that the check below holds
for x, y in [(9, 8), (16, 36)]:
    out[y][x] |= 1 << 10
# The shore at the left of the lake is lower than the plateau: a step between them (elevation 0 lets the player
# walk from one to the other, like the stairs)
for x in (7, 8, 9):
    out[19][x] &= 0x0FFF


# Every cell without collision can be reached from the arrival, walking or surfing, without going through Mewtwo and
# the Mega Stones, which can be reached on foot
OBJECTS = {MEWTWO, *ITEMS.values()}
cells, talked = reach.reach(out, ARRIVAL, OBJECTS)
missed = [(x, y) for y in range(H) for x in range(W) if not reach.blocked(out[y][x]) and (x, y) not in cells | OBJECTS]
assert not missed, missed
assert talked == OBJECTS, OBJECTS - talked
assert out[MEWTWO[1]][MEWTWO[0]] == floor(4)
assert out[ARRIVAL[1]][ARRIVAL[0]] == floor(4)
open("data/layouts/NablaCeruleanCave/map.bin", "wb").write(struct.pack("<%dH" % (W * H), *[v for row in out for v in row]))
