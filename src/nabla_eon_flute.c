#include "global.h"
#include "event_data.h"
#include "field_screen_effect.h"
#include "nabla_eon_flute.h"
#include "overworld.h"
#include "pokemon.h"
#include "rtc.h"
#include "constants/region_map_sections.h"

// Pokémon Nabla: the Eon Flute (data/scripts/nabla/eon_flute.inc). Latios takes the player to the places
// where legendary Pokémon live, then back to where they were (kept in the dynamic warp of the save).

static const mapsec_u8_t sEonFluteDestinations[] =
{
    MAPSEC_FARAWAY_ISLAND,
    MAPSEC_NAVEL_ROCK,
    MAPSEC_BIRTH_ISLAND,
    MAPSEC_NABLA_BIRD_ISLET,
    MAPSEC_NABLA_MOON_ISLAND,
    MAPSEC_NABLA_LIBERTY_ISLAND,
    MAPSEC_NABLA_TAPU_ISLANDS,
    MAPSEC_NABLA_CERULEAN_CAVE,
    MAPSEC_NABLA_BURNED_TOWER,
    MAPSEC_NABLA_THREE_LAKES,
    MAPSEC_NABLA_SPEAR_PILLAR,
    MAPSEC_NABLA_STARK_MOUNTAIN,
};

bool8 NablaEonFlute_IsAtDestination(void)
{
    for (u32 i = 0; i < ARRAY_COUNT(sEonFluteDestinations); i++)
    {
        if (gMapHeader.regionMapSectionId == sEonFluteDestinations[i])
            return TRUE;
    }
    return FALSE;
}

void NablaEonFlute_SaveReturnPoint(void)
{
    SetDynamicWarpWithCoords(0, gSaveBlock1Ptr->location.mapGroup, gSaveBlock1Ptr->location.mapNum, WARP_ID_NONE,
                             gSaveBlock1Ptr->pos.x, gSaveBlock1Ptr->pos.y);
}

void NablaEonFlute_WarpBack(void)
{
    SetWarpDestinationToDynamicWarp(0);
    DoWarp();
    ResetInitialPlayerAvatarState();
}

// The legendary Pokémon of some mirages change at night (data/scripts/nabla/mirages.inc)
bool8 NablaMirage_IsNight(void)
{
    return GetTimeOfDay() == TIME_NIGHT;
}

// A Pokémon hidden in a mirage shows up at its altar when the player has the Pokémon it asks for in their party
// (data/scripts/nabla/mirages.inc): TRUE if the party has the species in VAR_0x8004, in any of its forms
bool8 NablaMirage_PartyHasSpecies(void)
{
    enum Species species = GET_BASE_SPECIES_ID(gSpecialVar_0x8004);

    for (u32 i = 0; i < CalculatePlayerPartyCount(); i++)
    {
        if (!GetMonData(&gParties[B_TRAINER_PLAYER][i], MON_DATA_IS_EGG)
         && GET_BASE_SPECIES_ID(GetMonData(&gParties[B_TRAINER_PLAYER][i], MON_DATA_SPECIES)) == species)
            return TRUE;
    }
    return FALSE;
}
