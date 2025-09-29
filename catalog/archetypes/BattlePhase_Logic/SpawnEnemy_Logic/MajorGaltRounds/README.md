# MajorGaltWaves

SpawnMajorGaltWave(`GV_BattleRound`):
  Switch(`GV_BattleRound`):
    case 1: `GV_EnemyUnitGroup` = SpawnMajorGaltWave1()
    repeat 2-15...

  // Return `GV_EnemyUnitGroup`

SpawnMajorGaltWave1():
  // Create 10 Servos for player 5 at GV_BattleCenterPointPosition
  Unit_CreateUnit(10, Worker_AttacksBack_GivesNoXP, 5, GV_BattleCenterPointPosition)
  UnitGroup_AddUnits(`GV_EnemyUnitGroup`, UnitGroup_GetLastCreatedUnits())

  // Return `GV_EnemyUnitGroup`

SpawnMajorGaltWave2():
  // Create 20 Scouts for player 5 at GV_BattleCenterPointPosition
  Unit_CreateUnit(20, Scout, 5, GV_BattleCenterPointPosition)
  UnitGroup_AddUnits(`GV_EnemyUnitGroup`, UnitGroup_GetLastCreatedUnits())

  // Return `GV_EnemyUnitGroup`

SpawnMajorGaltWave3:
  15 Lancer 1500

SpawnMajorGaltWave4:
  20 Gunner 2000

SpawnMajorGaltWave5:
  10 Gunner, 5 MedTech, 10 Lancer 2750

SpawnMajorGaltWave6:
  15 MissileJeep, 15 Scout 3000

SpawnMajorGaltWave7:
  12 Vulcan 3600

SpawnMajorGaltWave8:
  20 MissileJeep, 6 MedTech 3900

SpawnMajorGaltWave9:
  10 MissileJeep, 5 Vulcan, 2 ArtilleryMechDeployed, 6 MedTech 4700

SpawnMajorGaltWave10:
  5 Gunner, 4 MedTech, 3 MissileJeep, 2 Vulcan, 1 ArtilleryMechDeployed, 10 Scout, 5 Lancer ~5500

SpawnMajorGaltWave11:
  24 Jet 6000

SpawnMajorGaltWave12:
  12 Jet 12 Vulcan 3 MedTech 6600

SpawnMajorGaltWave13:
  10 Helicarrier 3 MedTech 7000

SpawnMajorGaltWave14:
  10 Jet, 8 Vulcan, 4 Helicarrier 3 MedTech 7500

SpawnMajorGaltWave15:
  BotPersonaMajorGaltHeroUnit + 14