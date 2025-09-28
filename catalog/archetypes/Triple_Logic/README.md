# Triple

When a player has 3 of a kind, they should be replaced with a triple version.

--------------------

Triple_TriplifyCoreIfThreeArePresent(Unit `IV_Triple_TriplifyCoreIfThreeArePresent_CoreToCheckFor`):
  set `GV_Triple_TriplifyCoreIfThreeArePresent_BattleGroupCountForTriple` = 0
  set `GV_Triple_TriplifyCoreIfThreeArePresent_CoreUnitGroupForTriple` = UnitGroup_GetNewUnitGroup()
  set `GV_Triple_TriplifyCoreIfThreeArePresent_TripleFound` = false

  `GV_Triple_TriplifyCoreIfThreeArePresent_TripleFound` =
    CheckStagingForTripleHelper(
      `IV_Triple_TriplifyCoreIfThreeArePresent_CoreToCheckFor`,
      `GV_Triple_TriplifyCoreIfThreeArePresent_BattleGroupCountForTriple`,
      `GV_Triple_TriplifyCoreIfThreeArePresent_CoreUnitGroupForTriple`
    )
  if not `GV_Triple_TriplifyCoreIfThreeArePresent_TripleFound`:
    CheckHandForTripleHelper(
      `IV_Triple_TriplifyCoreIfThreeArePresent_CoreToCheckFor`,
      `GV_Triple_TriplifyCoreIfThreeArePresent_BattleGroupCountForTriple`,
      `GV_Triple_TriplifyCoreIfThreeArePresent_CoreUnitGroupForTriple`
    )

--------------------

// Reuses 
//  Unit `IV_Triple_TriplifyCoreIfThreeArePresent_CoreToCheckFor`
//  Integer `GV_Triple_TriplifyCoreIfThreeArePresent_BattleGroupCountForTriple`
//  UnitGroup `GV_Triple_TriplifyCoreIfThreeArePresent_CoreUnitGroupForTriple`
// Returns `GV_Triple_TriplifyCoreIfThreeArePresent_TripleFound`
CheckStagingForTripleHelper():
  set `IV_PlayerToGetStagingCoresFor` = Unit_GetOwningPlayer(`IV_Triple_TriplifyCoreIfThreeArePresent_CoreToCheckFor`)
  `OV_PlayerStagingCoresAsUnitGroup` = GetAllStagingCoresForPlayer(`IV_PlayerToGetStagingCoresFor`)
  UnitGroup_ForEachUnitInGroup(`OV_PlayerStagingCoresAsUnitGroup`):
    If(
      Unit_GetPlacedName(`IV_Triple_TriplifyCoreIfThreeArePresent_CoreToCheckFor`) ==
      Unit_GetPlacedName(UnitGroup_GetCurrentUnit)
    ):
      `GV_Triple_TriplifyCoreIfThreeArePresent_BattleGroupCountForTriple` += 1
      UnitGroup_AddUnit(`GV_Triple_TriplifyCoreIfThreeArePresent_CoreUnitGroupForTriple`, UnitGroup_GetCurrentUnit)
    `GV_Triple_TriplifyCoreIfThreeArePresent_TripleFound` = CheckForAndReplaceNonTriplesWithTripleHelper()
    
    // I don't think the following is necessary, since we should always convert as soon as we hit 3, so we
    // should never have >3 STAGING cores to check.
    //if `GV_Triple_TriplifyCoreIfThreeArePresent_TripleFound`:
    //  SkipRemainingActions()

--------------------

// Reuses 
//  Unit `IV_Triple_TriplifyCoreIfThreeArePresent_CoreToCheckFor`
//  Integer `GV_Triple_TriplifyCoreIfThreeArePresent_BattleGroupCountForTriple`
//  UnitGroup `GV_Triple_TriplifyCoreIfThreeArePresent_CoreUnitGroupForTriple`
// Returns `GV_Triple_TriplifyCoreIfThreeArePresent_TripleFound`
CheckHandForTripleHelper():
  set `IV_GetAllHandCoresForPlayer_Player` = Unit_GetOwningPlayer(`IV_Triple_TriplifyCoreIfThreeArePresent_CoreToCheckFor`)
  `OV_GetAllHandCoresForPlayer_HandCoreUnitGroup` = GetAllHandCoresForPlayer(`IV_GetAllHandCoresForPlayer_Player`)
  UnitGroup_ForEachUnitInGroup(`OV_GetAllHandCoresForPlayer_HandCoreUnitGroup`):
    If(
      Unit_GetPlacedName(`IV_Triple_TriplifyCoreIfThreeArePresent_CoreToCheckFor`) ==
      Unit_GetPlacedName(UnitGroup_GetCurrentUnit)
    ):
      `GV_Triple_TriplifyCoreIfThreeArePresent_BattleGroupCountForTriple` += 1
      UnitGroup_AddUnit(`GV_Triple_TriplifyCoreIfThreeArePresent_CoreUnitGroupForTriple`, UnitGroup_GetCurrentUnit)
    `GV_Triple_TriplifyCoreIfThreeArePresent_TripleFound` = CheckForAndReplaceNonTriplesWithTripleHelper()
    if `GV_Triple_TriplifyCoreIfThreeArePresent_TripleFound`:
      SkipRemainingActions()

--------------------

