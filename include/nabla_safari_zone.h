#ifndef GUARD_NABLA_SAFARI_ZONE_H
#define GUARD_NABLA_SAFARI_ZONE_H

#include "constants/regions.h"

bool32 InSafariZoneRegion(void);
bool32 IsPlayerInEvolutionRegion(enum Region region);
void NablaSafariZone_PushRegions(void);
u16 NablaSafariZone_CountLockedRegions(void);
void NablaSafariZone_UnlockRegion(void);
void NablaSafariZone_BufferRegionName(void);

#endif // GUARD_NABLA_SAFARI_ZONE_H
