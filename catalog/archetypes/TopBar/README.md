// triggers when: anyone's topbar casts ability
ShopTopBarAbilityCastedTrigger():
  if triggering ability was refresh:
    `GV_PlayerToRefreshFor` = Unit_GetOwningPlayer(Unit_GetTriggeringUnit())
    RefreshForPlayer(`GV_PlayerToRefreshFor`)
    SkipRemainingActions()

  If triggering ability was ReadyUp:
    Trigger_Run(ReadyUp_Trigger)
    SkipRemainingActions()

  If triggering ability was UnreadyUp:
    `GV_PlayerToUnreadyUp` = Unit_GetOwningPlayer(Unit_GetTriggeringUnit())
    UnreadyUp_Trigger(`GV_PlayerToUnreadyUp`)
    SkipRemainingActions()

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
    // enable tier3 ability for triggering player
    TechTree_SetAbilityAllowed(
      Unit_GetOwningPlayer(Unit_GetTriggeringUnit()),
      Tier3Upgrade,
      add
    )
    Blackboard_SetValue_Integer(
      Blackboard_GetBlackboardOfPlayer(PlayerGroup_GetCurrentPlayer()),
      "next_shop_tier_cost",
      7
    )
    SkipRemainingActions()

  If(Ability_GetTriggeringAbility == Tier3Upgrade):
    Blackboard_SetValue_Integer(
      Blackboard_GetBlackboardOfPlayer(),
      "shop_tier",
      3
    )
    // disable tier3 ability for triggering player
    TechTree_SetAbilityAllowed(
      Unit_GetOwningPlayer(Unit_GetTriggeringUnit()),
      Tier3Upgrade,
      remove
    )
    // enable tier4 ability for triggering player
    TechTree_SetAbilityAllowed(
      Unit_GetOwningPlayer(Unit_GetTriggeringUnit()),
      Tier4Upgrade,
      add
    )
    Blackboard_SetValue_Integer(
      Blackboard_GetBlackboardOfPlayer(PlayerGroup_GetCurrentPlayer()),
      "next_shop_tier_cost",
      8
    )
    SkipRemainingActions()

  If(Ability_GetTriggeringAbility == Tier4Upgrade):
    Blackboard_SetValue_Integer(
      Blackboard_GetBlackboardOfPlayer(),
      "shop_tier",
      4
    )
    // disable tier4 ability for triggering player
    TechTree_SetAbilityAllowed(
      Unit_GetOwningPlayer(Unit_GetTriggeringUnit()),
      Tier4Upgrade,
      remove
    )
    // enable tier5 ability for triggering player
    TechTree_SetAbilityAllowed(
      Unit_GetOwningPlayer(Unit_GetTriggeringUnit()),
      Tier5Upgrade,
      add
    )
    Blackboard_SetValue_Integer(
      Blackboard_GetBlackboardOfPlayer(PlayerGroup_GetCurrentPlayer()),
      "next_shop_tier_cost",
      9
    )
    SkipRemainingActions()

  If(Ability_GetTriggeringAbility == Tier5Upgrade):
    Blackboard_SetValue_Integer(
      Blackboard_GetBlackboardOfPlayer(),
      "shop_tier",
      5
    )
    // disable tier5 ability for triggering player
    TechTree_SetAbilityAllowed(
      Unit_GetOwningPlayer(Unit_GetTriggeringUnit()),
      Tier5Upgrade,
      remove
    )
    // enable tier6 ability for triggering player
    TechTree_SetAbilityAllowed(
      Unit_GetOwningPlayer(Unit_GetTriggeringUnit()),
      Tier6Upgrade,
      add
    )
    Blackboard_SetValue_Integer(
      Blackboard_GetBlackboardOfPlayer(PlayerGroup_GetCurrentPlayer()),
      "next_shop_tier_cost",
      11
    )
    SkipRemainingActions()

  If(Ability_GetTriggeringAbility == Tier6Upgrade):
    Blackboard_SetValue_Integer(
      Blackboard_GetBlackboardOfPlayer(),
      "shop_tier",
      6
    )
    // disable tier6 ability for triggering player
    TechTree_SetAbilityAllowed(
      Unit_GetOwningPlayer(Unit_GetTriggeringUnit()),
      Tier6Upgrade,
      remove
    )
    SkipRemainingActions()
