# Core_SpawnUnits

// Returns (`GV_LengthOfUnitDataToSpawnArray`, `GV_UnitDataToSpawnArray`, `GV_NumOfUnitsToSpawnForEachUnitDataArray`) SetVarsForCoreSpawnUnits(`IV_Core_SpawnUnits_CoreToSpawn`):
  Switch(`IV_Core_SpawnUnits_CoreToSpawn`):
    case HogDog_ShopCore: SetVarsFor_HogDog_ShopCore_SpawnUnits()
    repeat for all battle groups...

----------------------------------------

// Notes:
// - Both arrays must be equal length and the index of numOfUnits must correspond to unitData
Core_SpawnUnits(
  `GV_LengthOfUnitDataToSpawnArray`,
  `GV_UnitDataToSpawnArray`,
  `GV_NumOfUnitsToSpawnForEachUnitDataArray`,
  `IV_Core_SpawnUnits_PlayerToSpawnFor`,
  `IV_Core_SpawnUnits_CoreToAttachUnitsTo`
):
  // Iterate through `GV_UnitDataToSpawnArray`
  General_ForEachInteger(`i`, 0, `GV_LengthOfUnitDataToSpawnArray`-1):
    // Spawn the corresponding number of units.
    Unit_CreateUnit(
      `GV_NumOfUnitsToSpawnForEachUnitDataArray`[`i`],
      `GV_UnitDataToSpawnArray`[`i`],
      `IV_Core_SpawnUnits_PlayerToSpawnFor`,
      Actor_GetPosition(`IV_Core_SpawnUnits_CoreToAttachUnitsTo`),
      true
    )
    // Add to local var `units_spawned`
    UnitGroup_AddUnits(`units_spawned`, UnitGroup_GetLastCreatedUnits())

  // Add `units_spawned` to shopCore's blackboard `units`
  Blackboard_SetValue_UnitGroup(
    Blackboard_GetBlackboardOfEntity(`IV_Core_SpawnUnits_CoreToAttachUnitsTo`),
    `units`,
    UnitGroup_CopyOfUnitGroup(`units_spawned`)
  )