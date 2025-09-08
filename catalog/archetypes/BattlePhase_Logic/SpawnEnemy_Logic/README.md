# SpawnEnemy_Logic

SpawnEnemy():
  Switch(`GV_Opponent`):
    case "MajorGalt": `GV_EnemyUnitGroup` = SpawnMajorGaltWave(`GV_BattleRound`)
    repeat for any new opponents
  `GV_EnemyUnitCountAtBeginningOfRound` = UnitGroup_CountAliveUnits(`GV_EnemyUnitGroup`)
  `GV_BattleRound` += 1
