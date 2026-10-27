NablaEmeraldForest_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, NablaEmeraldForest_OnTransition
	.byte 0

NablaEmeraldForest_OnTransition:
	call Nabla_EmeraldForest_EventScript_SetUp
	end
