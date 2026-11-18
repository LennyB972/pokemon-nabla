#include "global.h"
#include "event_data.h"
#include "shop_criteria.h"
#include "test/test.h"

extern const u16 Nabla_Pokemart_Items[];

// Whether every Poké Mart (data/scripts/nabla/pokemart.inc) sells the item, with this many badges
// (src/shop_criteria.c)
static bool32 PokemartSells(enum Item item, u32 badges)
{
    const u16 *list = Nabla_Pokemart_Items;
    u16 total = 0;
    bool32 sold = FALSE;
    u32 i;

    for (i = 0; i < badges; i++)
        FlagSet(FLAG_BADGE01_GET + i);
    while (list[total] != ITEM_NONE)
        total++;
    TryBuildDynamicShopItemList(&list, &total);
    for (i = 0; i < total; i++)
    {
        if (list[i] == item)
            sold = TRUE;
    }
    TryFreeDynamicShopItemList(&list);
    for (i = 0; i < badges; i++)
        FlagClear(FLAG_BADGE01_GET + i);
    return sold;
}

TEST("Nabla: Poké Marts sell the Exp. Candies early, and no Mail but the Harbor Mail")
{
    enum Item item = ITEM_NONE;
    u32 badges = 0;

    PARAMETRIZE { item = ITEM_EXP_CANDY_XS; badges = 0; }
    PARAMETRIZE { item = ITEM_EXP_CANDY_S; badges = 0; }
    PARAMETRIZE { item = ITEM_EXP_CANDY_M; badges = 1; }
    PARAMETRIZE { item = ITEM_EXP_CANDY_L; badges = 3; }
    PARAMETRIZE { item = ITEM_HARBOR_MAIL; badges = 2; }

    EXPECT(PokemartSells(item, badges));
    if (badges > 0)
        EXPECT(!PokemartSells(item, badges - 1));
    EXPECT(!PokemartSells(ITEM_ORANGE_MAIL, NUM_BADGES));
    EXPECT(!PokemartSells(ITEM_WOOD_MAIL, NUM_BADGES));
    EXPECT(!PokemartSells(ITEM_SHADOW_MAIL, NUM_BADGES));
}
