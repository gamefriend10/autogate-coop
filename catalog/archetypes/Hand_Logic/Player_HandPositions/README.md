// Note: The hand position placed_name must follow the pattern "PlayerX_HandPositionY" and it must exist.
Vector GetVectorForHandPositionOfTriggeringPlayer(String `GV_OpenHandPositionToSpawnAt`)

returns: Vector for TriggeringPlayer's `GV_OpenHandPositionToSpawnAt` via `GV_HandPositionToSpawnAt`

`player_number_as_string` = String_Concat(
  "Player",
  String_ToString(Unit_GetOwningPlayer(Unit_GetTriggeringUnit()))
)

switch(`GV_OpenHandPositionToSpawnAt`)
  case "hand_position_0": `position_number_as_string` = "HandPosition1"
  repeat for "hand_position_1-5": `position_number_as_string` = "HandPosition2-6"... 
`placed_name_of_position` = String_Concat(
  `player_number_as_string`,
  "_",
  `position_number_as_string`
)
`GV_HandPositionToSpawnAt` = Actor_GetPosition(Point_GetPointFromPlacedName(`placed_name_of_position`))