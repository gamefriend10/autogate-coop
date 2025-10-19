# MajorGaltHardWaves

SpawnMajorGaltHardWave(`GV_BattleRound`):
  Switch(`GV_BattleRound`):
    case 1: `GV_EnemyUnitGroup` = SpawnMajorGaltHardWave1()
    repeat 2-15...

  // Return `GV_EnemyUnitGroup`

SpawnMajorGaltHardWave1():
  // Create 20 Servos for player 5 at GV_BattleCenterPointPosition
  Unit_CreateUnit(20, Worker_AttacksBack_GivesNoXP, 5, GV_BattleCenterPointPosition)
  UnitGroup_AddUnits(`GV_EnemyUnitGroup`, UnitGroup_GetLastCreatedUnits())

  // Return `GV_EnemyUnitGroup`

SpawnMajorGaltHardWave2():
  // Create 20 Scouts for player 5 at GV_BattleCenterPointPosition
  Unit_CreateUnit(20, Scout, 5, GV_BattleCenterPointPosition)
  UnitGroup_AddUnits(`GV_EnemyUnitGroup`, UnitGroup_GetLastCreatedUnits())

  // Return `GV_EnemyUnitGroup`

SpawnMajorGaltHardWave3:
  15 Lancer 1500

SpawnMajorGaltHardWave4:
  20 Gunner 2000

SpawnMajorGaltHardWave5:
  10 Gunner, 5 MedTech_Autogate, 10 Lancer 2750

SpawnMajorGaltHardWave6:
  15 MissileJeep, 15 Scout 3000

SpawnMajorGaltHardWave7:
  12 Vulcan 3600

SpawnMajorGaltHardWave8:
  20 MissileJeep, 6 MedTech_Autogate 3900

SpawnMajorGaltHardWave9:
  10 MissileJeep, 5 Vulcan, 2 ArtilleryMechDeployed, 6 MedTech_Autogate 4700

SpawnMajorGaltHardWave10:
  5 Gunner, 4 MedTech_Autogate, 3 MissileJeep, 2 Vulcan, 1 ArtilleryMechDeployed, 10 Scout, 5 Lancer ~5500

SpawnMajorGaltHardWave11:
  24 Jet 6000

SpawnMajorGaltHardWave12:
  12 Jet 12 Vulcan 3 MedTech_Autogate 6600

SpawnMajorGaltHardWave13:
  10 Helicarrier 3 MedTech_Autogate 7000

SpawnMajorGaltHardWave14:
  10 Jet, 8 Vulcan, 4 Helicarrier 3 MedTech_Autogate 7500

SpawnMajorGaltHardWave15:
  BotPersonaMajorGaltHardHeroUnit + 14