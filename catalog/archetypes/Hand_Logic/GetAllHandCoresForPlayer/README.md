// Returns UnitGroup `OV_GetAllHandCoresForPlayer_HandCoreUnitGroup`
GetAllHandCoresForPlayer(Player `IV_GetAllHandCoresForPlayer_Player`):
  UnitGroup_Clear(`OV_GetAllHandCoresForPlayer_HandCoreUnitGroup`)
  `player_blackboard` = Blackboard_GetBlackboardOfPlayer(`IV_GetAllHandCoresForPlayer_Player`)
  General_ForEachInteger(`i`, 0, 5):
    `player_blackboard_key` = String_Concat("hand_core_at_hand_position_", `i`)
    UnitGroup_AddUnit(
      `OV_GetAllHandCoresForPlayer_HandCoreUnitGroup`,
      Blackboard_GetValue_Unit(
        `player_blackboard`,
        `player_blackboard_key`
      )
    )
  <!-- UnitGroup_ForEachUnitInGroup(`OV_GetAllHandCoresForPlayer_HandCoreUnitGroup`):
    print(Unit_GetPlacedName(UnitGroup_GetCurrentUnit)) -->
