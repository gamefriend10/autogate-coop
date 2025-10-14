// Note: runs on triggeringUnit
// Conditions: Entity_HasAllTags(triple_snowtag)
Triple_PickAndAddRandomNextTierBattleGroupToHand():
  // Pick BG of player's next tier
  Switch(
    Math_Min(
      Blackboard_GetValue_Integer(
        Blackboard_GetBlackboardOfPlayer(),
        "shop_tier"
      ) + 1,
      6
    )
  ):
    case 2:
      Set `IV_DetermineHandCoreFromTag_Tag` = `Tier2BattleGroups`[Random_Integer(0, `LengthOfTier2BattleGroups`-1)]
    case 3:
      Set `IV_DetermineHandCoreFromTag_Tag` = `Tier3BattleGroups`[Random_Integer(0, `LengthOfTier3BattleGroups`-1)]
    case 4:
      Set `IV_DetermineHandCoreFromTag_Tag` = `Tier4BattleGroups`[Random_Integer(0, `LengthOfTier4BattleGroups`-1)]
    case 5:
      Set `IV_DetermineHandCoreFromTag_Tag` = `Tier5BattleGroups`[Random_Integer(0, `LengthOfTier5BattleGroups`-1)]
    case 6:
      Set `IV_DetermineHandCoreFromTag_Tag` = `Tier6BattleGroups`[Random_Integer(0, `LengthOfTier6BattleGroups`-1)]
  `OV_DetermineHandCoreFromTag_HandCoreType` = DetermineHandCoreFromTag(`IV_DetermineHandCoreFromTag_Tag`)

  Set `IV_AddBattleGroupToHand_HandCoreType` = `OV_DetermineHandCoreFromTag_HandCoreType`
  Set `IV_AddBattleGroupToHand_Player` = Unit_GetOwningPlayer(Unit_GetTriggeringUnit())
  `OV_AddBattleGroupToHand_HandCore` = AddBattleGroupToHand(`IV_AddBattleGroupToHand_HandCoreType`, `IV_AddBattleGroupToHand_Player`)