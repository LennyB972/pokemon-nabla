#!/usr/bin/env python3
"""Draws the NablaMoonIsland map (data/layouts/NablaMoonIsland/map.bin), a mirage of the Eon Flute.

An island above the sea shaped like a crescent moon lying on its back, horns up, built with the pieces of
Birth Island (tilesets General and Dewford): a tree on the summit of each horn, slopes in diagonal down to the
sea, a bay in V between the horns, straight cliff sides, and the cliff of Birth Island to the south. Cresselia
waits at the foot of the bay by day, Darkrai at night. The sea cannot be crossed.

Running it again overwrites the map, including changes made in Porymap since.
Usage (from the repo root): python3 dev_scripts/nabla/draw_moon_island.py
"""
import struct

W, H = 32, 24
LEFT_HORN, RIGHT_HORN = 5, 26  # columns of the summits (row 4); the bay closes on row 13
MOON = (15, 14)    # Cresselia and Darkrai
ARRIVAL = (15, 16)

# Block values (metatile + collision + elevation) as they are on Birth Island
birth = open("data/layouts/BirthIsland_Exterior/map.bin", "rb").read()
value = {}
for v in struct.unpack("<%dH" % (len(birth) // 2), birth):
    value.setdefault(v & 0x3FF, v)


def b(mt):
    return value[mt]


SEA = b(0x170)
out = [[SEA] * W for _ in range(H)]


def put(x, y, *mts):
    for i, mt in enumerate(mts):
        out[y][x + i] = b(mt)


# The summits: a tree, then the slopes start on both sides
for a in (LEFT_HORN, RIGHT_HORN):
    put(a - 1, 4, 0x328, 0x329, 0x32a)
    put(a - 2, 5, 0x378, 0x330, 0x331, 0x332, 0x37a)
    put(a - 3, 6, 0x378, 0x073, 0x338, 0x339, 0x33a, 0x075, 0x37a)

# Below the summits: straight cliff sides outside, slopes in diagonal on the side of the bay
for y in range(7, 17):
    put(1, y, 0x192, 0x073, 0x073)                             # west side
    put(W - 4, y, 0x075, 0x075, 0x190)                         # east side
    bay_left, bay_right = y + 2, (W - 3) - y                   # slopes on the bay, row by row
    for x in range(4, W - 4):
        out[y][x] = b(0x001)
    if bay_left < bay_right:
        for x in range(bay_left + 1, bay_right):
            out[y][x] = SEA
        out[y][bay_left] = b(0x37a)
        out[y][bay_right] = b(0x378)
        out[y][bay_left - 1] = b(0x075 if y % 2 else 0x002)
        out[y][bay_right + 1] = b(0x073 if y % 2 else 0x002)
assert (W - 3) - 13 == 13 + 3  # the two slopes of the bay meet side by side on row 13

# Two trees on the grass, between the cliff sides and the bay
for x0 in (7, W - 11):
    for j, row in enumerate([(0x32b, 0x32c, 0x32d, 0x340), (0x333, 0x334, 0x335, 0x348), (0x33b, 0x33c, 0x33d, 0x350)]):
        put(x0, 14 + j, *row)

# The cliff to the south (Birth Island's, two columns wider, without its stairs), and the sea at its foot
put(1, 17, 0x192, 0x073, 0x073, 0x07b, *[0x07c] * (W - 10), 0x07d, 0x075, 0x075, 0x190)
put(1, 18, 0x192, 0x073, 0x07b, *[0x07c] * (W - 8), 0x07d, 0x075, 0x190)
put(1, 19, 0x192, 0x07b, *[0x07c] * (W - 6), 0x07d, 0x190)
put(1, 20, 0x19a, *[0x189] * (W - 4), 0x198)

for x, y in (MOON, ARRIVAL):
    assert out[y][x] == b(0x001), (x, y)
open("data/layouts/NablaMoonIsland/map.bin", "wb").write(struct.pack("<%dH" % (W * H), *[v for row in out for v in row]))
