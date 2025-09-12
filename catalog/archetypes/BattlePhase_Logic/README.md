OrderToBattle

prereqs:
1. `UnitsToOrderToBattle` has all the appropriate units added to it

Orders units to attack BattleCenterPoint

Q: what happens when the units in the unitgroup die...? do they get auto removed? will it crash? spam errors?

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

// Executes every 5 seconds via Timer_OnPeriodicEvent(5)
CheckBattlePhaseOver():
  If `GV_CurrentGameState` != Preset_GameState.battle:
    SkipRemainingActions()
  If UnitGroup_CountAliveUnits(`GV_EnemyUnitGroup`) == 0 || UnitGroup_CountAliveUnits(`UnitsToOrderToBattle`) == 0:
    TriggerRun(OnExitBattlePhaseTrigger())
    TriggerRun(OnEnterBuyPhaseTrigger())

--------------------

OnEnterBattlePhaseTrigger

`GV_CurrentGameState` = Preset_GameState.battle
PlayerGroup_ForEachPlayerInGroup(PlayerGroup_GetActivePlayers()):
  TechTree_SetUpgradeLevel(PlayerGroup_GetCurrentPlayer, GameStateIsBattleStateDummyUpgrade, 1) // Stops rdy up
  `GV_PlayerToCreateBattleUnitsFor` = PlayerGroup_GetCurrentPlayer
  CreateBattleUnitsForPlayer(`GV_PlayerToCreateBattleUnitsFor`)
  TODO: Set camera to player's corner
  TODO: Pan camera to battle center
`GV_EnemyUnitCountAtBeginningOfRound` = SpawnEnemy()
OrderToBattle()

--------------------

OnExitBattlePhaseTrigger():
  // Using Random_Value to cast Integer->Value
  `percent_of_enemy_units_alive` = (
    Random_Value(UnitGroup_CountAliveUnits(`GV_EnemyUnitGroup`), UnitGroup_CountAliveUnits(`GV_EnemyUnitGroup`)) /
    Random_Value(`GV_EnemyUnitCountAtBeginningOfRound`, `GV_EnemyUnitCountAtBeginningOfRound`)
  )
  `hp_to_deduct` = `GV_BattleRound` * 10 * `percent_of_enemy_units_alive`
  UnitGroup_ForEachUnitInGroup(`GV_Heros_UnitGroup`):
    Unit_SetHealth(
      UnitGroup_GetCurrentUnit(),
      Unit_GetHealth(UnitGroup_GetCurrentUnit()) - `hp_to_deduct`
    )
    If Unit_GetHealth(UnitGroup_GetCurrentUnit()) <= 0:
      Unit_Kill(UnitGroup_GetCurrentUnit())
  `GV_BattleRound` += 1
  TODO: kill remaining player/enemy units