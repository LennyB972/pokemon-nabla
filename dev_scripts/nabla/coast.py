"""Turns the plan of a coast (sea, sand, grass, trees, rocks) into blocks of the General tileset.

Shared by the scripts that draw Nabla's beaches and islands (draw_west_beach.py, draw_bird_islet.py). Plan cells:
"~" sea, "." sand, "g" grass, "T" tall grass, "f" flowers, "o" rock on grass, "r" rock on sand, "D" under a rock
mound. Objects drawn over the cells: ("tree", x, y, rows), ("dome", x, y), ("searock", x, y, kind).
Shores and grass edges are picked from the neighbours of each cell, and each block keeps the collision and
elevation it has in Emerald's maps. The rules of the tiles are in docs/nabla/zones.md.
"""
import collections
import json
import struct

WATER_EDGES = {(1,0,0,0): 0x11c, (0,1,0,0): 0x12c, (0,0,1,0): 0x123, (0,0,0,1): 0x125,
               (1,0,1,0): 0x11b, (1,0,0,1): 0x11d, (0,1,1,0): 0x12b, (0,1,0,1): 0x12d}
GRASS_EDGES = {(1,0,0,0): 0x119, (0,1,0,0): 0x129, (0,0,1,0): 0x120, (0,0,0,1): 0x122,
               (1,0,1,0): 0x118, (1,0,0,1): 0x11a, (0,1,1,0): 0x128, (0,1,0,1): 0x12a}
SEA_ROCKS = {"foam": [(0x150, 0x151), (0x158, 0x159)], "brown": [(0x175, 0x176), (0x17d, 0x17e)],
             "moss": [(0x348, 0x349), (0x350, 0x351)]}

# Usual block value (metatile + collision + elevation) of each metatile in Emerald's maps on General
_values = collections.defaultdict(collections.Counter)
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
        _values[v & 0x3FF][v] += 1


def block(mt):
    return _values[mt].most_common(1)[0][0] if _values[mt] else mt | (3 << 12)


def to_blocks(grid, objects, outside=lambda x, y: "w"):
    """Blocks of the plan, and the cells for which no block fits. outside(x, y) gives the kind ("w" sea,
    "s" sand) of a cell off the map, as seen through the border or a connection."""
    H, W = len(grid), len(grid[0])

    def kind(x, y):
        if not (0 <= x < W and 0 <= y < H):
            return outside(x, y)
        c = grid[y][x]
        return "w" if c == "~" else "s" if c in ".rD" else "g"
    out = [[0] * W for _ in range(H)]
    problems = []
    for y in range(H):
        for x in range(W):
            c = grid[y][x]
            if c == "~":
                out[y][x] = block(0x170)
            elif c in ".rD":
                n = {d: kind(x + dx, y + dy) for d, (dx, dy) in {"u": (0,-1), "d": (0,1), "l": (-1,0), "r": (1,0)}.items()}
                wk = tuple(int(n[d] == "w") for d in "udlr")
                gk = tuple(int(n[d] == "g") for d in "udlr")
                if any(wk) and any(gk):
                    problems.append((x, y, "water and grass"))
                if any(wk):
                    mt = WATER_EDGES.get(wk)
                    if mt is None:
                        problems.append((x, y, "water edges %s" % (wk,))); mt = 0x124
                elif any(gk):
                    mt = GRASS_EDGES.get(gk)
                    if mt is None:
                        problems.append((x, y, "grass edges %s" % (gk,))); mt = 0x124
                else:
                    diag = {d: kind(x + dx, y + dy) for d, (dx, dy) in {"ul": (-1,-1), "ur": (1,-1), "dl": (-1,1), "dr": (1,1)}.items()}
                    mt = {"ul": 0x13d, "ur": 0x13e, "dl": 0x145, "dr": 0x146}.get(next((d for d, k in diag.items() if k == "w"), None), 0x124)
                out[y][x] = block(mt)
                if c == "r":
                    out[y][x] = block(0xe2)
            elif c == "T":
                out[y][x] = block(0x0d)
            elif c == "f":
                out[y][x] = block(0x04)
            elif c == "o":
                out[y][x] = block(0xe0)
            else:  # grass, and under trees
                out[y][x] = block(0x01)
    for o in objects:
        if o[0] == "tree":   # stacked trees, n rows = 3 + 2k
            x, y, n = o[1], o[2], o[3] if len(o) > 3 else 3
            seq = [(0x1ce, 0x1cf), (0x1d6, 0x1d7)] + [((0x1dc, 0x1dd), (0x1d4, 0x1d5))[i % 2] for i in range(n - 3)] + [(0x1e6, 0x1e7)]
            for i, (a, b) in enumerate(seq):
                out[y + i][x], out[y + i][x + 1] = block(a), block(b)
        elif o[0] == "dome":
            x, y = o[1], o[2]
            for j, r in enumerate([(0x80, 0x81, 0x82), (0x88, 0x71, 0x8a), (0x90, 0x79, 0x92)]):
                for i, mt in enumerate(r):
                    out[y + j][x + i] = block(mt)
        elif o[0] == "searock":
            x, y = o[1], o[2]
            for j, r in enumerate(SEA_ROCKS[o[3] if len(o) > 3 else "foam"]):
                for i, mt in enumerate(r):
                    out[y + j][x + i] = block(mt)
    problems = [p for p in problems if grid[p[1]][p[0]] != "D"]  # cells under a mound are drawn over
    return out, problems


def write(path, out):
    H, W = len(out), len(out[0])
    open(path, "wb").write(struct.pack("<%dH" % (W * H), *[v for row in out for v in row]))
