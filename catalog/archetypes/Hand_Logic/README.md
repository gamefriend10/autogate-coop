# String PickFirstOpenHandPositionForPlayer()

returns: "hand_position_X" to be used in player blackboard in GlobalVar: `GV_OpenHandPositionToSpawnAt`

1. init local `player_blackboard` to Blackboard_GetBlackboardOfPlayer (always should be triggering player)
2. if Logic_NotConditions `player_blackboard` Blackboard_HasValue("hand_core_at_hand_position_0")
 1. then set `GV_OpenHandPositionToSpawnAt` to "hand_position_0"
 2. General_SkipRemainingActions
3. repeat for the rest of the 5 hand positions...

# Vector GetVectorForPlayerXHandPosition(String `GV_OpenHandPositionToSpawnAt`)

returns: vector for Player X's HandPosition Y in GlobalVar: `GV_HandPositionToSpawnAt`

1. switch(`GV_OpenHandPositionToSpawnAt`)
  1. case "hand_position_1": set `GV_HandPositionToSpawnAt` to position of Player1_HandPosition2
  2. repeat for "hand_position_2-5" Player1_HandPosition3-6... 
  3. default: set `GV_HandPositionToSpawnAt` to position of Player1_HandPosition1

# AddHandCoreToOpenHandPositionInPlayerBlackboard(String `GV_OpenHandPositionToSpawnAt`)

1. switch(`GV_OpenHandPositionToSpawnAt`)
  1. case "hand_position_1": set playerBlackboard `hand_core_at_hand_position_1` to triggeringUnit
  2. repeat for "hand_position_2-5" `hand_core_at_hand_position_2-5`... 
  3. default: set playerBlackboard `hand_core_at_hand_position_0` to triggeringUnit

# SetHandCoreBlackboardHandPosition(String `GV_OpenHandPositionToSpawnAt`)

1. Set this handcore's `hand_position` (tracked by blackboard) to `GV_OpenHandPositionToSpawnAt`

# RemoveHandCoreFromHandPositionInPlayerBlackboard()

1. Run this handcore's `hand_position` through a switch() to remove handCore from e.g. "hand_core_at_hand_position_0" in PlayerBlackboard