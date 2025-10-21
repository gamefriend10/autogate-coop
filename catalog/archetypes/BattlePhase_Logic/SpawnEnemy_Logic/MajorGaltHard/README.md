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
  // Create 40 Scouts for player 5 at GV_BattleCenterPointPosition
  Unit_CreateUnit(40, Scout, 5, GV_BattleCenterPointPosition)
  UnitGroup_AddUnits(`GV_EnemyUnitGroup`, UnitGroup_GetLastCreatedUnits())

  // Return `GV_EnemyUnitGroup`

SpawnMajorGaltHardWave3:
  32 Lancer 800

SpawnMajorGaltHardWave4:
  48 Gunner 1200

SpawnMajorGaltHardWave5:
  32 Gunner, 16 MedTech_Autogate, 20 Lancer 1900

SpawnMajorGaltHardWave6:
  48 MissileJeep, 56 Scout 2500

SpawnMajorGaltHardWave7:
  40 Vulcan 3000

SpawnMajorGaltHardWave8:
  24 MedTech_Autogate, 100 MissileJeep 4650

SpawnMajorGaltHardWave9:
  8 ArtilleryMechDeployed_Autogate, 24 MedTech_Autogate, 40 MissileJeep, 20 Vulcan 4700

SpawnMajorGaltHardWave10:
  8 ArtilleryMechDeployed_Autogate, 20 Gunner, 16 MedTech_Autogate, 12 MissileJeep, 8 Vulcan, 40 Scout, 20 Lancer ~6000

SpawnMajorGaltHardWave11:
  12 Helicarrier, 96 Jet, 32 MedTech_Autogate 2100 + 5400 + 2400 = 9900

SpawnMajorGaltHardWave12:
  96 Jet 48 Vulcan 32 MedTech_Autogate 5400 + 3600 + 2400 = 11400

SpawnMajorGaltHardWave13:
  24 ArtilleryMechDeployed_Autogate, 80 Helicarrier 32 MedTech_Autogate 48 Vulcan 144 Gunner
  2250 + 7000 + 2400 + 3600 + 3600 = 18850

SpawnMajorGaltHardWave14:
  48 ArtilleryMechDeployed_Autogate, 160 Jet, 96 Helicarrier 32 Vulcan 32 MedTech_Autogate 144 Gunner 96 Lancer
  4500 + 2250 + 7000 + 2400 + 2800 + 2400 + 3600 + 2400 = 27350

SpawnMajorGaltHardWave15:
  MajorGalt_Autogate + Wave14