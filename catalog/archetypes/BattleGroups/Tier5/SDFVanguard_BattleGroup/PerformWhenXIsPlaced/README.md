// When a Vanguard Battle Group is placed, add 1 Exo
// to every adjacent (diagonal included) Battle Group.
// Note: also handles sdfvanguard triple
SDFVanguard_PerformWhenXIsPlaced():
  // Note: It would be more efficient to put this check one level up, but harder to reason about
  If(Entity_HasNoneTags(Unit_GetTriggeringUnit(), vanguard_snowtag)):
    General_SkipRemainingActions()
  
  set `IV_PlayerToGetStagingCoresFor` = Unit_GetOwningPlayer(Unit_GetTriggeringUnit())
  `OV_PlayerStagingCoresAsUnitGroup` = GetAllStagingCoresForPlayer(`IV_PlayerToGetStagingCoresFor`)

  // Add sdf cores to `sdfs` unit group
  Set `sdfs` = UnitGroup_GetNewUnitGroup()
  UnitGroup_ForEachUnitInGroup(`OV_PlayerStagingCoresAsUnitGroup`):
    // Need an if for every tag bc compiled code for HasAllTags wont accept a ref to a SnowTag, only a SnowTag itself
    If(Entity_HasAllTags(UnitGroup_GetCurrentUnit(), sdfvanguard_snowtag)):
      UnitGroup_AddUnit(`sdfs`, UnitGroup_GetCurrentUnit())
      General_Continue()
    If(Entity_HasAllTags(UnitGroup_GetCurrentUnit(), sdfvanguardtriple_snowtag)):
      UnitGroup_AddUnit(`sdfs`, UnitGroup_GetCurrentUnit())
      General_Continue()
  
  // For each sdf, spawn 1 or 2 exos in adjacent BGs
  UnitGroup_ForEachUnitInGroup(`sdfs`):
    set `num_to_spawn` = 1
    If(Entity_HasAllTags(UnitGroup_GetCurrentUnit(), sdfvanguardtriple_snowtag)):
      set `num_to_spawn` = 2
    set `IV_Staging_GetAdjacentStagingCores_Core` = UnitGroup_GetCurrentUnit()
    `OV_Staging_GetAdjacentStagingCores_Cores` = Staging_GetAdjacentStagingCores(`IV_Staging_GetAdjacentStagingCores_Core`)
    UnitGroup_ForEachUnitInGroup(`OV_Staging_GetAdjacentStagingCores_Cores`):
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