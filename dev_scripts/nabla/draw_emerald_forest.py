#!/usr/bin/env python3
"""Draws the maps of the Emerald Forest and its opening on Route 123, from plans made of characters.

Each character of a plan stands for two columns of the map (trees are two cells wide):
  "#" trees of the forest (Petalburg Woods), "%" small trees (Route 123), "." grass, "T" tall grass.
Details are then put on single cells (flowers, rocks, ledges). The blocks are those of the General tileset,
each with the collision and elevation it has in Emerald's maps:
  - forest trees: a top 1ce 1cf, then rows 1d4 1d5 and 1dc 1dd in turn, and a foot 1e4 1e5; the row under
    the top and the foot have side pieces next to the grass (1d6 1d7, 1e6 1e7). A run of trees between two
    rows of grass is thus 3, 5, 7... rows tall;
  - small trees: a top e, rows c6 c7, a foot 16 (at least 2 rows between two rows of grass).
The script checks these rules, and that no cell the player can reach touches the edge of a map where there
is no connection (invisible wall).

Running it again overwrites the maps, including changes made in Porymap since.
Usage (from the repo root): python3 dev_scripts/nabla/draw_emerald_forest.py
"""
import collections
import json
import struct
import sys

# --- Plans (one character = two columns)

# The forest edge, under the opening of Route 123 (its columns 102-107 are columns 8-13 here)
ENTRANCE = [
    "%%%%...%%%%%",
    "%%%%...%%%%%",
    "%%%%..T.%%%%",
    "%%%TT.TT.%%%",
    "%%TTTT.TT.%%",
    "%%TTT..TT.%%",
    "%%%TT..%%T.%",
    "%%%T...%%TT%",
    "%%TT.%%%%TT%",
    "%%TT.%%%%.T%",
    "%%T..%%%..T%",
    "%%%...TT.TT%",
    "%%%%..TTT.T%",
    "%%%%..TT...%",
    "####......##",
    "####......##",
    "######..####",
    "######..####",
    "######..####",
    "######..####",
    "######..####",
    "######..####",
]
ENTRANCE_DETAILS = [("f", 15, 2), ("f", 17, 4), ("f", 9, 12), ("o", 13, 5), ("f", 16, 13), ("f", 9, 15)]

# The forest: a winding main path (clearing, west side, meadow, east side, down to the sanctuary), with a loop
# on the west side, a nook to the east of the first clearing and a pocket west of the east side
FOREST = [
    "##########..############",
    "##########..############",
    "##########..############",
    "########TT....##########",
    "######TTTT...TTT########",
    "#####TTTTT....TTT.######",
    "####TTTTT.#####TTT..####",
    "####TTTT..#####...TTT###",
    "###TTTT...#####...TTTT##",
    "###............TTTT.TT##",
    "##............TTTTT...##",
    "##.TT##############TTT##",
    "##TTT##############TTT##",
    "##TT.##############TTT##",
    "##....TTT..########.TT##",
    "##....TTT..########TTT##",
    "##...####..########.TT##",
    "##.TT####..#############",
    "##TTT####TT#############",
    "##TTT####TT#############",
    "##TT.####TT#############",
    "##TT.####TT#############",
    "##...####..#############",
    "##TTT####..#############",
    "##TTT####..#############",
    "##....TTTT.#############",
    "##TTTTT..........TTTT.##",
    "##TTTTTT....TTTTTTTTTT##",
    "##.TTTTT....TTTTTTTTTT##",
    "##.TTTT......TT..TTTT.##",
    "##..TT............TT..##",
    "##....................##",
    "################TTT#####",
    "################TTT#####",
    "################.TT#####",
    "################TT.#####",
    "################TTT#####",
    "#####..............#####",
    "#####.TTT.TTTT.....#####",
    "#####.TTT.TTTT.....#####",
    "#####.TT...TTT.#...#####",
    "#####......TT..#.TT#####",
    "################TTT#####",
    "################.TT#####",
    "################TT.#####",
    "################TT.#####",
    "################...#####",
    "####........TTTT...#####",
    "####.TTT...TTTTT...#####",
    "####.TTT....TTT....#####",
    "########...#############",
    "########...#############",
    "########...#############",
    "########...#############",
    "########...#############",
    "########...#############",
]
FOREST_DETAILS = [("L", 4, 9, 22), ("f", 28, 31), ("f", 29, 31), ("f", 26, 30), ("f", 31, 27), ("f", 12, 9),
                  ("f", 13, 4), ("f", 33, 5), ("f", 22, 38), ("o", 24, 27), ("o", 40, 15), ("f", 31, 48), ("o", 10, 40)]

