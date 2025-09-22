// Returns String "hand_position_X" via `GV_OpenHandPositionToSpawnAt`
String PickFirstOpenHandPositionForPlayer(`IV_PickFirstOpenHandPositionForPlayer_Player`):
  `player_blackboard` = Blackboard_GetBlackboardOfPlayer(`IV_PickFirstOpenHandPositionForPlayer_Player`)
  If(!Blackboard_HasValue(`player_blackboard`, "hand_core_at_hand_position_0")):
    `GV_OpenHandPositionToSpawnAt` = "hand_position_0"
    General_SkipRemainingActions()
  repeat for the rest of the 5 hand positions...

--------------------

AddHandCoreToOpenHandPositionInPlayerBlackboard(
  String `GV_OpenHandPositionToSpawnAt`
  Player `IV_AddHandCoreToOpenHandPositionInPlayerBlackboard_Player`
):
  `player_blackboard` = Blackboard_GetBlackboardOfPlayer(`IV_AddHandCoreToOpenHandPositionInPlayerBlackboard_Player`)
  Switch(`GV_OpenHandPositionToSpawnAt`):
    case "hand_position_1": Blackboard_SetValue_Unit(
      `player_blackboard`,
      "hand_core_at_hand_position_1",
      Unit_GetTriggeringUnit()
    )
    repeat for "hand_position_2-5" `hand_core_at_hand_position_2-5`... 
    default: Blackboard_SetValue_Unit(
      `player_blackboard`,
      "hand_core_at_hand_position_0",
      Unit_GetTriggeringUnit()
    )

--------------------

// Use this handcore's blackboard value at `hand_position` e.g. "hand_position_0" to rm itself from
// the handcore's owning player's PlayerBlackboard key e.g. `hand_core_at_hand_position_0`
// Conditions: Entity_HasAllTags(`IV_RemoveHandCoreFromHandPositionInPlayerBlackboard_HandCore`, handcore_snowtag)
RemoveHandCoreFromHandPositionInPlayerBlackboard(
  Unit `IV_RemoveHandCoreFromHandPositionInPlayerBlackboard_HandCore`
):
  `player_blackboard` = Blackboard_GetBlackboardOfPlayer(
    Unit_GetOwningPlayer(`IV_RemoveHandCoreFromHandPositionInPlayerBlackboard_HandCore`)
  )
  Switch(
    Blackboard_GetValue_String(
      Blackboard_GetBlackboardOfEntity(`IV_RemoveHandCoreFromHandPositionInPlayerBlackboard_HandCore`),
      "hand_position"
    )
  ):
    case "hand_position_1": Blackboard_RemoveValue(
      `player_blackboard`,
      "hand_core_at_hand_position_1"
    )
    etc.
  