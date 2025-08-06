OrderToBattle

prereqs:
1. `UnitsToOrderToBattle` has all the appropriate units added to it

Orders units to attack BattleCenterPoint

Q: what happens when the units in the unitgroup die...? do they get auto removed? will it crash? spam errors?

----
TODO: remove this from StagingCoreBirthTrigger
OnEnterBattlePhaseTrigger

PlayerGroup_ForEachPlayerInGroup(PlayerGroup_GetActivePlayers())
  Set `GV_PlayerToCreateBattleUnitsFor` = PlayerGroup_GetCurrentPlayer
  CreateBattleUnitsForPlayer(`GV_PlayerToCreateBattleUnitsFor`)
  DISABLED: Camera_PushCameraTrackingTarget(
    Player_GetActiveCamera(PlayerGroup_GetCurrentPlayer),
    UnitGroup_GetFirstUnit(`UnitsToOrderToBattle`) TODO: track player's group? or just set camera to center
  )
SpawnEnemy()
OrderToBattle()

---
CreateBattleUnitsForPlayer(Player `GV_PlayerToCreateBattleUnitsFor`)

Set row = 0
Set col = 0
General_ForEachInteger(row, 0, 2):
  General_ForEachInteger(col, 0, 2):
    Set `GV_StagingCoreToDuplicateTheBattleUnitsOf` = player `GV_PlayerToCreateBattleUnitsFor` 's blackboard[[row][col]] stagingCore
    Set `GV_BattlePositionForPlayer` = GetBattlePositionForPlayer(`GV_PlayerToCreateBattleUnitsFor`)
    DuplicateUnitsAndMoveToBattleArea(`GV_StagingCoreToDuplicateTheBattleUnitsOf`, `GV_BattlePositionForPlayer`)
    

---
Vector GetBattlePositionForPlayer(Player `GV_PlayerToCreateBattleUnitsFor`)

If `GV_PlayerToCreateBattleUnitsFor` == 1:
  Set `GV_BattlePositionForPlayer` to Actor_GetPosition(Player1_BattlePoint)
repeat for player 2-4

---
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