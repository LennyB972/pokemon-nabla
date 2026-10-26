#include "global.h"
#include "event_data.h"
#include "event_object_movement.h"
#include "item_menu.h"
#include "nabla_rayquaza_event.h"
#include "pokemon.h"
#include "pokemon_storage_system.h"
#include "constants/items.h"

// Pokémon Nabla: the Sky Pillar event (data/scripts/nabla/rayquaza_event.inc).

// The Rayquaza caught at the top of Sky Pillar joins the party at its head; it is the only Rayquaza the
// player can have at this point. FALSE if it went to the PC.
bool8 NablaRayquazaEvent_PutRayquazaFirst(void)
{
    for (u32 i = 0; i < PARTY_SIZE; i++)
    {
        if (GetMonData(&gParties[B_TRAINER_PLAYER][i], MON_DATA_SPECIES_OR_EGG) == SPECIES_RAYQUAZA)
        {
            struct Pokemon rayquaza = gParties[B_TRAINER_PLAYER][i];

            for (; i > 0; i--)
                gParties[B_TRAINER_PLAYER][i] = gParties[B_TRAINER_PLAYER][i - 1];
            gParties[B_TRAINER_PLAYER][0] = rayquaza;
            UpdateFollowingPokemon();
            return TRUE;
        }
    }
    return FALSE;
}

// With a full party, Rayquaza comes from the PC in place of the Pokémon chosen in the party (VAR_0x8004)
void NablaRayquazaEvent_SwapRayquazaIntoParty(void)
{
    struct Pokemon *mon = &gParties[B_TRAINER_PLAYER][gSpecialVar_0x8004];

    for (u32 box = 0; box < TOTAL_BOXES_COUNT; box++)
    {
        for (u32 pos = 0; pos < IN_BOX_COUNT; pos++)
        {
            struct BoxPokemon *boxMon = GetBoxedMonPtr(box, pos);

            if (GetBoxMonData(boxMon, MON_DATA_SPECIES_OR_EGG) == SPECIES_RAYQUAZA)
            {
                struct BoxPokemon sentToPC = mon->box;

                BoxMonToMon(boxMon, mon);
                SetBoxMonAt(box, pos, &sentToPC);
                NablaRayquazaEvent_PutRayquazaFirst();
                return;
            }
        }
    }
}

// The white rock of Mossdeep City changes the form of a Pokémon as a METEORITE does (Deoxys), since
// Rayquaza ate the player's METEORITE

static bool32 TryWhiteRockFormChange(struct Pokemon *mon)
{
    gSpecialVar_ItemId = ITEM_METEORITE;
    return TryFormChange(mon, FORM_CHANGE_ITEM_USE, B_TRAINER_PLAYER);
}

bool8 NablaWhiteRock_HasFormChangeMon(void)
{
    for (u32 i = 0; i < PARTY_SIZE; i++)
    {
        struct Pokemon mon = gParties[B_TRAINER_PLAYER][i];

        if (TryWhiteRockFormChange(&mon))
            return TRUE;
    }
    return FALSE;
}

// The Pokémon chosen in the party (VAR_0x8004)
bool8 NablaWhiteRock_TryFormChange(void)
{
    return TryWhiteRockFormChange(&gParties[B_TRAINER_PLAYER][gSpecialVar_0x8004]);
}