# The sanctuary: a clearing at the end of the path, an old tree in the middle, surrounded by flowers
SANCTUARY = [
    "####...####",
    "####...####",
    "###.....###",
    "##.......##",
    "#.........#",
    "#.........#",
    "#....#....#",
    "#....#....#",
    "#....#....#",
    "#.........#",
    "#.........#",
    "##.......##",
    "###.....###",
    "###########",
    "###########",
    "###########",
    "###########",
    "###########",
]
SANCTUARY_DETAILS = [("f", 8, 5), ("f", 9, 5), ("f", 12, 5), ("f", 13, 5), ("f", 7, 6), ("f", 14, 6),
                     ("f", 7, 8), ("f", 14, 8), ("f", 8, 9), ("f", 13, 9), ("f", 9, 10), ("f", 10, 10),
                     ("f", 11, 10), ("f", 12, 10)]

BIG_TREES_BORDER = (0x1d4, 0x1d5, 0x1dc, 0x1dd)
SMALL_TREES_BORDER = (0x0c6, 0x0c7, 0x0c7, 0x0c6)  # as on Route 123
MAPS = [
    # name, plan, details, edges where the player may leave the map (side, first, last), border blocks
    ("NablaEmeraldForest_Entrance", ENTRANCE, ENTRANCE_DETAILS, [("up", 8, 13), ("down", 12, 15)], SMALL_TREES_BORDER),
    ("NablaEmeraldForest", FOREST, FOREST_DETAILS, [("up", 20, 23), ("down", 16, 21)], BIG_TREES_BORDER),
    ("NablaEmeraldForest_Sanctuary", SANCTUARY, SANCTUARY_DETAILS, [("up", 8, 13)], BIG_TREES_BORDER),
]

