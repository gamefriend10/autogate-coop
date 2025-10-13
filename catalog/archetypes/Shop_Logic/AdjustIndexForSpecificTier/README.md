// Shift the index based on what tier we're at
// E.g. 1 unit per tier means indices 012345. If we get 5, we want the first index
// of Tier 6, i.e. 0, so we subtract LengthOfTier5AndBelow.
// Returns:
//  `OV_AdjustIndexForSpecificTier_Tier`
//  `OV_AdjustIndexForSpecificTier_Index`
AdjustIndexForSpecificTier(Integer `IV_AdjustIndexForSpecificTier_Index`):
  Set `OV_AdjustIndexForSpecificTier_Tier` = 1
  Set `OV_AdjustIndexForSpecificTier_Index` = `IV_AdjustIndexForSpecificTier_Index`
  If(`IV_AdjustIndexForSpecificTier_Index` > `LengthOfTier5AndBelowBattleGroups`-1):
    Set `OV_AdjustIndexForSpecificTier_Tier` = 6
    Set `OV_AdjustIndexForSpecificTier_Index` -= `LengthOfTier5AndBelowBattleGroups`
    General_SkipRemainingActions()
  If(`IV_AdjustIndexForSpecificTier_Index` > `LengthOfTier4AndBelowBattleGroups`-1):
    Set `OV_AdjustIndexForSpecificTier_Tier` = 5
    Set `OV_AdjustIndexForSpecificTier_Index` -= `LengthOfTier4AndBelowBattleGroups`
    General_SkipRemainingActions()
  If(`IV_AdjustIndexForSpecificTier_Index` > `LengthOfTier3AndBelowBattleGroups`-1):
    Set `OV_AdjustIndexForSpecificTier_Tier` = 4
    Set `OV_AdjustIndexForSpecificTier_Index` -= `LengthOfTier3AndBelowBattleGroups`
    General_SkipRemainingActions()
  If(`IV_AdjustIndexForSpecificTier_Index` > `LengthOfTier2AndBelowBattleGroups`-1):
    Set `OV_AdjustIndexForSpecificTier_Tier` = 3
    Set `OV_AdjustIndexForSpecificTier_Index` -= `LengthOfTier2AndBelowBattleGroups`
    General_SkipRemainingActions()
  If(`IV_AdjustIndexForSpecificTier_Index` > `LengthOfTier1BattleGroups`-1):
    Set `OV_AdjustIndexForSpecificTier_Tier` = 2
    Set `OV_AdjustIndexForSpecificTier_Index` -= `LengthOfTier1BattleGroups`
    General_SkipRemainingActions()