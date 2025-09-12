# ShopTopBarAbilityCastedTrigger

triggers when: anyone's topbar casts ability

1. if triggering ability was tier2
  1. set tier to 2 for TODO: triggering player
  2. set tier2 ability to disabled for triggering player

1. if triggering ability was refresh
  `GV_PlayerToRefreshFor` = Unit_GetOwningPlayer(Unit_GetTriggeringUnit())
  RefreshForPlayer(`GV_PlayerToRefreshFor`)

If triggering ability was ReadyUp
  Trigger_Run(ReadyUp_Trigger)

If triggering ability was UnreadyUp:
  `GV_PlayerToUnreadyUp` = Unit_GetOwningPlayer(Unit_GetTriggeringUnit())
  UnreadyUp_Trigger(`GV_PlayerToUnreadyUp`)

