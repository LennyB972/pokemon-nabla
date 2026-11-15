#include "global.h"
#include "daycare.h"
#include "event_data.h"
#include "item.h"
#include "pokemon.h"
#include "test/overworld_script.h"
#include "test/test.h"

// The changes Nabla makes to Pokémon of the post-game (docs/nabla/postgame.md): Kubfu evolves at level 50 holding
// its scroll, Type: Null at level 50, and the lines of Kubfu and Cosmog breed.

TEST("Nabla: Kubfu evolves at level 50 holding its scroll, and Type: Null at level 50")
{
    struct Pokemon mon;
    bool32 canStopEvo;
    enum Species species = SPECIES_NONE, evolution = SPECIES_NONE;
    enum Item item = ITEM_NONE;
    u32 level = 50;

    PARAMETRIZE { species = SPECIES_KUBFU; item = ITEM_SCROLL_OF_DARKNESS; evolution = SPECIES_URSHIFU_SINGLE_STRIKE; }
    PARAMETRIZE { species = SPECIES_KUBFU; item = ITEM_SCROLL_OF_WATERS; evolution = SPECIES_URSHIFU_RAPID_STRIKE; }
    PARAMETRIZE { species = SPECIES_KUBFU; item = ITEM_SCROLL_OF_WATERS; level = 49; evolution = SPECIES_NONE; }
    PARAMETRIZE { species = SPECIES_KUBFU; evolution = SPECIES_NONE; }
    PARAMETRIZE { species = SPECIES_TYPE_NULL; evolution = SPECIES_SILVALLY_NORMAL; }
    PARAMETRIZE { species = SPECIES_TYPE_NULL; level = 49; evolution = SPECIES_NONE; }

    CreateMon(&mon, species, level, 0, OTID_STRUCT_PLAYER_ID);
    SetMonData(&mon, MON_DATA_HELD_ITEM, &item);
    EXPECT_EQ(GetEvolutionTargetSpecies(&mon, EVO_MODE_NORMAL, ITEM_NONE, NULL, &canStopEvo, CHECK_EVO), evolution);
}

TEST("Nabla: the scrolls can be held")
{
    EXPECT_EQ(GetItemPocket(ITEM_SCROLL_OF_DARKNESS), POCKET_ITEMS);
    EXPECT_EQ(GetItemPocket(ITEM_SCROLL_OF_WATERS), POCKET_ITEMS);
}

TEST("Nabla: the lines of Kubfu and Cosmog breed with Ditto, and their Eggs give Kubfu and Cosmog")
{
    enum Species parent = SPECIES_NONE, egg = SPECIES_NONE;

    PARAMETRIZE { parent = SPECIES_KUBFU; egg = SPECIES_KUBFU; }
    PARAMETRIZE { parent = SPECIES_URSHIFU_RAPID_STRIKE; egg = SPECIES_KUBFU; }
    PARAMETRIZE { parent = SPECIES_COSMOG; egg = SPECIES_COSMOG; }
    PARAMETRIZE { parent = SPECIES_LUNALA; egg = SPECIES_COSMOG; }

    ZeroPlayerPartyMons();
    VarSet(VAR_TEMP_C, parent);
    RUN_OVERWORLD_SCRIPT(
        givemon SPECIES_DITTO, 100; givemon VAR_TEMP_C, 100;
    );
    StorePokemonInDaycare(&gParties[B_TRAINER_PLAYER][0], &gSaveBlock1Ptr->daycare.mons[0]);
    StorePokemonInDaycare(&gParties[B_TRAINER_PLAYER][0], &gSaveBlock1Ptr->daycare.mons[1]);
    RUN_OVERWORLD_SCRIPT( special GiveEggFromDaycare; );
    EXPECT_EQ(GetMonData(&gParties[B_TRAINER_PLAYER][0], MON_DATA_SPECIES), egg);
}
