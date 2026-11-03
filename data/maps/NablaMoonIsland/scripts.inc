NablaMoonIsland_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, NablaMoonIsland_OnTransition
	.byte 0

NablaMoonIsland_OnTransition:
	call Nabla_MoonIsland_EventScript_SetUp
	end
