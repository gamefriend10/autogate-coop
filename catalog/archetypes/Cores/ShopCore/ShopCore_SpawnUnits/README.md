(`GV_LengthOfUnitDataToSpawnArray`, `GV_UnitDataToSpawnArray`, `GV_NumOfUnitsToSpawnForEachUnitDataArray`) SetVarsForShopCoreSpawnUnits(`GV_ShopCoreToSpawn`):

Switch(`GV_ShopCoreToSpawn`):
  case HogDog_ShopCore: SetVarsFor_HogDog_ShopCore_SpawnUnits()
  repeat for all battle groups...

----------------------------------------

// Notes:
// - Both arrays must be equal length and the index of numOfUnits must correspond to unitData
ShopCore_SpawnUnits(
  `GV_LengthOfUnitDataToSpawnArray`,
  `GV_UnitDataToSpawnArray`,
  `GV_NumOfUnitsToSpawnForEachUnitDataArray`,
  `GV_PlayerToSpawnShopCoreFor`,
  `ShopPositionToSpawnAt`,
  `GV_ShopCoreToAttachUnitsTo`
):

// Iterate through `GV_UnitDataToSpawnArray`
General_ForEachInteger(`i`, 0, `GV_LengthOfUnitDataToSpawnArray`-1):
  // Spawn the corresponding number of units.
  Unit_CreateUnit(
    `GV_NumOfUnitsToSpawnForEachUnitDataArray`[`i`],
    `GV_UnitDataToSpawnArray`[`i`],
    `GV_PlayerToSpawnShopCoreFor`,
    `ShopPositionToSpawnAt`,
    true
  )
  // Add to local var `units_spawned`
  UnitGroup_AddUnits(`units_spawned`, UnitGroup_GetLastCreatedUnits())

// Add `units_spawned` to shopCore's blackboard `units`
Blackboard_SetValue_UnitGroup(
  Blackboard_GetBlackboardOfEntity(`GV_ShopCoreToAttachUnitsTo`),
  `units`,
  UnitGroup_CopyOfUnitGroup(`units_spawned`)
)