#include "global.h"
#include "event_data.h"
#include "item.h"
#include "nabla_lab_assistant.h"
#include "pokemon.h"
#include "string_util.h"
#include "constants/items.h"
#include "constants/nabla.h"

// Pokémon Nabla: the assistant of Prof. Birch's lab after the League (data/scripts/nabla/lab_assistant.inc). The
// player shows him a Pokémon of the party (its slot in VAR_0x8004); he gives the items that go with it (its form
// items, its Mega Stone) that are not in the bag, so an item used up (a scroll) or held is given again. Keldeo and
// Meloetta remember their move (Secret Sword, Relic Song) with the Move Relearner instead.

static const u16 sRedOrb[] = {ITEM_RED_ORB};
static const u16 sBlueOrb[] = {ITEM_BLUE_ORB};
static const u16 sLatiasite[] = {ITEM_LATIASITE};
static const u16 sAdamantCrystal[] = {ITEM_ADAMANT_CRYSTAL};
static const u16 sLustrousGlobe[] = {ITEM_LUSTROUS_GLOBE};
static const u16 sGriseousCore[] = {ITEM_GRISEOUS_CORE};
static const u16 sGracidea[] = {ITEM_GRACIDEA};
static const u16 sPlates[] =
{
    ITEM_FLAME_PLATE, ITEM_SPLASH_PLATE, ITEM_ZAP_PLATE, ITEM_MEADOW_PLATE, ITEM_ICICLE_PLATE, ITEM_FIST_PLATE,
    ITEM_TOXIC_PLATE, ITEM_EARTH_PLATE, ITEM_SKY_PLATE, ITEM_MIND_PLATE, ITEM_INSECT_PLATE, ITEM_STONE_PLATE,
    ITEM_SPOOKY_PLATE, ITEM_DRACO_PLATE, ITEM_DREAD_PLATE, ITEM_IRON_PLATE, ITEM_PIXIE_PLATE,
};
static const u16 sRevealGlass[] = {ITEM_REVEAL_GLASS};
static const u16 sDnaSplicers[] = {ITEM_DNA_SPLICERS};
static const u16 sDrives[] = {ITEM_BURN_DRIVE, ITEM_CHILL_DRIVE, ITEM_DOUSE_DRIVE, ITEM_SHOCK_DRIVE};
static const u16 sZygardeCube[] = {ITEM_ZYGARDE_CUBE};
static const u16 sPrisonBottle[] = {ITEM_PRISON_BOTTLE};
static const u16 sMemories[] =
{
    ITEM_FIRE_MEMORY, ITEM_WATER_MEMORY, ITEM_ELECTRIC_MEMORY, ITEM_GRASS_MEMORY, ITEM_ICE_MEMORY,
    ITEM_FIGHTING_MEMORY, ITEM_POISON_MEMORY, ITEM_GROUND_MEMORY, ITEM_FLYING_MEMORY, ITEM_PSYCHIC_MEMORY,
    ITEM_BUG_MEMORY, ITEM_ROCK_MEMORY, ITEM_GHOST_MEMORY, ITEM_DRAGON_MEMORY, ITEM_DARK_MEMORY, ITEM_STEEL_MEMORY,
    ITEM_FAIRY_MEMORY,
};
static const u16 sNecrozmaItems[] = {ITEM_N_SOLARIZER, ITEM_N_LUNARIZER, ITEM_ULTRANECROZIUM_Z};
static const u16 sScrolls[] = {ITEM_SCROLL_OF_DARKNESS, ITEM_SCROLL_OF_WATERS};
static const u16 sRustedSword[] = {ITEM_RUSTED_SWORD};
static const u16 sRustedShield[] = {ITEM_RUSTED_SHIELD};
static const u16 sReinsOfUnity[] = {ITEM_REINS_OF_UNITY};
static const u16 sMasks[] = {ITEM_WELLSPRING_MASK, ITEM_HEARTHFLAME_MASK, ITEM_CORNERSTONE_MASK};

struct LabAssistantItems
{
    u16 species;
    u8 count;
    const u16 *items;
};

#define ITEMS(species, items) {species, ARRAY_COUNT(items), items}

