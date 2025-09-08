# MajorGaltWaves

SpawnMajorGaltWave(`GV_BattleRound`):
  Switch(`GV_BattleRound`):
    case 1: SpawnMajorGaltWave1()
    TODO: repeat 2-15...

SpawnMajorGaltWave1():
  // Create 10 Servos for player 5 at GV_BattleCenterPointPosition
  Unit_CreateUnit(10, Worker, 5, GV_BattleCenterPointPosition)

SpawnMajorGaltWave1():
  // Create 20 Scouts for player 5 at GV_BattleCenterPointPosition
  Unit_CreateUnit(20, Scout, 5, GV_BattleCenterPointPosition)