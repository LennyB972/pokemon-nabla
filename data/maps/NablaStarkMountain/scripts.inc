NablaStarkMountain_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, NablaStarkMountain_OnTransition
	.byte 0

NablaStarkMountain_OnTransition:
	call Nabla_StarkMountain_EventScript_SetUp
	end