// If there is 3 of a kind found, remove the 3 battle groups and add the triple version to the player' hand.
// Reuses 
//  Unit `IV_Triple_TriplifyCoreIfThreeArePresent_CoreToCheckFor`
//  Integer `GV_Triple_TriplifyCoreIfThreeArePresent_BattleGroupCountForTriple`
//  UnitGroup `GV_Triple_TriplifyCoreIfThreeArePresent_CoreUnitGroupForTriple`
// Returns `GV_Triple_TriplifyCoreIfThreeArePresent_TripleFound`
CheckForAndReplaceNonTriplesWithTripleHelper():
  If(`GV_Triple_TriplifyCoreIfThreeArePresent_BattleGroupCountForTriple` != 3):
    SkipRemainingActions()

  `GV_Triple_TriplifyCoreIfThreeArePresent_TripleFound` = true

  // If any are hand cores (condition on RemoveHandCoreFromHandPositionInPlayerBlackboard),
  // rm from player's blackboard, so the triple can fit in one of the newly open slots.
  // Note: okay to not rm from staging, bc deleting will rm anyway and the triple goes to the hand.
  UnitGroup_ForEachUnitInGroup(`GV_Triple_TriplifyCoreIfThreeArePresent_CoreUnitGroupForTriple`):
    `IV_RemoveHandCoreFromHandPositionInPlayerBlackboard_HandCore` = UnitGroup_GetCurrentUnit
    RemoveHandCoreFromHandPositionInPlayerBlackboard(`IV_RemoveHandCoreFromHandPositionInPlayerBlackboard_HandCore`)
  
  `IV_AddTripleVersionOfBattleGroupToHand_NonTripleCore` = `IV_Triple_TriplifyCoreIfThreeArePresent_CoreToCheckFor`
  AddTripleVersionOfBattleGroupToHand(`IV_AddTripleVersionOfBattleGroupToHand_NonTripleCore`)

  // Delete non-triple cores and their units
  UnitGroup_ForEachUnitInGroup(`GV_Triple_TriplifyCoreIfThreeArePresent_CoreUnitGroupForTriple`):
    UnitGroup_ForEachUnitInGroup(
      Blackboard_GetValue_UnitGroup(
        Blackboard_GetBlackboardOfEntity(UnitGroup_GetCurrentUnit),
        "units"
      )
    ):
      Unit_Remove(UnitGroup_GetCurrentUnit)
    Unit_Remove(UnitGroup_GetCurrentUnit)

--------------------

AddTripleVersionOfBattleGroupToHand(`IV_AddTripleVersionOfBattleGroupToHand_NonTripleCore`):
  `OV_DetermineTripleVersionOfCoreToSpawn_TripleCoreToSpawn` = 
    DetermineTripleVersionOfCoreToSpawn(`IV_AddTripleVersionOfBattleGroupToHand_NonTripleCore`)

  `IV_PickFirstOpenHandPositionForPlayer_Player` =
    Unit_GetOwningPlayer(`IV_AddTripleVersionOfBattleGroupToHand_NonTripleCore`)
  `GV_OpenHandPositionToSpawnAt` = PickFirstOpenHandPositionForPlayer(`IV_PickFirstOpenHandPositionForPlayer_Player`)
  `GV_HandPositionToSpawnAt` = GetVectorForHandPositionOfTriggeringPlayer(`GV_OpenHandPositionToSpawnAt`)

  Unit_CreateUnit(
    1,
    `OV_DetermineTripleVersionOfCoreToSpawn_TripleCoreToSpawn`,
    `IV_PickFirstOpenHandPositionForPlayer_Player`,
    `GV_HandPositionToSpawnAt`,
    true
  )
  `IV_Core_SpawnUnits_CoreToAttachUnitsTo` = Unit_GetLastCreatedUnit()

  // Save to tripleHandCore's Blackboard its own index position in the hand
  Blackboard_SetValue_String(
    Blackboard_GetBlackboardOfEntity(`IV_Core_SpawnUnits_CoreToAttachUnitsTo`),
    "hand_position",
    `GV_OpenHandPositionToSpawnAt`
  )

  `IV_AddHandCoreToOpenHandPositionInPlayerBlackboard_Player` = `IV_PickFirstOpenHandPositionForPlayer_Player`
  AddHandCoreToOpenHandPositionInPlayerBlackboard(
    `GV_OpenHandPositionToSpawnAt`,
    `IV_AddHandCoreToOpenHandPositionInPlayerBlackboard_Player`
  )

  `IV_Core_SpawnUnits_CoreToSpawn` = Unit_GetType(`IV_Core_SpawnUnits_CoreToAttachUnitsTo`)
  (`GV_LengthOfUnitDataToSpawnArray`, `GV_UnitDataToSpawnArray`, `GV_NumOfUnitsToSpawnForEachUnitDataArray`) = 
    SetVarsForCoreSpawnUnits(`IV_Core_SpawnUnits_CoreToSpawn`)
  `IV_Core_SpawnUnits_PlayerToSpawnFor` = `IV_PickFirstOpenHandPositionForPlayer_Player`
  Core_SpawnUnits(
    `GV_LengthOfUnitDataToSpawnArray`,
    `GV_UnitDataToSpawnArray`,
    `GV_NumOfUnitsToSpawnForEachUnitDataArray`,
    `IV_Core_SpawnUnits_PlayerToSpawnFor`,
    `IV_Core_SpawnUnits_CoreToAttachUnitsTo`
  )

--------------------

// Reuses `IV_AddTripleVersionOfBattleGroupToHand_NonTripleCore`
// Returns `OV_DetermineTripleVersionOfCoreToSpawn_TripleCoreToSpawn`
DetermineTripleVersionOfCoreToSpawn():
  If(Entity_HasAllTags(`IV_AddTripleVersionOfBattleGroupToHand_NonTripleCore`, lancerarmstrong_snowtag)):
    `OV_DetermineTripleVersionOfCoreToSpawn_TripleCoreToSpawn` = LancerArmstrongTriple_HandCore
    SkipRemainingActions()
  repeat for all hand cores...
