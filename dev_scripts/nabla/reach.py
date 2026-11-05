#!/usr/bin/env python3
"""Where the player can go on a map, following the rules of the game (GetCollisionAtCoords,
src/event_object_movement.c; IsPlayerFacingSurfableFishableWater and CanStopSurfing, src/field_player_avatar.c):
a block with collision stops the player; two elevations other than 0 and 15 must be equal (a block of elevation 0,
like stairs, goes between elevations); surfing starts from elevation 3 onto water of elevation 1 and stops on
elevation 3; a ledge is jumped in its direction, landing two cells further.

Run on a map, it checks that the player can walk to every object of the map (Pokémon, items) from a cell, that no
object cuts off a part of the map, and that the Pokémon in view never fill the memory of sprites: the whole sheet of
a Pokémon's sprite is loaded (OW_GFX_COMPRESS), 384 tiles for a big one (64 x 64), and only two big sheets fit next
to the player (the mirages hide the following Pokémon with FLAG_TEMP_HIDE_FOLLOWER); beyond, sprites show garbage.
A Pokémon called by an altar is never there with the Pokémon it asks for in the party (caught, so gone from the map).
Usage (from the repo root): python3 dev_scripts/nabla/reach.py <Map> <x> <y>
"""
import json
import os
import re
import struct
import sys

from PIL import Image

SPRITE_TILES = 768                   # two big sheets
VIEW_LEFT, VIEW_RIGHT, VIEW_UP, VIEW_DOWN = 9, 10, 7, 9  # objects spawned around the player (TrySpawnObjectEvents)

elevation = lambda v: v >> 12
blocked = lambda v: (v >> 10) & 3


def ledges(blocks, primary, secondary):
    """The direction (dx, dy) in which each ledge of a layout is jumped (behaviors MB_JUMP_*), None elsewhere."""
    names = re.findall(r"^\s*(MB_\w+)", open("include/constants/metatile_behaviors.h").read(), re.M)
    folder = lambda tileset, kind: "data/tilesets/%s/%s/metatile_attributes.bin" % (
        kind, re.sub(r"(?<!^)(?=[A-Z])", "_", tileset[len("gTileset_"):]).lower())
    attributes = open(folder(primary, "primary"), "rb").read(), open(folder(secondary, "secondary"), "rb").read()
    directions = {"MB_JUMP_EAST": (1, 0), "MB_JUMP_WEST": (-1, 0), "MB_JUMP_NORTH": (0, -1), "MB_JUMP_SOUTH": (0, 1)}

    def jump(v):
        m = v & 0x3FF
        data, i = (attributes[0], m) if m < 0x200 else (attributes[1], m - 0x200)
        return directions.get(names[struct.unpack_from("<H", data, 2 * i)[0] & 0xFF])
    return [[jump(v) for v in row] for row in blocks]


def reach(blocks, start, objects=(), jumps=None):
    """The cells reached from start, walking or surfing, without going through the objects, and the objects next to
    a cell reached on foot, at its elevation (where the player can talk to them). jumps: ledges(...), for a map with
    ledges."""
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
            if not (0 <= nx < W and 0 <= ny < H):
                continue
            if jumps and not surfing and jumps[ny][nx] == (nx - x, ny - y):
                lx, ly = 2 * nx - x, 2 * ny - y
                if 0 <= lx < W and 0 <= ly < H and not blocked(blocks[ly][lx]) and (lx, ly) not in objects:
                    todo.append((lx, ly, False))
                continue
            if blocked(blocks[ny][nx]):
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


def sheet_tiles(graphics_id):
    """Tiles of the whole sheet of a Pokémon's sprite (OBJ_EVENT_GFX_SPECIES), 0 for other objects."""
    m = re.fullmatch(r"OBJ_EVENT_GFX_SPECIES\((\w+)\)", graphics_id)
    if not m:
        return 0
    name = m.group(1).lower()
    base, _, form = name.rpartition("_")
    for path in ("graphics/pokemon/%s/overworld.png" % name, "graphics/pokemon/%s/%s/overworld.png" % (base, form)):
        if os.path.exists(path):
            w, h = Image.open(path).size
            return w * h // 64
    raise FileNotFoundError(graphics_id)


def altar_requirements():
    """The Pokémon each Pokémon called by an altar asks for (data/scripts/nabla/mirages.inc), as species names."""
    s = open("data/scripts/nabla/mirages.inc", encoding="utf-8").read()
    return {m.group(1): set(re.findall(r"setvar VAR_0x8004, SPECIES_(\w+)", m.group(2))) for m in
            re.finditer(r"goto_if_set FLAG_NABLA_(\w+)_CAUGHT, \w+\n(.*?)\taddobject LOCALID_\w+?_\1\n", s, re.S)}


def load(name):
    """The map.json of a map, its blocks and its ledges."""
    m = json.load(open("data/maps/%s/map.json" % name))
    layout = next(l for l in json.load(open("data/layouts/layouts.json"))["layouts"] if l.get("id") == m["layout"])
    W, H = layout["width"], layout["height"]
    raw = open(layout["blockdata_filepath"], "rb").read()
    blocks = [[struct.unpack_from("<H", raw, 2 * (y * W + x))[0] for x in range(W)] for y in range(H)]
    return m, blocks, ledges(blocks, layout["primary_tileset"], layout["secondary_tileset"])


if __name__ == "__main__":
    name, start = sys.argv[1], (int(sys.argv[2]), int(sys.argv[3]))
    m, blocks, jumps = load(name)
    objects = {(o["x"], o["y"]): o for o in m["object_events"]}
    cells, talked = reach(blocks, start, objects, jumps)
    alone, _ = reach(blocks, start, (), jumps)
    problems = ["%s at (%d, %d): not reached on foot" % (o["graphics_id"], x, y)
                for (x, y), o in objects.items() if (x, y) not in talked]
    problems += ["%s at (%d, %d): elevation %d on a block of elevation %d"
                 % (o["graphics_id"], x, y, o["elevation"], elevation(blocks[y][x]))
                 for (x, y), o in objects.items() if elevation(blocks[y][x]) not in (o["elevation"], 0, 15)]
    problems += ["(%d, %d): cut off by the objects" % c for c in sorted(alone - cells - set(objects))]
    # The sheets in view, from every cell the player can stand on (one sheet per species), the Pokémon called by an
    # altar being there or not, without the Pokémon they ask for when they are
    species = lambda o: re.sub(r"OBJ_EVENT_GFX_SPECIES\((\w+)\)", r"\1", o["graphics_id"])
    requirements = altar_requirements()
    called = sorted({species(o) for o in objects.values()} & set(requirements))
    for px, py in sorted(cells):
        in_view = {species(o): sheet_tiles(o["graphics_id"]) for (x, y), o in objects.items()
                   if px - VIEW_LEFT <= x <= px + VIEW_RIGHT and py - VIEW_UP <= y <= py + VIEW_DOWN}
        worst = (0, ())
        for k in range(1 << len(called)):
            there = {c for i, c in enumerate(called) if k >> i & 1}
            gone = set(called) - there | set().union(*(requirements[c] for c in there))
            seen = {sp: tiles for sp, tiles in in_view.items() if sp not in gone}
            worst = max(worst, (sum(seen.values()), tuple(sorted(sp for sp in seen if seen[sp]))))
        if worst[0] > SPRITE_TILES:
            problems.append("(%d, %d): too many sprites in view (%d tiles): %s" % (px, py, worst[0], ", ".join(worst[1])))
            break
    print("\n".join(problems) or "%s: every object can be reached on foot" % name)
    sys.exit(bool(problems))
