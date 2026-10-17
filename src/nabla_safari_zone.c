#include "global.h"
#include "event_data.h"
#include "list_menu.h"
#include "malloc.h"
#include "nabla_safari_zone.h"
#include "regions.h"
#include "script_menu.h"
#include "string_util.h"
#include "constants/nabla.h"
#include "constants/region_map_sections.h"

// Pokémon Nabla's Safari Zone: each visit explores one region (VAR_NABLA_SAFARI_REGION).
// Kanto is always open; the other regions are unlocked at the counter, in any order.
// Wild encounters of a region: see src/wild_encounter.c and dev_scripts/nabla/safari_tables.py.

extern const u8 Nabla_Text_SafariZoneRegionKanto[];
extern const u8 Nabla_Text_SafariZoneRegionJohto[];
extern const u8 Nabla_Text_SafariZoneRegionSinnoh[];
extern const u8 Nabla_Text_SafariZoneRegionUnova[];
extern const u8 Nabla_Text_SafariZoneRegionKalos[];
extern const u8 Nabla_Text_SafariZoneRegionAlola[];
extern const u8 Nabla_Text_SafariZoneRegionGalar[];
extern const u8 Nabla_Text_SafariZoneRegionPaldea[];

struct SafariZoneRegion
{
    const u8 *name;
    u16 flag; // 0: always open
    u8 evolutionRegions[2]; // Regional evolutions (Alolan Raichu, Hisuian Typhlosion...) happen there
};

static const struct SafariZoneRegion sSafariZoneRegions[] =
{
    [NABLA_SAFARI_REGION_KANTO]  = {Nabla_Text_SafariZoneRegionKanto,  0,                        {REGION_KANTO}},
    [NABLA_SAFARI_REGION_JOHTO]  = {Nabla_Text_SafariZoneRegionJohto,  FLAG_NABLA_SAFARI_JOHTO,  {REGION_JOHTO}},
    [NABLA_SAFARI_REGION_SINNOH] = {Nabla_Text_SafariZoneRegionSinnoh, FLAG_NABLA_SAFARI_SINNOH, {REGION_SINNOH}},
    [NABLA_SAFARI_REGION_UNOVA]  = {Nabla_Text_SafariZoneRegionUnova,  FLAG_NABLA_SAFARI_UNOVA,  {REGION_UNOVA}},
    [NABLA_SAFARI_REGION_KALOS]  = {Nabla_Text_SafariZoneRegionKalos,  FLAG_NABLA_SAFARI_KALOS,  {REGION_KALOS}},
    [NABLA_SAFARI_REGION_ALOLA]  = {Nabla_Text_SafariZoneRegionAlola,  FLAG_NABLA_SAFARI_ALOLA,  {REGION_ALOLA}},
    [NABLA_SAFARI_REGION_GALAR]  = {Nabla_Text_SafariZoneRegionGalar,  FLAG_NABLA_SAFARI_GALAR,  {REGION_GALAR, REGION_HISUI}},
    [NABLA_SAFARI_REGION_PALDEA] = {Nabla_Text_SafariZoneRegionPaldea, FLAG_NABLA_SAFARI_PALDEA, {REGION_PALDEA}},
};

bool32 InSafariZoneRegion(void)
{
    return gMapHeader.regionMapSectionId == MAPSEC_SAFARI_ZONE && VarGet(VAR_NABLA_SAFARI_REGION) != NABLA_SAFARI_REGION_NONE;
}

static bool32 IsSafariZoneRegionOpen(u32 region)
{
    return sSafariZoneRegions[region].flag == 0 || FlagGet(sSafariZoneRegions[region].flag);
}

// Region of the IF_REGION / IF_NOT_REGION evolution conditions: in the Safari Zone, the region being explored
bool32 IsPlayerInEvolutionRegion(enum Region region)
{
    u32 safariRegion = VarGet(VAR_NABLA_SAFARI_REGION);

    if (!InSafariZoneRegion() || safariRegion >= ARRAY_COUNT(sSafariZoneRegions))
        return GetCurrentRegion() == region;
    return sSafariZoneRegions[safariRegion].evolutionRegions[0] == region
        || sSafariZoneRegions[safariRegion].evolutionRegions[1] == region;
}

// Counter menus: pushes the open regions (VAR_0x8004 = FALSE) or the locked ones (TRUE) to dynmultistack
void NablaSafariZone_PushRegions(void)
{
    bool32 pushLocked = gSpecialVar_0x8004;
    u32 i;

    for (i = NABLA_SAFARI_REGION_KANTO; i < ARRAY_COUNT(sSafariZoneRegions); i++)
    {
        if (IsSafariZoneRegionOpen(i) != pushLocked)
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

u16 NablaSafariZone_CountLockedRegions(void)
{
    u32 i, count = 0;

    for (i = NABLA_SAFARI_REGION_KANTO; i < ARRAY_COUNT(sSafariZoneRegions); i++)
    {
        if (!IsSafariZoneRegionOpen(i))
            count++;
    }
    return count;
}

// VAR_0x8005: region
void NablaSafariZone_UnlockRegion(void)
{
    FlagSet(sSafariZoneRegions[gSpecialVar_0x8005].flag);
}

// VAR_0x8005: region
void NablaSafariZone_BufferRegionName(void)
{
    StringCopy(gStringVar1, sSafariZoneRegions[gSpecialVar_0x8005].name);
}
