// Use this stagingcore's blackboard value at `row` and `col` e.g. "0" to rm itself from
// the stagingcore's owning player's PlayerBlackboard key e.g. `00`
// Conditions: Entity_HasAllTags(`IV_RemoveStagingCoreFromPlayerBlackboard_Core`, stagingcore_snowtag)
RemoveStagingCoreFromPlayerBlackboard(
  Unit `IV_RemoveStagingCoreFromPlayerBlackboard_Core`
):
  `rowcol` = String_Concat(
    Blackboard_GetValue_String(
      Blackboard_GetBlackboardOfEntity(`IV_RemoveStagingCoreFromPlayerBlackboard_Core`),
      "row"
    ),
    Blackboard_GetValue_String(
      Blackboard_GetBlackboardOfEntity(`IV_RemoveStagingCoreFromPlayerBlackboard_Core`),
      "col"
    )
  )
  Blackboard_RemoveValue(
    Blackboard_GetBlackboardOfPlayer(
      Unit_GetOwningPlayer(`IV_RemoveStagingCoreFromPlayerBlackboard_Core`)
    ),
    `rowcol`
  )