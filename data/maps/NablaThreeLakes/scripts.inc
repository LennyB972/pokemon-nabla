NablaThreeLakes_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, NablaThreeLakes_OnTransition
	.byte 0

NablaThreeLakes_OnTransition:
	call Nabla_ThreeLakes_EventScript_SetUp
	end
