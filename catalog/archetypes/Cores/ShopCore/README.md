# ShopToHandCoreTransitionTrigger

Trigger: shopCore uses ability (expected to only be Buy, which morphs ShopCore into HandCore)

1. Reposition this to next open hand position (Actor_SetPosition)
2. move shopCore's `units` (tracked by blackboard) to Actor's current position
3. Remove this shopCore from the player's blackboard
  1. (the player blackboard key to use should be saved to `shop_position_key` in this core's blackboard)
