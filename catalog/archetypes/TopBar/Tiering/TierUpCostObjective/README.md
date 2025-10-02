## Global Vars ----------

Init `GV_TierUpCost_ObjectiveList` = Objectives_List_Create("Tier Up Costs")

Init `GV_Player1TierUpCost_Objective` = Objectives_Objective_Create("Player 1's Current Tier | Next Tier Cost:", "1 | 5")

Init `GV_Player2TierUpCost_Objective` = Objectives_Objective_Create("Player 2's Current Tier | Next Tier Cost:", "1 | 5")

Init `GV_Player3TierUpCost_Objective` = Objectives_Objective_Create("Player 3's Current Tier | Next Tier Cost:", "1 | 5")

Init `GV_Player4TierUpCost_Objective` = Objectives_Objective_Create("Player 4's Current Tier | Next Tier Cost:", "1 | 5")

## Functions ----------

InitTierUpCostObjective_Trigger():
  Objectives_List_AddObjective(`GV_TierUpCost_ObjectiveList`, `GV_Player1TierUpCost_Objective`)
  Objectives_List_AddObjective(`GV_TierUpCost_ObjectiveList`, `GV_Player2TierUpCost_Objective`)
  Objectives_List_AddObjective(`GV_TierUpCost_ObjectiveList`, `GV_Player3TierUpCost_Objective`)
  Objectives_List_AddObjective(`GV_TierUpCost_ObjectiveList`, `GV_Player4TierUpCost_Objective`)
  Objectives_Panel_AddList(`GV_TierUpCost_ObjectiveList`)

--------------------

UpdateTierUpCostObjective_Trigger():
  Objectives_Objective_SetDetails(
    `GV_Player1TierUpCost_Objective`,
    String_FormatString(
      "{0} | {1}",
      Blackboard_GetValue_Integer(
        Blackboard_GetBlackboardOfPlayer(PlayerGroup_GetCurrentPlayer()),
        "shop_tier"
      ),
      Blackboard_GetValue_Integer(
        Blackboard_GetBlackboardOfPlayer(1),
        "next_shop_tier_cost"
      )
    )
  )
  TODO:
  Objectives_Objective_SetDetails(
    `GV_Player2TierUpCost_Objective`,
    Blackboard_GetValue_Integer(
      Blackboard_GetBlackboardOfPlayer(2),
      "next_shop_tier_cost"
    )
  )
  Objectives_Objective_SetDetails(
    `GV_Player3TierUpCost_Objective`,
    Blackboard_GetValue_Integer(
      Blackboard_GetBlackboardOfPlayer(3),
      "next_shop_tier_cost"
    )
  )
  Objectives_Objective_SetDetails(
    `GV_Player4TierUpCost_Objective`,
    Blackboard_GetValue_Integer(
      Blackboard_GetBlackboardOfPlayer(4),
      "next_shop_tier_cost"
    )
  )