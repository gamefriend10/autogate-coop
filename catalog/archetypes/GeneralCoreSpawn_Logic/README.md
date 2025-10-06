// LONG if-then-else that determines which ShopCore BattleGroup to spawn
GeneralShopCoreSpawn(
  `GV_PlayerToSpawnShopCoreFor`,
  `ShopPositionToSpawnAt`,
  `BattleGroupToSpawnTag`,
  `ShopPositionKeyToSaveToBlackboard`
):
  // TODO: switch this over to switch case
  If(`BattleGroupToSpawnTag` == hogdog_snowtag):
    `GV_ShopCoreToSpawn` = HogDog_ShopCore
  If ... etc
  ShopCore_Spawn(`GV_ShopCoreToSpawn`, `GV_PlayerToSpawnShopCoreFor`, `ShopPositionToSpawnAt`, `ShopPositionKeyToSaveToBlackboard`)
