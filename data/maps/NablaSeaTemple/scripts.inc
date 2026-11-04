NablaSeaTemple_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, NablaSeaTemple_OnTransition
	.byte 0

NablaSeaTemple_OnTransition:
	call Nabla_SeaTemple_EventScript_SetUp
	end
