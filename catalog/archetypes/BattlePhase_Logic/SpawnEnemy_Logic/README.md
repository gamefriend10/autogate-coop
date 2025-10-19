## Adding an opponent

1. copy/paste an old opponent
2. run `python scripts/replace_string_recursive.py <dir> <old-name> <new-name>`
  1. careful about renaming FG assets to be used e.g. icons, units, which will brick the build
2. add to SpawnEnemy()
3. add to ShopTopBarCaster abilityList
4. add to AutoGateFaction

SpawnEnemy():
  Switch(`GV_Opponent`):
    case "MajorGaltEasy": `GV_EnemyUnitGroup` = SpawnMajorGaltWave(`GV_BattleRound`)
    case "MajorGaltHard": `GV_EnemyUnitGroup` = SpawnMajorGaltHardWave(`GV_BattleRound`)
    repeat for any new opponents
  `GV_EnemyUnitCountAtBeginningOfRound` = UnitGroup_CountAliveUnits(`GV_EnemyUnitGroup`)
