#include "global.h"
#include "event_data.h"
#include "list_menu.h"
#include "malloc.h"
#include "money.h"
#include "nabla_safari_zone.h"
#include "random.h"
#include "regions.h"
#include "script_menu.h"
#include "string_util.h"
#include "constants/nabla.h"
#include "constants/region_map_sections.h"

// Pokémon Nabla's Safari Zone: each visit explores one region (VAR_NABLA_SAFARI_REGION).
// Kanto is always open; the other regions are unlocked at the counter, in any order, and the
// special zones too after the League.
// Wild encounters of a region: see src/wild_encounter.c and dev_scripts/nabla/safari_tables.py.

extern const u8 Nabla_Text_SafariZoneRegionKanto[];
extern const u8 Nabla_Text_SafariZoneRegionJohto[];
extern const u8 Nabla_Text_SafariZoneRegionSinnoh[];
extern const u8 Nabla_Text_SafariZoneRegionUnova[];
extern const u8 Nabla_Text_SafariZoneRegionKalos[];
extern const u8 Nabla_Text_SafariZoneRegionAlola[];
extern const u8 Nabla_Text_SafariZoneRegionGalar[];
extern const u8 Nabla_Text_SafariZoneRegionPaldea[];
extern const u8 Nabla_Text_SafariZoneRegionStarters[];
extern const u8 Nabla_Text_SafariZoneRegionParadox[];
extern const u8 Nabla_Text_SafariZoneRegionUltraBeasts[];
extern const u8 Nabla_Text_SafariZoneRegionPrice[];
extern const u8 Nabla_Text_SafariZoneSpecialPrice[];

#define REGION(text, flagId, ...) {.name = text, .flag = flagId, .price = NABLA_SAFARI_REGION_PRICE, .priceText = Nabla_Text_SafariZoneRegionPrice, .evolutionRegions = {__VA_ARGS__}}
#define SPECIAL_ZONE(text, flagId) {.name = text, .flag = flagId, .price = NABLA_SAFARI_SPECIAL_PRICE, .priceText = Nabla_Text_SafariZoneSpecialPrice, .afterLeague = TRUE}

struct SafariZoneRegion
{
    const u8 *name;
    u16 flag; // 0: always open
    u32 price;
    const u8 *priceText;
    bool8 afterLeague;
    u8 evolutionRegions[2]; // Regional evolutions (Alolan Raichu, Hisuian Typhlosion...) happen there
};

static const struct SafariZoneRegion sSafariZoneRegions[] =
{
    [NABLA_SAFARI_REGION_KANTO]        = REGION(Nabla_Text_SafariZoneRegionKanto,  0,                        REGION_KANTO),
    [NABLA_SAFARI_REGION_JOHTO]        = REGION(Nabla_Text_SafariZoneRegionJohto,  FLAG_NABLA_SAFARI_JOHTO,  REGION_JOHTO),
    [NABLA_SAFARI_REGION_SINNOH]       = REGION(Nabla_Text_SafariZoneRegionSinnoh, FLAG_NABLA_SAFARI_SINNOH, REGION_SINNOH),
    [NABLA_SAFARI_REGION_UNOVA]        = REGION(Nabla_Text_SafariZoneRegionUnova,  FLAG_NABLA_SAFARI_UNOVA,  REGION_UNOVA),
    [NABLA_SAFARI_REGION_KALOS]        = REGION(Nabla_Text_SafariZoneRegionKalos,  FLAG_NABLA_SAFARI_KALOS,  REGION_KALOS),
    [NABLA_SAFARI_REGION_ALOLA]        = REGION(Nabla_Text_SafariZoneRegionAlola,  FLAG_NABLA_SAFARI_ALOLA,  REGION_ALOLA),
    [NABLA_SAFARI_REGION_GALAR]        = REGION(Nabla_Text_SafariZoneRegionGalar,  FLAG_NABLA_SAFARI_GALAR,  REGION_GALAR, REGION_HISUI),
    [NABLA_SAFARI_REGION_PALDEA]       = REGION(Nabla_Text_SafariZoneRegionPaldea, FLAG_NABLA_SAFARI_PALDEA, REGION_PALDEA),
    [NABLA_SAFARI_REGION_STARTERS]     = SPECIAL_ZONE(Nabla_Text_SafariZoneRegionStarters,    FLAG_NABLA_SAFARI_STARTERS),
    [NABLA_SAFARI_REGION_PARADOX]      = SPECIAL_ZONE(Nabla_Text_SafariZoneRegionParadox,     FLAG_NABLA_SAFARI_PARADOX),
    [NABLA_SAFARI_REGION_ULTRA_BEASTS] = SPECIAL_ZONE(Nabla_Text_SafariZoneRegionUltraBeasts, FLAG_NABLA_SAFARI_ULTRA_BEASTS),
};

