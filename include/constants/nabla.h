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

// Safari Zone counter: price of a region, extra entries of the region menus
#define NABLA_SAFARI_REGION_PRICE  30000
#define NABLA_SAFARI_MENU_UNLOCK   100
#define NABLA_SAFARI_MENU_CANCEL   101

#endif // GUARD_CONSTANTS_NABLA_H
