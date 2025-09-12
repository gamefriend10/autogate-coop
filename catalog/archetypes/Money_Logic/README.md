# Money

--------------------

AddMaxLumForPlayer_Trigger(`IV_NumberOfMaxLumToAdd`, `IV_PlayerToAddMaxLumTo`):
  `IV_PlayerToGetMaxLumOf` = `IV_PlayerToAddMaxLumTo`
  `OV_MaxLumOfPlayer` = GetMaxLumForPlayer_Trigger(`IV_PlayerToGetMaxLumOf`)
  `IV_NumberOfMaxLumToSet` = `OV_MaxLumOfPlayer` + `IV_NumberOfMaxLumToAdd`
  `IV_PlayerToSetMaxLumFor` = `IV_PlayerToAddMaxLumTo`
  SetMaxLumForPlayer_Trigger(`IV_NumberOfMaxLumToSet`, `IV_PlayerToSetMaxLumFor`)

--------------------

SetMaxLumForPlayer_Trigger(`IV_NumberOfMaxLumToSet`, `IV_PlayerToSetMaxLumFor`):
  Blackboard_SetValue_Integer(
    Blackboard_GetBlackboardOfPlayer(`IV_PlayerToSetMaxLumFor`),
    "maxLum",
    `IV_NumberOfMaxLumToSet`
  )

--------------------

ResetPlayerLumToTheirMax(`IV_PlayerToResetLumFor`):
  `IV_PlayerToGetMaxLumOf` = `IV_PlayerToResetLumFor`
  `OV_MaxLumOfPlayer` = GetMaxLumForPlayer_Trigger(`IV_PlayerToGetMaxLumOf`)
  Player_SetPropertyValue(
    `OV_MaxLumOfPlayer`,
    `IV_PlayerToResetLumFor`,
    PlayerProperty_ResourceA
  )

--------------------

// Returns `OV_MaxLumOfPlayer`
GetMaxLumForPlayer_Trigger(`IV_PlayerToGetMaxLumOf`):
  `OV_MaxLumOfPlayer` = Blackboard_GetValue_Integer(
    Blackboard_GetBlackboardOfPlayer(`IV_PlayerToGetMaxLumOf`),
    "maxLum"
  )