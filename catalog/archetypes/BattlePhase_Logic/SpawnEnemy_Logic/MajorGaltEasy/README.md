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
  3 Helicarrier, 24 Jet, 8 MedTech_Autogate 2100 + 5400 + 2400 = 9900

SpawnMajorGaltWave12:
  24 Jet 12 Vulcan 8 MedTech_Autogate 5400 + 3600 + 2400 = 11400

SpawnMajorGaltWave13:
  6 ArtilleryMechDeployed_Autogate, 20 Helicarrier 8 MedTech_Autogate 12 Vulcan 36 Gunner
  2250 + 7000 + 2400 + 3600 + 3600 = 18850

SpawnMajorGaltWave14:
  12 ArtilleryMechDeployed_Autogate, 40 Jet, 24 Helicarrier 8 Vulcan 8 MedTech_Autogate 36 Gunner 24 Lancer
  4500 + 2250 + 7000 + 2400 + 2800 + 2400 + 3600 + 2400 = 27350

SpawnMajorGaltWave15:
  MajorGalt_Autogate + Wave14