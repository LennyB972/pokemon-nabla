#include "global.h"
#include "event_data.h"
#include "item.h"
#include "party_menu.h"
#include "pokemon.h"
#include "test/test.h"

TEST("Nabla: an item can be used at once as many times in a row as it has an effect")
{
    struct Pokemon *mon = &gParties[B_TRAINER_PLAYER][0];
    enum Item item = ITEM_NONE;
    u32 quantity = 10, expected = 0, hpLost = 0, hpEv = 0, status = STATUS1_NONE, level = 50, levelCaps = FALSE;
    void (*callback)(u8, TaskFunc) = ItemUseCB_Medicine;

    PARAMETRIZE { item = ITEM_POTION; hpLost = 50; expected = 3; }
    PARAMETRIZE { item = ITEM_POTION; hpLost = 50; quantity = 2; expected = 2; }
    PARAMETRIZE { item = ITEM_POTION; hpLost = 0; expected = 0; }
    PARAMETRIZE { item = ITEM_HP_UP; hpEv = 232; expected = 2; }
    PARAMETRIZE { item = ITEM_FULL_HEAL; status = STATUS1_POISON; expected = 1; }
    PARAMETRIZE { item = ITEM_RARE_CANDY; callback = ItemUseCB_RareCandy; level = 95; expected = 5; }
    PARAMETRIZE { item = ITEM_RARE_CANDY; callback = ItemUseCB_RareCandy; level = 14; levelCaps = TRUE; expected = 2; }

    if (levelCaps)
        FlagSet(FLAG_NABLA_LEVEL_CAPS);
    CreateMon(mon, SPECIES_WOBBUFFET, level, 0, OTID_STRUCT_PLAYER_ID);
    SetMonData(mon, MON_DATA_HP_EV, &hpEv);
    CalculateMonStats(mon);
    u32 hp = GetMonData(mon, MON_DATA_MAX_HP) - hpLost;
    SetMonData(mon, MON_DATA_HP, &hp);
    SetMonData(mon, MON_DATA_STATUS, &status);
    ClearBag();
    AddBagItem(item, quantity);
    gPartyMenu.menuType = PARTY_MENU_TYPE_FIELD;
    gPartyMenu.slotId = 0;
    gItemUseCB = callback;

    EXPECT_EQ(GetItemUseMaxQuantity(mon, item), expected);
}
