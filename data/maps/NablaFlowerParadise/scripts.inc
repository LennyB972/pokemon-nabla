NablaFlowerParadise_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, NablaFlowerParadise_OnTransition
	.byte 0

NablaFlowerParadise_OnTransition:
	call Nabla_FlowerParadise_EventScript_SetUp
	end
