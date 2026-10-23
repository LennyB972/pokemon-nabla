#include "global.h"
#include "event_data.h"
#include "money.h"
#include "nabla_safari_zone.h"
#include "pokemon.h"
#include "test/test.h"
#include "constants/nabla.h"
#include "constants/region_map_sections.h"

TEST("Nabla: regional evolutions happen in the matching Safari Zone region")
{
    struct Pokemon mon;
    bool32 canStopEvo;
    enum Species species = SPECIES_NONE, evolution = SPECIES_NONE;
    enum Item item = ITEM_NONE;
    u32 mapsec = MAPSEC_SAFARI_ZONE, region = NABLA_SAFARI_REGION_NONE, level = 5;

    PARAMETRIZE { species = SPECIES_PIKACHU; item = ITEM_THUNDER_STONE; region = NABLA_SAFARI_REGION_KANTO; evolution = SPECIES_RAICHU; }
    PARAMETRIZE { species = SPECIES_PIKACHU; item = ITEM_THUNDER_STONE; region = NABLA_SAFARI_REGION_ALOLA; evolution = SPECIES_RAICHU_ALOLA; }
    PARAMETRIZE { species = SPECIES_QUILAVA; level = 36; evolution = SPECIES_TYPHLOSION; }
    PARAMETRIZE { species = SPECIES_QUILAVA; level = 36; region = NABLA_SAFARI_REGION_GALAR; evolution = SPECIES_TYPHLOSION_HISUI; }
    PARAMETRIZE { species = SPECIES_QUILAVA; level = 36; region = NABLA_SAFARI_REGION_GALAR; mapsec = MAPSEC_ROUTE_121; evolution = SPECIES_TYPHLOSION; }

    gMapHeader.regionMapSectionId = mapsec;
    VarSet(VAR_NABLA_SAFARI_REGION, region);
    CreateMon(&mon, species, level, 0, OTID_STRUCT_PLAYER_ID);
    EXPECT_EQ(GetEvolutionTargetSpecies(&mon, item == ITEM_NONE ? EVO_MODE_NORMAL : EVO_MODE_ITEM_USE, item, NULL, &canStopEvo, CHECK_EVO), evolution);
}

TEST("Nabla: Safari Zone Pokémon are level 5 in the Starter Zone and follow the badges elsewhere")
{
    u32 region = NABLA_SAFARI_REGION_NONE, badges = 0, champion = FALSE, minLevel = 0, maxLevel = 0;

    PARAMETRIZE { region = NABLA_SAFARI_REGION_KANTO; minLevel = 5; maxLevel = 8; }
    PARAMETRIZE { region = NABLA_SAFARI_REGION_KANTO; badges = 6; minLevel = 38; maxLevel = 42; }
    PARAMETRIZE { region = NABLA_SAFARI_REGION_KANTO; badges = 7; minLevel = 48; maxLevel = 52; }
    PARAMETRIZE { region = NABLA_SAFARI_REGION_KANTO; badges = 8; minLevel = 53; maxLevel = 57; }
    PARAMETRIZE { region = NABLA_SAFARI_REGION_KANTO; champion = TRUE; minLevel = 68; maxLevel = 72; }
    PARAMETRIZE { region = NABLA_SAFARI_REGION_STARTERS; champion = TRUE; minLevel = 5; maxLevel = 5; }

    VarSet(VAR_NABLA_SAFARI_REGION, region);
    for (u32 i = 0; i < badges; i++)
        FlagSet(FLAG_BADGE01_GET + i);
    if (champion)
        FlagSet(FLAG_IS_CHAMPION);
    for (u32 i = 0; i < 20; i++)
    {
        u32 level = GetSafariZoneRegionWildLevel();
        EXPECT_GE(level, minLevel);
        EXPECT_LE(level, maxLevel);
    }
}

TEST("Nabla: Safari Zone special zones are sold after the League, for their own price")
{
    VarSet(VAR_0x8005, NABLA_SAFARI_REGION_PARADOX);
    EXPECT_EQ(NablaSafariZone_CountRegionsForSale(), 7);
    FlagSet(FLAG_IS_CHAMPION);
    EXPECT_EQ(NablaSafariZone_CountRegionsForSale(), 10);

    SetMoney(&gSaveBlock1Ptr->money, NABLA_SAFARI_SPECIAL_PRICE - 1);
    EXPECT_EQ(NablaSafariZone_TryBuyRegion(), FALSE);
    EXPECT(!FlagGet(FLAG_NABLA_SAFARI_PARADOX));

    SetMoney(&gSaveBlock1Ptr->money, NABLA_SAFARI_SPECIAL_PRICE + 1);
    EXPECT_EQ(NablaSafariZone_TryBuyRegion(), TRUE);
    EXPECT(FlagGet(FLAG_NABLA_SAFARI_PARADOX));
    EXPECT_EQ(GetMoney(&gSaveBlock1Ptr->money), 1);
    EXPECT_EQ(NablaSafariZone_CountRegionsForSale(), 9);
}
