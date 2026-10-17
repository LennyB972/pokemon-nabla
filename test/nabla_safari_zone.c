#include "global.h"
#include "event_data.h"
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
