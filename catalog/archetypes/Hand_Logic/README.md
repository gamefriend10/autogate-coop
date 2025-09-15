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

SetHandCoreBlackboardHandPosition(String `GV_OpenHandPositionToSpawnAt`)

// Set this handcore's blackboard `hand_position` to `GV_OpenHandPositionToSpawnAt`

--------------------

RemoveHandCoreFromHandPositionInPlayerBlackboard()

1. Run this handcore's `hand_position` through a switch() to remove handCore from e.g. "hand_core_at_hand_position_0" in PlayerBlackboard