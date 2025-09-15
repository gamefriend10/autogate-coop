// Returns String "hand_position_X" via `GV_OpenHandPositionToSpawnAt`
String PickFirstOpenHandPositionForPlayer(`IV_PickFirstOpenHandPositionForPlayer_Player`):
  `player_blackboard` = Blackboard_GetBlackboardOfPlayer(`IV_PickFirstOpenHandPositionForPlayer_Player`)
  If(!Blackboard_HasValue(`player_blackboard`, "hand_core_at_hand_position_0")):
    `GV_OpenHandPositionToSpawnAt` = "hand_position_0"
    General_SkipRemainingActions()
  repeat for the rest of the 5 hand positions...

--------------------

AddHandCoreToOpenHandPositionInPlayerBlackboard(String `GV_OpenHandPositionToSpawnAt`)

1. switch(`GV_OpenHandPositionToSpawnAt`)
  1. case "hand_position_1": set playerBlackboard `hand_core_at_hand_position_1` to triggeringUnit
  2. repeat for "hand_position_2-5" `hand_core_at_hand_position_2-5`... 
  3. default: set playerBlackboard `hand_core_at_hand_position_0` to triggeringUnit

--------------------

SetHandCoreBlackboardHandPosition(String `GV_OpenHandPositionToSpawnAt`)

// Set this handcore's blackboard `hand_position` to `GV_OpenHandPositionToSpawnAt`

--------------------

RemoveHandCoreFromHandPositionInPlayerBlackboard()

1. Run this handcore's `hand_position` through a switch() to remove handCore from e.g. "hand_core_at_hand_position_0" in PlayerBlackboard