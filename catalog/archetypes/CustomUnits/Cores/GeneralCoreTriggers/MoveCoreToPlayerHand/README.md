// Requires an open hand position. Does not check for this.
MoveCoreToOwningPlayerHand(Unit `IV_MoveCoreToOwningPlayerHand_Core`):
  set `player` = Unit_GetOwningPlayer(`IV_MoveCoreToOwningPlayerHand_Core`)

  // Get open hand position
  `IV_PickFirstOpenHandPositionForPlayer_Player` = `player`
  `GV_OpenHandPositionToSpawnAt` = PickFirstOpenHandPositionForPlayer(`IV_PickFirstOpenHandPositionForPlayer_Player`)
  `GV_HandPositionToSpawnAt` = GetVectorForHandPositionOfTriggeringPlayer(`GV_OpenHandPositionToSpawnAt`)

  // Set position of core to that open position
  Blackboard_SetValue_String(
    Blackboard_GetBlackboardOfEntity(`IV_MoveCoreToOwningPlayerHand_Core`),
    "hand_position",
    `GV_OpenHandPositionToSpawnAt`
  )
  Actor_SetPosition(`IV_MoveCoreToOwningPlayerHand_Core`, `GV_HandPositionToSpawnAt`)

  // Set position of core's `units` (tracked by blackboard) to that open position
  UnitGroup_ForEachUnitInGroup(
    Blackboard_GetValue_UnitGroup(
      Blackboard_GetBlackboardOfEntity(`IV_MoveCoreToOwningPlayerHand_Core`),
      "units"
    )
  ):
    Actor_SetPosition(UnitGroup_GetCurrentUnit(), `GV_HandPositionToSpawnAt`)

  // Add core to player's blackboard
  `IV_AddHandCoreToOpenHandPositionInPlayerBlackboard_Player` = `player`
  AddHandCoreToOpenHandPositionInPlayerBlackboard(
    `GV_OpenHandPositionToSpawnAt`,
    `IV_AddHandCoreToOpenHandPositionInPlayerBlackboard_Player`
  )