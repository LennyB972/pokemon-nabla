NablaBirdIslet_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, NablaBirdIslet_OnTransition
	.byte 0

NablaBirdIslet_OnTransition:
	call Nabla_BirdIslet_EventScript_SetUp
	end
