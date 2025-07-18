# Shop Selection Core

Buy Logic
1. Buy Ability triggers morph ability into Hand Selection Core
2. Shop Selection Core performs any ability (Unit_OnAbilityUsed)
    1. Reposition this to next open hand position (Actor_SetPosition)
    2. Set pos var to spawn at
    3. Run GeneralCoreSpawn trigger
    4. TODO: Add the spawned units to this core's blackboard?