static const struct LabAssistantItems sLabAssistantItems[] =
{
    ITEMS(SPECIES_GROUDON, sRedOrb),
    ITEMS(SPECIES_KYOGRE, sBlueOrb),
    ITEMS(SPECIES_LATIAS, sLatiasite),
    ITEMS(SPECIES_DIALGA, sAdamantCrystal),
    ITEMS(SPECIES_PALKIA, sLustrousGlobe),
    ITEMS(SPECIES_GIRATINA, sGriseousCore),
    ITEMS(SPECIES_SHAYMIN, sGracidea),
    ITEMS(SPECIES_ARCEUS, sPlates),
    ITEMS(SPECIES_TORNADUS, sRevealGlass),
    ITEMS(SPECIES_THUNDURUS, sRevealGlass),
    ITEMS(SPECIES_LANDORUS, sRevealGlass),
    ITEMS(SPECIES_ENAMORUS, sRevealGlass),
    ITEMS(SPECIES_KYUREM, sDnaSplicers),
    ITEMS(SPECIES_GENESECT, sDrives),
    ITEMS(SPECIES_ZYGARDE, sZygardeCube),
    ITEMS(SPECIES_HOOPA, sPrisonBottle),
    ITEMS(SPECIES_SILVALLY, sMemories),
    ITEMS(SPECIES_NECROZMA, sNecrozmaItems),
    ITEMS(SPECIES_KUBFU, sScrolls),
    ITEMS(SPECIES_ZACIAN, sRustedSword),
    ITEMS(SPECIES_ZAMAZENTA, sRustedShield),
    ITEMS(SPECIES_CALYREX, sReinsOfUnity),
    ITEMS(SPECIES_OGERPON, sMasks),
};

// The base species of the Pokémon shown (none for an Egg), its name in STR_VAR_1
static enum Species GetShownSpecies(void)
{
    enum Species species = GetMonData(&gParties[B_TRAINER_PLAYER][gSpecialVar_0x8004], MON_DATA_SPECIES_OR_EGG);

    StringCopy(gStringVar1, GetSpeciesName(species));
    return species == SPECIES_EGG ? SPECIES_NONE : GET_BASE_SPECIES_ID(species);
}

static const struct LabAssistantItems *GetShownItems(void)
{
    enum Species species = GetShownSpecies();

    for (u32 i = 0; species != SPECIES_NONE && i < ARRAY_COUNT(sLabAssistantItems); i++)
    {
        if (GET_BASE_SPECIES_ID(sLabAssistantItems[i].species) == species)
            return &sLabAssistantItems[i];
    }
    return NULL;
}

static u32 CountMissingItems(const struct LabAssistantItems *entry)
{
    u32 count = 0;

    for (u32 i = 0; i < entry->count; i++)
    {
        if (!CheckBagHasItem(entry->items[i], 1))
            count++;
    }
    return count;
}

// What the assistant does with the Pokémon shown (LAB_ASSISTANT_*, include/constants/nabla.h)
u16 NablaLabAssistant_Check(void)
{
    const struct LabAssistantItems *entry = GetShownItems();
    enum Species species = GetShownSpecies();
    u32 missing;

    if (species == GET_BASE_SPECIES_ID(SPECIES_KELDEO) || species == GET_BASE_SPECIES_ID(SPECIES_MELOETTA))
        return LAB_ASSISTANT_SECRET_MOVE;
    if (entry == NULL)
        return LAB_ASSISTANT_NOTHING;
    missing = CountMissingItems(entry);
    if (missing == 0)
        return LAB_ASSISTANT_HAS_ALL;
    return missing > LAB_ASSISTANT_ONE_BY_ONE ? LAB_ASSISTANT_MANY_ITEMS : LAB_ASSISTANT_ITEMS;
}

// The next item for the Pokémon shown that is not in the bag, given one by one; ITEM_NONE once there is none
u16 NablaLabAssistant_NextItem(void)
{
    const struct LabAssistantItems *entry = GetShownItems();

    for (u32 i = 0; entry != NULL && i < entry->count; i++)
    {
        if (!CheckBagHasItem(entry->items[i], 1))
            return entry->items[i];
    }
    return ITEM_NONE;
}

// Puts at once in the bag all the items for the Pokémon shown that are not in it (the Plates, the Memories), as
// long as there is room; returns how many, in STR_VAR_2 too
u16 NablaLabAssistant_GiveAllItems(void)
{
    const struct LabAssistantItems *entry = GetShownItems();
    u32 count = 0;

    for (u32 i = 0; entry != NULL && i < entry->count; i++)
    {
        if (!CheckBagHasItem(entry->items[i], 1) && AddBagItem(entry->items[i], 1))
            count++;
    }
    ConvertIntToDecimalStringN(gStringVar2, count, STR_CONV_MODE_LEFT_ALIGN, 2);
    return count;
}
