// Returns (`GV_LengthOfUnitDataToSpawnArray`, `GV_UnitDataToSpawnArray`, `GV_NumOfUnitsToSpawnForEachUnitDataArray`)
SetVarsFor_Blockhead_Core_SpawnUnits():
  `GV_LengthOfUnitDataToSpawnArray` = 1
  `GV_UnitDataToSpawnArray`[0] = Blockade_Autogate
  `GV_NumOfUnitsToSpawnForEachUnitDataArray`[0] = 1

--------------------

// Condition:
//  Ability_GetTriggeringAbility() == Blockhead_StagingCore_MassPromote ||
//  Ability_GetTriggeringAbility() == BlockheadTriple_StagingCore_MassPromote
// Trigger: Unit_OnAbilityUsed()
OnMassPromoteUsed():
  set `IV_PlayerToGetStagingCoresFor` = Unit_GetOwningPlayer(Unit_GetTriggeringUnit())
  `OV_PlayerStagingCoresAsUnitGroup` = GetAllStagingCoresForPlayer(`IV_PlayerToGetStagingCoresFor`)

  // For every staging core
  UnitGroup_ForEachUnitInGroup(`OV_PlayerStagingCoresAsUnitGroup`):
    If(Entity_HasNoneTags(UnitGroup_GetCurrentUnit(), vanguard_snowtag)):
      General_Continue()
    Set `IV_GiveCoreUnitsVeterancy_Core` = UnitGroup_GetCurrentUnit()
    Set `IV_GiveCoreUnitsVeterancy_NumXP` = 100
    GiveCoreUnitsVeterancy(`IV_GiveCoreUnitsVeterancy_Core`, `IV_GiveCoreUnitsVeterancy_NumXP`)