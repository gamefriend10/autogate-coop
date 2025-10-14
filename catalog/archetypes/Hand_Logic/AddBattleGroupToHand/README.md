// Note: assumes open spot
// Returns: Unit `OV_AddBattleGroupToHand_HandCore`
AddBattleGroupToHand(
  UnitData `IV_AddBattleGroupToHand_HandCoreType`,
  Player `IV_AddBattleGroupToHand_Player`
):
  Set `IV_PickFirstOpenHandPositionForPlayer_Player` = `IV_AddBattleGroupToHand_Player`
  `GV_OpenHandPositionToSpawnAt` = PickFirstOpenHandPositionForPlayer(`IV_PickFirstOpenHandPositionForPlayer_Player`)
  `GV_HandPositionToSpawnAt` = GetVectorForHandPositionOfTriggeringPlayer(`GV_OpenHandPositionToSpawnAt`)

  Unit_CreateUnit(
    1,
    `IV_AddBattleGroupToHand_HandCoreType`,
    `IV_AddBattleGroupToHand_Player`,
    `GV_HandPositionToSpawnAt`,
    true
  )
  Set `OV_AddBattleGroupToHand_HandCore` = Unit_GetLastCreatedUnit()

  // Save to HandCore's Blackboard its own index position in the hand
  Blackboard_SetValue_String(
    Blackboard_GetBlackboardOfEntity(`OV_AddBattleGroupToHand_HandCore`),
    "hand_position",
    `GV_OpenHandPositionToSpawnAt`
  )

  Set `IV_AddHandCoreToOpenHandPositionInPlayerBlackboard_HandCore` = `OV_AddBattleGroupToHand_HandCore`
  Set `IV_AddHandCoreToOpenHandPositionInPlayerBlackboard_Player` = `IV_AddBattleGroupToHand_Player`
  AddHandCoreToOpenHandPositionInPlayerBlackboard(
    `IV_AddHandCoreToOpenHandPositionInPlayerBlackboard_HandCore`,
    `GV_OpenHandPositionToSpawnAt`,
    `IV_AddHandCoreToOpenHandPositionInPlayerBlackboard_Player`
  )

  Set `IV_Core_SpawnUnits_CoreToSpawn` = `IV_AddBattleGroupToHand_HandCoreType`
  (`GV_LengthOfUnitDataToSpawnArray`, `GV_UnitDataToSpawnArray`, `GV_NumOfUnitsToSpawnForEachUnitDataArray`) = 
    SetVarsForCoreSpawnUnits(`IV_Core_SpawnUnits_CoreToSpawn`)
  Set `IV_Core_SpawnUnits_PlayerToSpawnFor` = `IV_AddBattleGroupToHand_Player`
  Set `IV_Core_SpawnUnits_CoreToAttachUnitsTo` = `OV_AddBattleGroupToHand_HandCore`
  Core_SpawnUnits(
    `GV_LengthOfUnitDataToSpawnArray`,
    `GV_UnitDataToSpawnArray`,
    `GV_NumOfUnitsToSpawnForEachUnitDataArray`,
    `IV_Core_SpawnUnits_PlayerToSpawnFor`,
    `IV_Core_SpawnUnits_CoreToAttachUnitsTo`
  )