bool32 InSafariZoneRegion(void)
{
    return gMapHeader.regionMapSectionId == MAPSEC_SAFARI_ZONE && VarGet(VAR_NABLA_SAFARI_REGION) != NABLA_SAFARI_REGION_NONE;
}

// Levels follow the player's badges: those of the nearby routes when the Safari Zone opens, 60-70 after
// the League. Starters are always met at level 5, as when they are received.
u8 GetSafariZoneRegionWildLevel(void)
{
    static const u8 sLevelRanges[NUM_BADGES + 2][2] =
    {
        {5, 8}, {9, 12}, {13, 16}, {17, 20}, {21, 24}, {24, 27}, {27, 31}, {33, 37}, {40, 45}, // by badge count
        {60, 70}, // League champion
    };
    u32 range = 0;

    if (VarGet(VAR_NABLA_SAFARI_REGION) == NABLA_SAFARI_REGION_STARTERS)
        return 5;
    if (FlagGet(FLAG_IS_CHAMPION))
    {
        range = NUM_BADGES + 1;
    }
    else
    {
        for (u32 flag = FLAG_BADGE01_GET; flag < FLAG_BADGE01_GET + NUM_BADGES; flag++)
            range += FlagGet(flag);
    }
    return sLevelRanges[range][0] + Random() % (sLevelRanges[range][1] - sLevelRanges[range][0] + 1);
}

static bool32 IsSafariZoneRegionOpen(u32 region)
{
    return sSafariZoneRegions[region].flag == 0 || FlagGet(sSafariZoneRegions[region].flag);
}

static bool32 IsSafariZoneRegionForSale(u32 region)
{
    return !IsSafariZoneRegionOpen(region) && (!sSafariZoneRegions[region].afterLeague || FlagGet(FLAG_IS_CHAMPION));
}

// Region of the IF_REGION / IF_NOT_REGION evolution conditions: in the Safari Zone, the region being explored
bool32 IsPlayerInEvolutionRegion(enum Region region)
{
    u32 safariRegion = VarGet(VAR_NABLA_SAFARI_REGION);

    if (!InSafariZoneRegion() || safariRegion >= ARRAY_COUNT(sSafariZoneRegions)
     || sSafariZoneRegions[safariRegion].evolutionRegions[0] == REGION_NONE)
        return GetCurrentRegion() == region;
    return sSafariZoneRegions[safariRegion].evolutionRegions[0] == region
        || sSafariZoneRegions[safariRegion].evolutionRegions[1] == region;
}

// Counter menus: pushes the open regions (VAR_0x8004 = FALSE) or the ones for sale (TRUE) to dynmultistack
void NablaSafariZone_PushRegions(void)
{
    bool32 pushForSale = gSpecialVar_0x8004;
    u32 i;

    for (i = NABLA_SAFARI_REGION_KANTO; i < ARRAY_COUNT(sSafariZoneRegions); i++)
    {
        if (pushForSale ? IsSafariZoneRegionForSale(i) : IsSafariZoneRegionOpen(i))
        {
            struct ListMenuItem item;
            u8 *name = Alloc(StringLength(sSafariZoneRegions[i].name) + 1); // freed by the multichoice

            StringCopy(name, sSafariZoneRegions[i].name);
            item.name = name;
            item.id = i;
            MultichoiceDynamic_PushElement(item);
        }
    }
}

u16 NablaSafariZone_CountRegionsForSale(void)
{
    u32 i, count = 0;

    for (i = NABLA_SAFARI_REGION_KANTO; i < ARRAY_COUNT(sSafariZoneRegions); i++)
    {
        if (IsSafariZoneRegionForSale(i))
            count++;
    }
    return count;
}

// VAR_0x8005: region. Returns FALSE if the player can't afford it.
u16 NablaSafariZone_TryBuyRegion(void)
{
    const struct SafariZoneRegion *region = &sSafariZoneRegions[gSpecialVar_0x8005];

    if (!IsEnoughMoney(&gSaveBlock1Ptr->money, region->price))
        return FALSE;
    RemoveMoney(&gSaveBlock1Ptr->money, region->price);
    FlagSet(region->flag);
    return TRUE;
}

// VAR_0x8005: region. Buffers its name in STR_VAR_1 and its price in STR_VAR_2.
void NablaSafariZone_BufferRegionName(void)
{
    StringCopy(gStringVar1, sSafariZoneRegions[gSpecialVar_0x8005].name);
    StringCopy(gStringVar2, sSafariZoneRegions[gSpecialVar_0x8005].priceText);
}
