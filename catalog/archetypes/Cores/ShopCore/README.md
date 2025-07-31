# ShopToHandCoreTransitionTrigger

Trigger: shopCore uses ability (expected to only be Buy, which morphs ShopCore into HandCore)

1. Reposition this to next open hand position (Actor_SetPosition)
2. move shopCore's `units` (tracked by blackboard) to Actor's current position
