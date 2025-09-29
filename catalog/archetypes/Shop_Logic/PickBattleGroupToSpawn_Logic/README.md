PickBattleGroupToSpawnForPlayer(Player `IV_PickBattleGroupToSpawnForPlayer_Player`):
  Switch(
    Blackboard_GetValue_Integer(
      Blackboard_GetBlackboardOfPlayer(`IV_PickBattleGroupToSpawnForPlayer_Player`),
      "shop_tier"
    )
  ):
    case 2: PickTier2AndBelowBattleGroupToSpawn
    case 3: PickTier3AndBelowBattleGroupToSpawn
    case 4: PickTier4AndBelowBattleGroupToSpawn // TODO
    case 5: PickTier5AndBelowBattleGroupToSpawn // TODO
    case 6: PickTier6AndBelowBattleGroupToSpawn // TODO
    default: PickTier1BattleGroupToSpawn

--------------------

PickTier1BattleGroupToSpawn():
  set `BattleGroupToSpawnTag` = `Tier1BattleGroups`[Random_Integer(0, LengthOfTier1BattleGroups-1)]

--------------------

PickTier2AndBelowBattleGroupToSpawn():
  set `BattleGroupToSpawnTag` = `Tier2AndBelowBattleGroups`[Random_Integer(0, LengthOfTier2AndBelowBattleGroups-1)]

--------------------

PickTier3AndBelowBattleGroupToSpawn():
  set `BattleGroupToSpawnTag` = `Tier3AndBelowBattleGroups`[Random_Integer(0, LengthOfTier3AndBelowBattleGroups-1)]