#include "global.h"
#include "event_data.h"
#include "item.h"
#include "nabla_lab_assistant.h"
#include "pokemon.h"
#include "test/test.h"
#include "constants/nabla.h"

// The lab assistant (src/nabla_lab_assistant.c), shown the Pokémon in the first slot of the party
static void ShowPokemon(enum Species species)
{
    ZeroPlayerPartyMons();
    CreateMon(&gParties[B_TRAINER_PLAYER][0], species, 80, 0, OTID_STRUCT_PLAYER_ID);
    gSpecialVar_0x8004 = 0;
}

// Gives what the script gives (one by one, or at once), as many items as it gives
static u32 GiveItems(void)
{
    u32 count = 0;
    u16 item;

    if (NablaLabAssistant_Check() == LAB_ASSISTANT_MANY_ITEMS)
        return NablaLabAssistant_GiveAllItems();
    while ((item = NablaLabAssistant_NextItem()) != ITEM_NONE && count < 32)
    {
        AddBagItem(item, 1);
        count++;
    }
    return count;
}

TEST("Nabla: the lab assistant gives the items that go with a legendary Pokémon, once")
{
    enum Species species = SPECIES_NONE;
    u32 check = 0, count = 0;
    enum Item item = ITEM_NONE;

    PARAMETRIZE { species = SPECIES_ARCEUS; check = LAB_ASSISTANT_MANY_ITEMS; count = 17; item = ITEM_PIXIE_PLATE; }
    PARAMETRIZE { species = SPECIES_SILVALLY_FIRE; check = LAB_ASSISTANT_MANY_ITEMS; count = 17; item = ITEM_DARK_MEMORY; }
    PARAMETRIZE { species = SPECIES_GENESECT; check = LAB_ASSISTANT_ITEMS; count = 4; item = ITEM_SHOCK_DRIVE; }
    PARAMETRIZE { species = SPECIES_NECROZMA_DUSK_MANE; check = LAB_ASSISTANT_ITEMS; count = 3; item = ITEM_ULTRANECROZIUM_Z; }
    PARAMETRIZE { species = SPECIES_OGERPON_WELLSPRING; check = LAB_ASSISTANT_ITEMS; count = 3; item = ITEM_CORNERSTONE_MASK; }
    PARAMETRIZE { species = SPECIES_GIRATINA_ORIGIN; check = LAB_ASSISTANT_ITEMS; count = 1; item = ITEM_GRISEOUS_CORE; }
    PARAMETRIZE { species = SPECIES_KYUREM_BLACK; check = LAB_ASSISTANT_ITEMS; count = 1; item = ITEM_DNA_SPLICERS; }
    PARAMETRIZE { species = SPECIES_CALYREX_ICE; check = LAB_ASSISTANT_ITEMS; count = 1; item = ITEM_REINS_OF_UNITY; }
    PARAMETRIZE { species = SPECIES_ENAMORUS; check = LAB_ASSISTANT_ITEMS; count = 1; item = ITEM_REVEAL_GLASS; }
    PARAMETRIZE { species = SPECIES_ZYGARDE_10; check = LAB_ASSISTANT_ITEMS; count = 1; item = ITEM_ZYGARDE_CUBE; }
    PARAMETRIZE { species = SPECIES_GROUDON; check = LAB_ASSISTANT_ITEMS; count = 1; item = ITEM_RED_ORB; }
    PARAMETRIZE { species = SPECIES_LATIAS; check = LAB_ASSISTANT_ITEMS; count = 1; item = ITEM_LATIASITE; }
    PARAMETRIZE { species = SPECIES_ZACIAN; check = LAB_ASSISTANT_ITEMS; count = 1; item = ITEM_RUSTED_SWORD; }
    PARAMETRIZE { species = SPECIES_KUBFU; check = LAB_ASSISTANT_ITEMS; count = 2; item = ITEM_SCROLL_OF_WATERS; }

    ClearBag();
    ShowPokemon(species);
    EXPECT_EQ(NablaLabAssistant_Check(), check);
    EXPECT_EQ(GiveItems(), count);
    EXPECT(CheckBagHasItem(item, 1));
    EXPECT_EQ(NablaLabAssistant_Check(), LAB_ASSISTANT_HAS_ALL);
    EXPECT_EQ(GiveItems(), 0);
}

TEST("Nabla: the lab assistant gives again an item that is no longer in the bag")
{
    ClearBag();
    ShowPokemon(SPECIES_KUBFU);
    GiveItems();
    RemoveBagItem(ITEM_SCROLL_OF_DARKNESS, 1);  // used up by the evolution of another Kubfu
    EXPECT_EQ(NablaLabAssistant_Check(), LAB_ASSISTANT_ITEMS);
    EXPECT_EQ(NablaLabAssistant_NextItem(), ITEM_SCROLL_OF_DARKNESS);
}

TEST("Nabla: the lab assistant has nothing for ordinary Pokémon, and the Move Relearner for Keldeo and Meloetta")
{
    enum Species species = SPECIES_NONE;
    u32 check = 0;

    PARAMETRIZE { species = SPECIES_WOBBUFFET; check = LAB_ASSISTANT_NOTHING; }
    PARAMETRIZE { species = SPECIES_RAYQUAZA; check = LAB_ASSISTANT_NOTHING; }
    PARAMETRIZE { species = SPECIES_KELDEO_RESOLUTE; check = LAB_ASSISTANT_SECRET_MOVE; }
    PARAMETRIZE { species = SPECIES_MELOETTA; check = LAB_ASSISTANT_SECRET_MOVE; }

    ClearBag();
    ShowPokemon(species);
    EXPECT_EQ(NablaLabAssistant_Check(), check);
    EXPECT_EQ(NablaLabAssistant_NextItem(), ITEM_NONE);
}

TEST("Nabla: the lab assistant has nothing for an Egg")
{
    bool8 isEgg = TRUE;

    ClearBag();
    ShowPokemon(SPECIES_ARCEUS);
    SetMonData(&gParties[B_TRAINER_PLAYER][0], MON_DATA_IS_EGG, &isEgg);
    EXPECT_EQ(NablaLabAssistant_Check(), LAB_ASSISTANT_NOTHING);
}
