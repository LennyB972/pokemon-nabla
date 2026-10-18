#include "global.h"
#include "item.h"
#include "script.h"
#include "event_data.h"
#include "malloc.h"
#include "shop_criteria.h"

static EWRAM_DATA const u16 *sDynamicShopItemListRef = NULL;

// Remove the UNUSED if you'll use the functions!
static bool32 ShopCriteriaByBadgeCount(u32 count);
static bool32 HasShopItemRequirements(enum Item item);
static UNUSED bool32 ShopCriteriaByFlag(u32 flagId);
static UNUSED bool32 ShopCriteriaByVar(u32 varId, u32 varValue);

void TryBuildDynamicShopItemList(const u16 **ogItemList, u16 *resultingTotal)
{
    sDynamicShopItemListRef = *ogItemList;

    u16 *list = AllocZeroed((*resultingTotal + 1) * sizeof(u16));
    u32 overallIdx = 0, idx = 0;

    while (idx < *resultingTotal)
    {
        enum Item item = sDynamicShopItemListRef[idx];

        if (IsItemShopCriteriaFulfilled(item) && HasShopItemRequirements(item))
        {
            list[overallIdx] = item;
            overallIdx++;
        }

        idx++;
    }

    list[overallIdx] = ITEM_NONE;

    *ogItemList = list;
    *resultingTotal = overallIdx;
}

void TryFreeDynamicShopItemList(const u16 **ogItemList)
{
    Free((u16 *)*ogItemList);
    *ogItemList = sDynamicShopItemListRef;
}

// Add new Criterias below!

// Pokémon Nabla: what the player needs before shops sell these items (any item not listed is always sold).
// Shared by every Poké Mart, so a new badge unlocks items everywhere, as in recent games.
static const struct
{
    enum Item item;
    u8 badges;
    u16 flag; // 0 if none
} sShopItemRequirements[] =
{
    { ITEM_POKE_BALL,     0, FLAG_ADVENTURE_STARTED },
    { ITEM_TIMER_BALL,    1 },
    { ITEM_REPEAT_BALL,   1 },
    { ITEM_GREAT_BALL,    2 },
    { ITEM_X_ACCURACY,    2 },
    { ITEM_DIRE_HIT,      2 },
    { ITEM_GUARD_SPEC,    2 },
    { ITEM_EXP_CANDY_S,   2 },
    { ITEM_HARBOR_MAIL,   2 },
    { ITEM_NEST_BALL,     3 },
    { ITEM_REVIVE,        3 },
    { ITEM_BURN_HEAL,     3 },
    { ITEM_ICE_HEAL,      3 },
    { ITEM_FLUFFY_TAIL,   3 },
    { ITEM_SUPER_REPEL,   3 },
    { ITEM_X_SP_ATK,      3 },
    { ITEM_LINKING_CORD,  3 },
    { ITEM_EXP_CANDY_M,   4 },
    { ITEM_ULTRA_BALL,    5 },
    { ITEM_HYPER_POTION,  5 },
    { ITEM_WOOD_MAIL,     5 },
    { ITEM_NET_BALL,      6 },
    { ITEM_DIVE_BALL,     6 },
    { ITEM_FULL_HEAL,     6 },
    { ITEM_MAX_REPEL,     6 },
    { ITEM_EXP_CANDY_L,   6 },
    { ITEM_MAX_POTION,    7 },
    { ITEM_SHADOW_MAIL,   7 },
    { ITEM_BEAST_BALL,    0, FLAG_IS_CHAMPION },
};

static bool32 HasShopItemRequirements(enum Item item)
{
    for (u32 i = 0; i < ARRAY_COUNT(sShopItemRequirements); i++)
    {
        if (sShopItemRequirements[i].item == item)
            return ShopCriteriaByBadgeCount(sShopItemRequirements[i].badges)
                && (sShopItemRequirements[i].flag == 0 || FlagGet(sShopItemRequirements[i].flag));
    }
    return TRUE;
}

static bool32 ShopCriteriaByBadgeCount(u32 count)
{
    u32 badgeCount = 0;

    for (u32 badgeFlag = FLAG_BADGE01_GET; badgeFlag < FLAG_BADGE01_GET + NUM_BADGES; badgeFlag++)
    {
        if (FlagGet(badgeFlag))
            badgeCount++;
    }

    if (badgeCount >= count)
        return TRUE;

    return FALSE;
}

// These two below are somewhat identical to ShopCriteriaByBadgeCount
// but uses only one specific event var/flag check. Useful if you need
// a specific badge flag instead of just the badge total.

static UNUSED bool32 ShopCriteriaByFlag(u32 flagId)
{
    if (FlagGet(flagId))
        return TRUE;

    return FALSE;
}

static UNUSED bool32 ShopCriteriaByVar(u32 varId, u32 varValue)
{
    if (VarGet(varId) >= varValue)
        return TRUE;

    return FALSE;
}
