ShopCore_Spawn(
  `GV_ShopCoreToSpawn`,
  `GV_PlayerToSpawnShopCoreFor`,
  `ShopPositionToSpawnAt`,
  `ShopPositionKeyToSaveToBlackboard
):
  // Creates shop core
  Unit_CreateUnit(1, `GV_ShopCoreToSpawn`, `GV_PlayerToSpawnShopCoreFor`, `ShopPositionToSpawnAt`, true)
  `IV_Core_SpawnUnits_CoreToAttachUnitsTo` = Unit_GetLastCreatedUnit()

  // Assigns shop core to player's blackboard
  Blackboard_SetValue_Unit(
    Blackboard_GetBlackboardOfPlayer(`GV_PlayerToSpawnShopCoreFor`),
    `ShopPositionKeyToSaveToBlackboard`,
    Unit_GetLastCreatedUnit()
  )

  // Saves shop position to shop core's blackboard
  Blackboard_SetValue_String(
    Blackboard_GetBlackboardOfEntity(Unit_GetLastCreatedUnit()),
    "shop_position_key",
    `ShopPositionKeyToSaveToBlackboard`
  )

  // Set vars for this shop core to spawn its units
  `IV_Core_SpawnUnits_CoreToSpawn` = `GV_ShopCoreToSpawn`
  (`GV_LengthOfUnitDataToSpawnArray`, `GV_UnitDataToSpawnArray`, `GV_NumOfUnitsToSpawnForEachUnitDataArray`) =
    SetVarsForCoreSpawnUnits(`IV_Core_SpawnUnits_CoreToSpawn`)

  // Spawn corresponding units for the shop
  `IV_Core_SpawnUnits_PlayerToSpawnFor` = `GV_PlayerToSpawnShopCoreFor`
  Core_SpawnUnits(
    `GV_LengthOfUnitDataToSpawnArray`,
    `GV_UnitDataToSpawnArray`,
    `GV_NumOfUnitsToSpawnForEachUnitDataArray`,
    `IV_Core_SpawnUnits_PlayerToSpawnFor`,
    `IV_Core_SpawnUnits_CoreToAttachUnitsTo`
  )

----------------------------------------

ShopToHandCoreTransitionTrigger

Trigger: shopCore uses ability (expected to only be Buy, which morphs ShopCore into HandCore)

`IV_PickFirstOpenHandPositionForPlayer_Player` = Unit_GetOwningPlayer(Unit_GetTriggeringUnit())
`GV_OpenHandPositionToSpawnAt` = PickFirstOpenHandPositionForPlayer(`IV_PickFirstOpenHandPositionForPlayer_Player`)

SetHandCoreBlackboardHandPosition(`GV_OpenHandPositionToSpawnAt`)
`GV_HandPositionToSpawnAt` = GetVectorForHandPositionOfTriggeringPlayer(`GV_OpenHandPositionToSpawnAt`)
Set position to `GV_HandPositionToSpawnAt`
move shopCore's `units` (tracked by blackboard) to Actor's current position
Remove this shopCore from the player's blackboard
  (the player blackboard key to use should be saved to `shop_position_key` in this core's blackboard)

`IV_AddHandCoreToOpenHandPositionInPlayerBlackboard_Player` = Unit_GetOwningPlayer(Unit_GetTriggeringUnit())
AddHandCoreToOpenHandPositionInPlayerBlackboard(
  `GV_OpenHandPositionToSpawnAt`,
  `IV_AddHandCoreToOpenHandPositionInPlayerBlackboard_Player`
)
