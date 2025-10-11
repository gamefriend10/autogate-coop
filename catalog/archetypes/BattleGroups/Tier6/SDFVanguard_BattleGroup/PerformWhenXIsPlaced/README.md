// When a Vanguard Battle Group is placed, add 1 Exo
// to every Battle Group (including this one).
SDFVanguard_PerformWhenXIsPlaced():
  // Note: It would be more efficient to put this check one level up, but harder to reason about
  If(Entity_HasNoneTags(Unit_GetTriggeringUnit(), vanguard_snowtag)):
    General_SkipRemainingActions()
  
  set `IV_PlayerToGetStagingCoresFor` = Unit_GetOwningPlayer(Unit_GetTriggeringUnit())
  `OV_PlayerStagingCoresAsUnitGroup` = GetAllStagingCoresForPlayer(`IV_PlayerToGetStagingCoresFor`)

  set `IV_General_GetNumberOfUnitsWithTag_Units` = `OV_PlayerStagingCoresAsUnitGroup`
  set `IV_General_GetNumberOfUnitsWithTag_Tag` = sdfvanguard_snowtag
  `OV_General_GetNumberOfUnitsWithTag_Num` = General_GetNumberOfUnitsWithTag(
    `IV_General_GetNumberOfUnitsWithTag_Units`,
    `IV_General_GetNumberOfUnitsWithTag_Tag`
  )
  set `num_to_spawn` = `OV_General_GetNumberOfUnitsWithTag_Num`
  
  set `IV_General_GetNumberOfUnitsWithTag_Tag` = sdfvanguardtriple_snowtag
  `OV_General_GetNumberOfUnitsWithTag_Num` = General_GetNumberOfUnitsWithTag(
    `IV_General_GetNumberOfUnitsWithTag_Units`,
    `IV_General_GetNumberOfUnitsWithTag_Tag`
  )
  set `num_to_spawn` += `OV_General_GetNumberOfUnitsWithTag_Num`

  If(`num_to_spawn` == 0):
    General_SkipRemainingActions()

  UnitGroup_ForEachUnitInGroup(`OV_PlayerStagingCoresAsUnitGroup`):
    Unit_CreateUnit(
      `num_to_spawn`,
      Gunner_Autogate,
      Unit_GetOwningPlayer(UnitGroup_GetCurrentUnit()),
      Actor_GetPosition(UnitGroup_GetCurrentUnit()),
      true
    )
    UnitGroup_AddUnits(
      Blackboard_GetValue_UnitGroup(
        Blackboard_GetBlackboardOfEntity(UnitGroup_GetCurrentUnit()),
        `units`
      ),
      UnitGroup_GetLastCreatedUnits()
    )