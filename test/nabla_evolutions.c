#include "global.h"
#include "pokemon.h"
#include "test/test.h"

TEST("Nabla: Feebas evolves into Milotic at level 20, whatever its beauty")
{
    struct Pokemon mon;
    bool32 canStopEvo;
    enum Species evolution = SPECIES_NONE;
    u32 level = 0;

    PARAMETRIZE { level = 19; evolution = SPECIES_NONE; }
    PARAMETRIZE { level = 20; evolution = SPECIES_MILOTIC; }

    CreateMon(&mon, SPECIES_FEEBAS, level, 0, OTID_STRUCT_PLAYER_ID);
    EXPECT_EQ(GetEvolutionTargetSpecies(&mon, EVO_MODE_NORMAL, ITEM_NONE, NULL, &canStopEvo, CHECK_EVO), evolution);
}
