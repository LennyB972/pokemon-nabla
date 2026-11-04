#!/usr/bin/env python3
"""Where the player can go on a map, following the rules of the game (GetCollisionAtCoords,
src/event_object_movement.c; IsPlayerFacingSurfableFishableWater and CanStopSurfing, src/field_player_avatar.c):
a block with collision stops the player; two elevations other than 0 and 15 must be equal (a block of elevation 0,
like stairs, goes between elevations); surfing starts from elevation 3 onto water of elevation 1 and stops on
elevation 3.

Run on a map, it checks that the player can walk to every object of the map (Pokémon, items) from a cell, and that
no object cuts off a part of the map.
Usage (from the repo root): python3 dev_scripts/nabla/reach.py <Map> <x> <y>
"""
import json
import struct
import sys

elevation = lambda v: v >> 12
blocked = lambda v: (v >> 10) & 3


def reach(blocks, start, objects=()):
    """The cells reached from start, walking or surfing, without going through the objects, and the objects next to
    a cell reached on foot, at its elevation (where the player can talk to them)."""
    H, W = len(blocks), len(blocks[0])
    objects = set(objects)
    seen, talked, todo = set(), set(), [tuple(start) + (False,)]
    while todo:
        state = todo.pop()
        if state in seen:
            continue
        seen.add(state)
        x, y, surfing = state
        e0 = elevation(blocks[y][x])
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if not (0 <= nx < W and 0 <= ny < H) or blocked(blocks[ny][nx]):
                continue
            e1 = elevation(blocks[ny][nx])
            if (nx, ny) in objects:
                if not surfing and e1 in (e0, 0, 15):
                    talked.add((nx, ny))
            elif surfing:
                if e1 in (1, 3):
                    todo.append((nx, ny, e1 == 1))
            elif e1 == 1:
                assert e0 != 0, ("the player walks on the water from", x, y)
                if e0 == 3:
                    todo.append((nx, ny, True))
            elif e0 in (0, 15) or e1 in (0, 15) or e0 == e1:
                todo.append((nx, ny, False))
    return {(x, y) for x, y, _ in seen}, talked


def load(name):
    m = json.load(open("data/maps/%s/map.json" % name))
    layout = next(l for l in json.load(open("data/layouts/layouts.json"))["layouts"] if l.get("id") == m["layout"])
    W, H = layout["width"], layout["height"]
    raw = open(layout["blockdata_filepath"], "rb").read()
    return m, [[struct.unpack_from("<H", raw, 2 * (y * W + x))[0] for x in range(W)] for y in range(H)]


if __name__ == "__main__":
    name, start = sys.argv[1], (int(sys.argv[2]), int(sys.argv[3]))
    m, blocks = load(name)
    objects = {(o["x"], o["y"]): o for o in m["object_events"]}
    cells, talked = reach(blocks, start, objects)
    alone, _ = reach(blocks, start)
    problems = ["%s at (%d, %d): not reached on foot" % (o["graphics_id"], x, y)
                for (x, y), o in objects.items() if (x, y) not in talked]
    problems += ["%s at (%d, %d): elevation %d on a block of elevation %d"
                 % (o["graphics_id"], x, y, o["elevation"], elevation(blocks[y][x]))
                 for (x, y), o in objects.items() if elevation(blocks[y][x]) not in (o["elevation"], 0, 15)]
    problems += ["(%d, %d): cut off by the objects" % c for c in sorted(alone - cells - set(objects))]
    print("\n".join(problems) or "%s: every object can be reached on foot" % name)
    sys.exit(bool(problems))
