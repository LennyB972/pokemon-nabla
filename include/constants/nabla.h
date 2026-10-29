#ifndef GUARD_CONSTANTS_NABLA_H
#define GUARD_CONSTANTS_NABLA_H

// Safari Zone regions: values of VAR_NABLA_SAFARI_REGION (NONE uses the original tables).
// Each Safari Zone area lists its region tables in this order after its own table in
// src/data/wild_encounters.json (see dev_scripts/nabla/safari_tables.py).
#define NABLA_SAFARI_REGION_NONE         0
#define NABLA_SAFARI_REGION_KANTO        1
#define NABLA_SAFARI_REGION_JOHTO        2
#define NABLA_SAFARI_REGION_SINNOH       3
#define NABLA_SAFARI_REGION_UNOVA        4
#define NABLA_SAFARI_REGION_KALOS        5
#define NABLA_SAFARI_REGION_ALOLA        6
#define NABLA_SAFARI_REGION_GALAR        7
#define NABLA_SAFARI_REGION_PALDEA       8
#define NABLA_SAFARI_REGION_STARTERS     9
#define NABLA_SAFARI_REGION_PARADOX      10
#define NABLA_SAFARI_REGION_ULTRA_BEASTS 11

// Safari Zone counter: prices (also written in data/text/nabla/safari_zone.inc), extra entries of the region menus
#define NABLA_SAFARI_REGION_PRICE  30000
#define NABLA_SAFARI_SPECIAL_PRICE 100000 // Starters, Paradox and Ultra Beasts, after the League
#define NABLA_SAFARI_MENU_UNLOCK   100
#define NABLA_SAFARI_MENU_CANCEL   101

// Level from which wild and trainers' Pokémon take the evolutions that need more than a level
// (trade, item, friendship...): Onix is a Steelix from level 40
#define NABLA_OTHER_EVOLUTIONS_LEVEL 40

// Rayquaza and Deoxys at the top of Sky Pillar, after the eighth Gym (data/scripts/nabla/rayquaza_event.inc)
#define NABLA_SKY_PILLAR_LEGENDARIES_LEVEL 65

// Legendary Pokémon after the League (Celebi with the GS Ball, mirages...)
#define NABLA_POST_GAME_LEGENDARIES_LEVEL 80

// Title defense (data/scripts/nabla/title_defense.inc): challengers, in the order of the first three.
// VAR_NABLA_TITLE_DEFENSE is the next of the first three challengers, then NABLA_TITLE_DEFENSE_RANDOM
// + the last challenger beaten.
#define NABLA_CHALLENGER_WALLY         0
#define NABLA_CHALLENGER_STEVEN        1
#define NABLA_CHALLENGER_WALLACE       2
#define NABLA_CHALLENGER_ROXANNE       3
#define NABLA_CHALLENGER_BRAWLY        4
#define NABLA_CHALLENGER_WATTSON       5
#define NABLA_CHALLENGER_FLANNERY      6
#define NABLA_CHALLENGER_NORMAN        7
#define NABLA_CHALLENGER_WINONA        8
#define NABLA_CHALLENGER_TATE_AND_LIZA 9
#define NABLA_CHALLENGER_JUAN          10
#define NABLA_CHALLENGER_MAXIE         11
#define NABLA_CHALLENGER_ARCHIE        12
#define NABLA_CHALLENGERS_COUNT        13
#define NABLA_TITLE_DEFENSE_RANDOM     3

#endif // GUARD_CONSTANTS_NABLA_H
