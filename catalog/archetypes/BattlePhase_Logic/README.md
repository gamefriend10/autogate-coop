OrderToBattle(`UnitsToOrderToBattle`):
  UnitGroup_IssueOrderTargetingPos(
    `UnitsToOrderToBattle`,
    Actor_GetPosition(
      Point_GetPointFromPlacedName(
        "BattleCenterPoint"
      )
    ),
    attackData
  )
  UnitGroup_IssueOrderTargetingPos(
    `GV_EnemyUnitGroup`,
    Actor_GetPosition(
      Point_GetPointFromPlacedName(
        "BattleCenterPoint"
      )
    ),
    attackData
  )

--------------------

CreateBattleUnitsForPlayer(Player `GV_PlayerToCreateBattleUnitsFor`)

Set row = 0
Set col = 0
Set `GV_BattlePositionForPlayer` = GetBattlePositionForPlayer(`GV_PlayerToCreateBattleUnitsFor`)
General_ForEachInteger(row, 0, 2):
  General_ForEachInteger(col, 0, 2):
    Set `GV_StagingCoreToDuplicateTheBattleUnitsOf` = player `GV_PlayerToCreateBattleUnitsFor` 's blackboard[[row][col]] stagingCore
    DuplicateUnitsAndMoveToBattleArea(`GV_StagingCoreToDuplicateTheBattleUnitsOf`, `GV_BattlePositionForPlayer`)

--------------------

Vector GetBattlePositionForPlayer(Player `GV_PlayerToCreateBattleUnitsFor`)

If `GV_PlayerToCreateBattleUnitsFor` == 1:
  Set `GV_BattlePositionForPlayer` to Actor_GetPosition(Player1_BattlePoint)
repeat for player 2-4

--------------------

DuplicateUnitsAndMoveToBattleArea(
  Player `GV_PlayerToCreateBattleUnitsFor`,
  Unit `GV_StagingCoreToDuplicateTheBattleUnitsOf`,
  Vector `GV_BattlePositionForPlayer`
)

UnitGroup_ForEachUnitInGroup(`units` from `GV_StagingCoreToDuplicateTheBattleUnitsOf`)
  Unit_CreateUnit(
    1,
    Unit_GetType(UnitGroup_GetCurrentUnit),
    `GV_PlayerToCreateBattleUnitsFor`,
    `GV_BattlePositionForPlayer`
  )
  Unit_SetVeterancyTier(
    Unit_GetLastCreatedUnit,
    Unit_GetVeterancyTier(UnitGroup_GetCurrentUnit)
    General_DoDoNot.do_not
  )
  UnitGroup_AddUnit(`UnitsToOrderToBattle`)

--------------------

// Executes every 3 seconds via Timer_OnPeriodicEvent()
CheckBattlePhaseOver():
  If `GV_CurrentGameState` != Preset_GameState.battle:
    SkipRemainingActions()
  OrderToBattle()
  // Print(UnitGroup_CountAliveUnits(`GV_EnemyUnitGroup`))
  If UnitGroup_CountAliveUnits(`GV_EnemyUnitGroup`) == 0 || UnitGroup_CountAliveUnits(`UnitsToOrderToBattle`) == 0:
    TriggerRun(OnExitBattlePhaseTrigger())
    TriggerRun(OnEnterBuyPhaseTrigger())

--------------------

OnEnterBattlePhaseTrigger

`GV_CurrentGameState` = Preset_GameState.battle
PlayerGroup_ForEachPlayerInGroup(PlayerGroup_GetActivePlayers()):
  TechTree_SetUpgradeLevel(PlayerGroup_GetCurrentPlayer, GameStateIsBattleStateDummyUpgrade, 1) // Stops top bar
  `GV_PlayerToCreateBattleUnitsFor` = PlayerGroup_GetCurrentPlayer
  CreateBattleUnitsForPlayer(`GV_PlayerToCreateBattleUnitsFor`)
  TODO: Set camera to player's corner
  TODO: Pan camera to battle center
`GV_EnemyUnitCountAtBeginningOfRound` = SpawnEnemy()
OrderToBattle()

--------------------

OnExitBattlePhaseTrigger():
  // Deduct hero hp
  // Using Random_Value to cast Integer->Value
  `percent_of_enemy_units_alive` = (
    Random_Value(UnitGroup_CountAliveUnits(`GV_EnemyUnitGroup`), UnitGroup_CountAliveUnits(`GV_EnemyUnitGroup`)) /
    Random_Value(`GV_EnemyUnitCountAtBeginningOfRound`, `GV_EnemyUnitCountAtBeginningOfRound`)
  )
  `hp_to_deduct` = `GV_BattleRound` * 10 * `percent_of_enemy_units_alive`

  // Print status msg
  If UnitGroup_CountAliveUnits(`GV_EnemyUnitGroup`) == 0:
    UI_SendChatMessage(String_FormatString(
      "You beat round {0}.",
      `GV_BattleRound`
    ))
  If UnitGroup_CountAliveUnits(`UnitsToOrderToBattle`) == 0:
    UI_SendChatMessage(String_FormatString(
      "You lost round {0}. You lose {1} hp.",
      `GV_BattleRound`,
      `hp_to_deduct`
    ))

  UnitGroup_ForEachUnitInGroup(`GV_Heros_UnitGroup`):
    Unit_SetHealth(
      UnitGroup_GetCurrentUnit(),
      Unit_GetHealth(UnitGroup_GetCurrentUnit()) - `hp_to_deduct`
    )
    If Unit_GetHealth(UnitGroup_GetCurrentUnit()) <= 0:
      Unit_Kill(UnitGroup_GetCurrentUnit())
      Game_EndGameForPlayer(
        Unit_GetOwningPlayer(UnitGroup_GetCurrentUnit()),
        Game_GameOverType.defeat,
        Game_KickDontKick.nokick
      )

  // Only add max lum up after completing rounds 1-7
  If `GV_BattleRound` <= 7: 
    set `IV_NumberOfMaxLumToAdd` = 1
    PlayerGroup_ForEachPlayerInGroup(PlayerGroup_GetActivePlayers()):
      set `IV_PlayerToAddMaxLumTo` = PlayerGroup_GetCurrentPlayer()
      AddMaxLumForPlayer_Trigger(`IV_NumberOfMaxLumToAdd`, `IV_PlayerToAddMaxLumTo`)

  `GV_BattleRound` += 1

  // Win the game after beating 15 rounds
  If `GV_BattleRound` > 15:
    PlayerGroup_ForEachPlayerInGroup(PlayerGroup_GetActivePlayers()):
      Game_EndGameForPlayer(
        PlayerGroup_GetCurrentPlayer(),
        Game_GameOverType.victory,
        Game_KickDontKick.nokick
      )

  // Remove remaining player units from game
  UnitGroup_ForEachUnitInGroup(`UnitsToOrderToBattle`):
    Unit_Kill(UnitGroup_GetCurrentUnit())

  // Remove remaining enemy units from game
  UnitGroup_ForEachUnitInGroup(`GV_EnemyUnitGroup`):
    Unit_Kill(UnitGroup_GetCurrentUnit())
