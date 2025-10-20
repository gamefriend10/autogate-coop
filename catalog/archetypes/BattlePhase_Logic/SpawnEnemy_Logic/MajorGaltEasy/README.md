# MajorGaltWaves

SpawnMajorGaltWave(`GV_BattleRound`):
  Switch(`GV_BattleRound`):
    case 1: `GV_EnemyUnitGroup` = SpawnMajorGaltWave1()
    repeat 2-15...

  // Return `GV_EnemyUnitGroup`

SpawnMajorGaltWave1():
  // Create 5 Servos for player 5 at GV_BattleCenterPointPosition
  Unit_CreateUnit(5, Worker_AttacksBack_GivesNoXP, 5, GV_BattleCenterPointPosition)
  UnitGroup_AddUnits(`GV_EnemyUnitGroup`, UnitGroup_GetLastCreatedUnits())

  // Return `GV_EnemyUnitGroup`

SpawnMajorGaltWave2():
  // Create 10 Scouts for player 5 at GV_BattleCenterPointPosition
  Unit_CreateUnit(10, Scout, 5, GV_BattleCenterPointPosition)
  UnitGroup_AddUnits(`GV_EnemyUnitGroup`, UnitGroup_GetLastCreatedUnits())

  // Return `GV_EnemyUnitGroup`

SpawnMajorGaltWave3:
  8 Lancer 800

SpawnMajorGaltWave4:
  12 Gunner 1200

SpawnMajorGaltWave5:
  8 Gunner, 4 MedTech_Autogate, 5 Lancer 1900

SpawnMajorGaltWave6:
  12 MissileJeep, 14 Scout 2500

SpawnMajorGaltWave7:
  10 Vulcan 3000

SpawnMajorGaltWave8:
  6 MedTech_Autogate, 25 MissileJeep 4650

SpawnMajorGaltWave9:
  2 ArtilleryMechDeployed_Autogate, 6 MedTech_Autogate, 10 MissileJeep, 5 Vulcan 4700

SpawnMajorGaltWave10:
  2 ArtilleryMechDeployed_Autogate, 5 Gunner, 4 MedTech_Autogate, 3 MissileJeep, 2 Vulcan, 10 Scout, 5 Lancer ~6000

SpawnMajorGaltWave11:
  36 Jet, 8 MedTech_Autogate 7200

SpawnMajorGaltWave12:
  12 Jet 12 Vulcan 8 MedTech_Autogate 7350

SpawnMajorGaltWave13:
  10 Helicarrier 3 MedTech_Autogate 4 Vulcan 8200

SpawnMajorGaltWave14:
  3 ArtilleryMechDeployed_Autogate, 10 Jet, 8 Vulcan, 4 Helicarrier 8 MedTech_Autogate ~9500

SpawnMajorGaltWave15:
  MajorGalt_Autogate + Wave14