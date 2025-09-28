# Pass

Transfer a Hand Core from your hand to another player's hand, if there's room.

--------------------

Pass_PassHandCoreToPlayer(Player `IV_Pass_PassHandCoreToPlayer_Player`):
  // Rm self from old player's blackboard
  set `IV_RemoveHandCoreFromHandPositionInPlayerBlackboard_HandCore` = Unit_GetTriggeringUnit()
  RemoveHandCoreFromHandPositionInPlayerBlackboard(`IV_RemoveHandCoreFromHandPositionInPlayerBlackboard_HandCore`)

  // Transfer ownership of core and its units
  Unit_ChangeOwner(Unit_GetTriggeringUnit(), `IV_Pass_PassHandCoreToPlayer_Player`)
  UnitGroup_ForEachUnitInGroup(
    Blackboard_GetValue_UnitGroup(
      Blackboard_GetBlackboardOfEntity(Unit_GetTriggeringUnit()),
      "units"
    )
  ):
    Unit_ChangeOwner(UnitGroup_GetCurrentUnit(), `IV_Pass_PassHandCoreToPlayer_Player`)

  set `IV_MoveCoreToOwningPlayerHand_Core` = Unit_GetTriggeringUnit()
  MoveCoreToOwningPlayerHand(`IV_MoveCoreToOwningPlayerHand_Core`)

  // Check for triple
  set `IV_Triple_TriplifyCoreIfThreeArePresent_CoreToCheckFor` = Unit_GetTriggeringUnit()
  Triple_TriplifyCoreIfThreeArePresent(`IV_Triple_TriplifyCoreIfThreeArePresent_CoreToCheckFor`)