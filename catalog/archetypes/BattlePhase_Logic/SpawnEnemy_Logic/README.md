# SpawnEnemy_Logic

SpawnEnemy():
  Switch(`GV_Opponent`):
    case "MajorGalt": SpawnMajorGaltWave(`GV_BattleRound`)
    repeat for any new opponents
  `GV_BattleRound` += 1
