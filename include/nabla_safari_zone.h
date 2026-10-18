#ifndef GUARD_NABLA_SAFARI_ZONE_H
#define GUARD_NABLA_SAFARI_ZONE_H

#include "constants/regions.h"

bool32 InSafariZoneRegion(void);
u8 GetSafariZoneRegionWildLevel(void);
bool32 IsPlayerInEvolutionRegion(enum Region region);
void NablaSafariZone_PushRegions(void);
u16 NablaSafariZone_CountRegionsForSale(void);
u16 NablaSafariZone_TryBuyRegion(void);
void NablaSafariZone_BufferRegionName(void);

#endif // GUARD_NABLA_SAFARI_ZONE_H
