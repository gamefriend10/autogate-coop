PickBattleGroupToSpawn():
  switch(`Tier`)
    case 2: PickTier2AndBelowBattleGroupToSpawn
    default: PickTier1BattleGroupToSpawn

TODO: refactor^ into
PickBattleGroupToSpawnForPlayer(`IV_PickBattleGroupToSpawnForPlayer_Player`):
  Switch(
    Blackboard_GetValue_Integer(
      Blackboard_GetBlackboardOfPlayer(`IV_PickBattleGroupToSpawnForPlayer_Player`),
      "shop_tier"
    )
  ):
    case 1: PickTier1BattleGroupToSpawn
    case 2: PickTier2AndBelowBattleGroupToSpawn
    case 3: PickTier3AndBelowBattleGroupToSpawn
    case 4: PickTier4AndBelowBattleGroupToSpawn
    case 5: PickTier5AndBelowBattleGroupToSpawn
    case 6: PickTier6AndBelowBattleGroupToSpawn

--------------------

PickTier1BattleGroupToSpawn():
  set `BattleGroupToSpawnTag` = `Tier1BattleGroups`[Random_Integer(0, LengthOfTier1BattleGroups-1)]

--------------------

PickTier2AndBelowBattleGroupToSpawn():
  set `BattleGroupToSpawnTag` = `Tier2AndBelowBattleGroups`[Random_Integer(0, LengthOfTier2AndBelowBattleGroups-1)]