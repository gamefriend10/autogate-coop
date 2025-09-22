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

// Trigger: shopCore uses ability (expected to only be Buy, which morphs ShopCore into HandCore)
ShopToHandCoreTransitionTrigger():
  set `IV_MoveCoreToOwningPlayerHand_Core` = Unit_GetTriggeringUnit()
  MoveCoreToOwningPlayerHand(`IV_MoveCoreToOwningPlayerHand_Core`)

  // Remove this shopCore from the player's blackboard
  // Note: the player blackboard key to use should be saved to `shop_position_key` in this core's blackboard
  Blackboard_RemoveValue(
    Blackboard_GetBlackboardOfPlayer(),
    Blackboard_GetValue_String(
      Blackboard_GetBlackboardOfEntity(Unit_GetTriggeringUnit()),
      "shop_position_key"
    )
  )

  // Wait for 0.1 seconds, because at execution time, this is technically still a ShopCore. Morphing into HandCore
  // doesn't count as birth/constructed, so we can't execute this on the other end either, without reworking how
  // HandCore is created.
  set `trigger_unit_core_before_wait` = Unit_GetTriggeringUnit()
  General_Wait(0.1)
  set `IV_Triple_TriplifyCoreIfThreeArePresent_CoreToCheckFor` = `trigger_unit_core_before_wait`
  Triple_TriplifyCoreIfThreeArePresent(`IV_Triple_TriplifyCoreIfThreeArePresent_CoreToCheckFor`)