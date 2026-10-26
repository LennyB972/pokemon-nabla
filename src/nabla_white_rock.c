#include "global.h"
#include "event_data.h"
#include "item_menu.h"
#include "nabla_white_rock.h"
#include "pokemon.h"
#include "constants/items.h"

// Pokémon Nabla: the white rock of Mossdeep City changes the form of a Pokémon as a METEORITE does (Deoxys),
// since Rayquaza ate the player's METEORITE at the top of Sky Pillar (data/scripts/nabla/rayquaza_event.inc).

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
