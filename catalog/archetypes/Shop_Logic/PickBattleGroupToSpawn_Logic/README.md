# PickBattleGroupToSpawn

1. switch(`Tier`)
  1. case 2: PickTier2AndBelowBattleGroupToSpawn
  2. default: PickTier1BattleGroupToSpawn

# PickTier1BattleGroupToSpawn

1. set `BattleGroupToSpawnTag` to a random tag from `Tier1BattleGroups`

# PickTier2AndBelowBattleGroupToSpawn

1. set `BattleGroupToSpawnTag` to a random tag from `Tier2AndBelowBattleGroups`