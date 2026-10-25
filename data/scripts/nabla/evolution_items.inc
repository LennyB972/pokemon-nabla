@ Clerks selling the evolution items (Lilycove Department Store 3F, Slateport market): stones, items
@ that replace trade evolutions, and items of later regions (see docs/nabla/couverture.md).
Nabla_EventScript_EvolutionItemsClerk::
	lock
	faceplayer
	message Nabla_Text_EvolutionItemsClerk
	waitmessage
	pokemart Nabla_Pokemart_EvolutionItems
	msgbox gText_PleaseComeAgain, MSGBOX_DEFAULT
	release
	end

	.align 2
Nabla_Pokemart_EvolutionItems:
	.2byte ITEM_FIRE_STONE
	.2byte ITEM_WATER_STONE
	.2byte ITEM_THUNDER_STONE
	.2byte ITEM_LEAF_STONE
	.2byte ITEM_MOON_STONE
	.2byte ITEM_SUN_STONE
	.2byte ITEM_DAWN_STONE
	.2byte ITEM_DUSK_STONE
	.2byte ITEM_SHINY_STONE
	.2byte ITEM_ICE_STONE
	.2byte ITEM_LINKING_CORD
	.2byte ITEM_KINGS_ROCK
	.2byte ITEM_METAL_COAT
	.2byte ITEM_DRAGON_SCALE
	.2byte ITEM_UPGRADE
	.2byte ITEM_DUBIOUS_DISC
	.2byte ITEM_PROTECTOR
	.2byte ITEM_ELECTIRIZER
	.2byte ITEM_MAGMARIZER
	.2byte ITEM_REAPER_CLOTH
	.2byte ITEM_DEEP_SEA_TOOTH
	.2byte ITEM_DEEP_SEA_SCALE
	.2byte ITEM_PRISM_SCALE
	.2byte ITEM_SACHET
	.2byte ITEM_WHIPPED_DREAM
	.2byte ITEM_STRAWBERRY_SWEET
	.2byte ITEM_LOVE_SWEET
	.2byte ITEM_BERRY_SWEET
	.2byte ITEM_CLOVER_SWEET
	.2byte ITEM_FLOWER_SWEET
	.2byte ITEM_STAR_SWEET
	.2byte ITEM_RIBBON_SWEET
	.2byte ITEM_GALARICA_CUFF
	.2byte ITEM_GALARICA_WREATH
	.2byte ITEM_TART_APPLE
	.2byte ITEM_SWEET_APPLE
	.2byte ITEM_SYRUPY_APPLE
	.2byte ITEM_CRACKED_POT
	.2byte ITEM_UNREMARKABLE_TEACUP
	.2byte ITEM_AUSPICIOUS_ARMOR
	.2byte ITEM_MALICIOUS_ARMOR
	.2byte ITEM_BLACK_AUGURITE
	.2byte ITEM_PEAT_BLOCK
	.2byte ITEM_METAL_ALLOY
	.2byte ITEM_GIMMIGHOUL_COIN
	pokemartlistend
