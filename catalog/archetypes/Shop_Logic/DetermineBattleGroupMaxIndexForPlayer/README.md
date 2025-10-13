// Determines which index is the last of a tier's battle groups, if you lined up all battle
// groups end to end. E.g. If Tier1 has 2 units and Tier2 has 1, the max index would be 2.
// Returns: `GV_DetermineBattleGroupMaxIndex_Index`
DetermineBattleGroupMaxIndex(Integer `IV_DetermineBattleGroupMaxIndex_Tier`):
  // Determine max index
  Switch(`IV_DetermineBattleGroupMaxIndex_Tier`):
    case 1:
      Set `GV_DetermineBattleGroupMaxIndex_Index` = `LengthOfTier1BattleGroups`-1
    case 2:
      Set `GV_DetermineBattleGroupMaxIndex_Index` = `LengthOfTier2AndBelowBattleGroups`-1
    case 3:
      Set `GV_DetermineBattleGroupMaxIndex_Index` = `LengthOfTier3AndBelowBattleGroups`-1
    case 4:
      Set `GV_DetermineBattleGroupMaxIndex_Index` = `LengthOfTier4AndBelowBattleGroups`-1
    case 5:
      Set `GV_DetermineBattleGroupMaxIndex_Index` = `LengthOfTier5AndBelowBattleGroups`-1
    case 6:
      Set `GV_DetermineBattleGroupMaxIndex_Index` = `LengthOfTier6AndBelowBattleGroups`-1