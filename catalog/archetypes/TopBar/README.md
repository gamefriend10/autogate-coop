// triggers when: anyone's topbar casts ability
ShopTopBarAbilityCastedTrigger():
  If(Ability_GetTriggeringAbility == Tier2Upgrade):
    Blackboard_SetValue_Integer(
      Blackboard_GetBlackboardOfPlayer(),
      "shop_tier",
      2
    )
    // disable tier2 ability for triggering player
    TechTree_SetAbilityAllowed(
      Unit_GetOwningPlayer(Unit_GetTriggeringUnit()),
      Tier2Upgrade,
      remove
    )
  
  if triggering ability was refresh:
    `GV_PlayerToRefreshFor` = Unit_GetOwningPlayer(Unit_GetTriggeringUnit())
    RefreshForPlayer(`GV_PlayerToRefreshFor`)

  If triggering ability was ReadyUp:
    Trigger_Run(ReadyUp_Trigger)

  If triggering ability was UnreadyUp:
    `GV_PlayerToUnreadyUp` = Unit_GetOwningPlayer(Unit_GetTriggeringUnit())
    UnreadyUp_Trigger(`GV_PlayerToUnreadyUp`)