# --- Blocks
# Usual block value (metatile + collision + elevation) of each metatile in Emerald's maps on General
values = collections.defaultdict(collections.Counter)
for l in json.load(open("data/layouts/layouts.json"))["layouts"]:
    if l.get("primary_tileset") != "gTileset_General" or "Nabla" in l.get("name", ""):
        continue
    try:
        data = open(l["blockdata_filepath"], "rb").read()
    except OSError:
        continue
    if len(data) != l["width"] * l["height"] * 2:
        continue
    for v in struct.unpack("<%dH" % (len(data) // 2), data):
        values[v & 0x3FF][v] += 1


def block(mt):
    return values[mt].most_common(1)[0][0] if values[mt] else mt | (3 << 12)


FLOOR = {".": 0x001, "T": 0x00d}
DETAILS = {"f": 0x004, "o": 0x0e0}
LEDGE = (0x0d5, 0x087, 0x0d6)  # one-way ledge, jumped down


def runs(column):
    # (first, last) rows of each run of True
    y, out = 0, []
    while y < len(column):
        if not column[y]:
            y += 1
            continue
        a = y
        while y < len(column) and column[y]:
            y += 1
        out.append((a, y - 1))
    return out


def draw(name, plan, details, exits, border):
    grid = ["".join(c * 2 for c in row) for row in plan]
    H, W = len(grid), len(grid[0])
    assert all(len(row) == W for row in grid), name
    out = [[None] * W for _ in range(H)]
    problems = []

    def big(x, y):
        return 0 <= x < W and 0 <= y < H and grid[y][x] == "#"

    for y in range(H):
        for x in range(W):
            if grid[y][x] in FLOOR:
                out[y][x] = block(FLOOR[grid[y][x]])
    # Small trees, one column at a time
    for x in range(W):
        for a, b in runs([grid[y][x] == "%" for y in range(H)]):
            if 0 < a and b < H - 1 and b - a < 1:
                problems.append("small tree too short at %d,%d" % (x, a))
            for y in range(a, b + 1):
                mt = 0x0e if y == a and a > 0 else 0x16 if y == b and b < H - 1 else (0xc6, 0xc7)[(x + y) % 2]
                out[y][x] = block(mt)
    # Forest trees, two columns at a time
    for x in range(0, W, 2):
        for a, b in runs([big(x, y) for y in range(H)]):
            top, foot = a > 0, b < H - 1
            if top and foot and (b - a < 2 or (b - a) % 2):
                problems.append("forest trees %d rows tall at %d,%d" % (b - a + 1, x, a))
            for y in range(a, b + 1):
                if top and y == a:
                    left, right = 0x1ce, 0x1cf
                elif foot and y == b:
                    left = 0x1e4 if big(x - 1, y) else 0x1e6
                    right = 0x1e5 if big(x + 2, y) else 0x1e7
                else:
                    first = a + 1 if top else None
                    rows_left = (b - 1 - y) if foot else (y - first) if top else y
                    if rows_left % 2 == 0:
                        left, right = 0x1d4, 0x1d5
                        if top and y == a + 1:
                            left = 0x1d4 if big(x - 1, y) else 0x1d6
                            right = 0x1d5 if big(x + 2, y) else 0x1d7
                    else:
                        left, right = 0x1dc, 0x1dd
                out[y][x], out[y][x + 1] = block(left), block(right)
    # Details on grass
    for d in details:
        if d[0] == "L":
            _, x0, x1, y = d
            for x in range(x0, x1 + 1):
                if grid[y][x] not in FLOOR:
                    problems.append("ledge on %s at %d,%d" % (grid[y][x], x, y))
                out[y][x] = block(LEDGE[0] if x == x0 else LEDGE[2] if x == x1 else LEDGE[1])
        else:
            kind, x, y = d
            if grid[y][x] not in FLOOR:
                problems.append("%s on %s at %d,%d" % (kind, grid[y][x], x, y))
            out[y][x] = block(DETAILS[kind])
    # No cell the player can reach touches an edge without a connection
    walkable = {(x, y) for y in range(H) for x in range(W) if grid[y][x] in FLOOR} - \
               {(d[1], d[2]) for d in details if d[0] == "o"}
    allowed = set()
    for side, first, last in exits:
        for i in range(first, last + 1):
            allowed.add({"up": (i, 0), "down": (i, H - 1), "left": (0, i), "right": (W - 1, i)}[side])
    start = next(iter(sorted(allowed)))
    seen, todo = {start}, [start]
    while todo:
        x, y = todo.pop()
        for n in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if n in walkable and n not in seen:
                seen.add(n)
                todo.append(n)
    for x, y in sorted(seen):
        if (x in (0, W - 1) or y in (0, H - 1)) and (x, y) not in allowed:
            problems.append("reachable edge at %d,%d" % (x, y))
    for x, y in sorted(allowed - seen):
        problems.append("exit not reached at %d,%d" % (x, y))
    for p in problems:
        print("draw_emerald_forest.py: %s: %s" % (name, p))
    path = "data/layouts/%s/map.bin" % name
    open(path, "wb").write(struct.pack("<%dH" % (W * H), *[v for row in out for v in row]))
    open("data/layouts/%s/border.bin" % name, "wb").write(struct.pack("<4H", *border))
    return not problems


# --- Route 123: the small trees of its last row are opened over columns 102-107
def open_route123():
    layout = [l for l in json.load(open("data/layouts/layouts.json"))["layouts"] if l.get("id") == "LAYOUT_ROUTE123"][0]
    path, W = layout["blockdata_filepath"], layout["width"]
    data = list(struct.unpack("<%dH" % (len(open(path, "rb").read()) // 2), open(path, "rb").read()))
    for x in range(102, 108):
        data[19 * W + x] = block(0x001)
    open(path, "wb").write(struct.pack("<%dH" % len(data), *data))


if __name__ == "__main__":
    ok = all([draw(*m) for m in MAPS])
    open_route123()
    sys.exit(0 if ok else 1)
