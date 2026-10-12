# Pokémon Nabla

**Pokémon Nabla** is an enhanced version of Pokémon Emerald that brings new content without breaking the original game. The story and maps of Emerald stay intact: Nabla adds to them instead of replacing them.

> 🚧 **In development** — no playable release yet.

## Planned features

- Modern battle mechanics (Gen 9 damage, Fairy type, recent abilities and moves), Mega Evolution
- Full National Pokédex (Gen 1 to 9)
- Two difficulty modes and optional level caps, chosen at the start of the game
- Quality of life: running indoors, instant text, modern Exp. Share, reusable TMs, HMs replaced by key items, following Pokémon, day/night cycle
- New areas during the adventure and in the post-game, story additions, stronger post-game League

## How to play

Nabla is distributed as a **BPS patch**.

1. Get a clean **Pokémon Emerald (USA)** ROM. SHA1: `f3ae088181bf583e55daf962a92bb46f4f1d07b7`.
2. Apply the patch with [Rom Patcher JS](https://www.marcrobledo.com/RomPatcher.js/) or [Flips](https://github.com/Alcaro/Flips).
3. Play on an emulator that supports the cartridge clock (RTC), such as [mGBA](https://mgba.io/), for the day/night cycle.

## Building from source

Follow [`INSTALL.md`](INSTALL.md) to set up the toolchain, then run `make`.
To build the release ROM and the BPS patch: `./make_bps.sh` (requires [Flips](https://github.com/Alcaro/Flips) and a clean Emerald (USA) ROM).

## Credits

- Based off RHH's **pokeemerald-expansion** 1.17.2 — https://github.com/rh-hideout/pokeemerald-expansion/ — by **RHH (Rom Hacking Hideout)** and [all its contributors](CREDITS.md).
- Built on [pret's `pokeemerald`](https://github.com/pret/pokeemerald) decompilation project.

Pokémon Nabla is a non-commercial fan project. Pokémon is © Nintendo, Creatures Inc. and GAME FREAK inc.
