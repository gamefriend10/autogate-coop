# MajorGaltWaves

SpawnMajorGaltWave(`GV_BattleRound`):
  Switch(`GV_BattleRound`):
    case 1: `GV_EnemyUnitGroup` = SpawnMajorGaltWave1()
    TODO: repeat 2-15...

  // Return `GV_EnemyUnitGroup`

SpawnMajorGaltWave1():
  // Create 10 Servos for player 5 at GV_BattleCenterPointPosition
  Unit_CreateUnit(10, Worker_AttacksBack_GivesNoXP, 5, GV_BattleCenterPointPosition)
  UnitGroup_AddUnits(`GV_EnemyUnitGroup`, UnitGroup_GetLastCreatedUnits())

  // Return `GV_EnemyUnitGroup`

SpawnMajorGaltWave1():
  // Create 20 Scouts for player 5 at GV_BattleCenterPointPosition
  Unit_CreateUnit(20, Scout, 5, GV_BattleCenterPointPosition)
  UnitGroup_AddUnits(`GV_EnemyUnitGroup`, UnitGroup_GetLastCreatedUnits())

  // Return `GV_EnemyUnitGroup`