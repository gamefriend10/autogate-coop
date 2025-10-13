// Reuses: Integer `GV_DetermineBattleGroupMaxIndex_Index`
// Returns: `BattleGroupToSpawnTag`
PickBattleGroupToSpawnForPlayer():
  // Pick random index
  Set `IV_AdjustIndexForSpecificTier_Index` = Random_Integer(0, `GV_DetermineBattleGroupMaxIndex_Index`)

  (`OV_AdjustIndexForSpecificTier_Tier`, `OV_AdjustIndexForSpecificTier_Index`) =
    AdjustIndexForSpecificTier(`IV_AdjustIndexForSpecificTier_Index`)

  Switch(`OV_AdjustIndexForSpecificTier_Tier`):
    case 1:
      Set `BattleGroupToSpawnTag` = `Tier1BattleGroups`[`OV_AdjustIndexForSpecificTier_Index`]
    case 2:
      Set `BattleGroupToSpawnTag` = `Tier2BattleGroups`[`OV_AdjustIndexForSpecificTier_Index`]
    case 3:
      Set `BattleGroupToSpawnTag` = `Tier3BattleGroups`[`OV_AdjustIndexForSpecificTier_Index`]
    case 4:
      Set `BattleGroupToSpawnTag` = `Tier4BattleGroups`[`OV_AdjustIndexForSpecificTier_Index`]
    case 5:
      Set `BattleGroupToSpawnTag` = `Tier5BattleGroups`[`OV_AdjustIndexForSpecificTier_Index`]
    case 6:
      Set `BattleGroupToSpawnTag` = `Tier6BattleGroups`[`OV_AdjustIndexForSpecificTier_Index`]