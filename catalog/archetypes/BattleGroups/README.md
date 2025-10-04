# Battle Groups

## Adding a battle group

1. Create a base core and inherit from this. This controls the name for all.
2. Create snow tag for battle group.
3. Create units for the battle group. Copy over flags from other groups (uncommandable) and rename the ID.
4. Create SetVarsFor_XXX_ShopCore_SpawnUnits function.
5. Create shop>hand morph and shop core. Use morph ability in shop core and add tags.
6. Create hand>staging construct and hand core. Use construct ability in hand core and add tags. Set build cost.
7. Create staging core. Add sell ability. Set build cost and footprint.

## When adding to/removing from the battle group arrays, 
1. update the length var of all affected battleGroup arrays (its own tier AND up)
  1. BOTH the array_size of the var itself AND 
  2. the var keeping track of the length e.g. LengthOfTier2AndBelowBattleGroups
2. add/remove the battleGroup's ShopCore to/from GeneralShopCoreSpawn 
3. add/remove the battleGroup's ShopCore to/from SetVarsForCoreSpawnUnits
4. add/rm tag to General_GetNumberOfUnitsWithTag
5. if there's a PerformEndOfBuyPhase, add/rm to BuyPhase_PerformEndOfBuyPhase

## When adding a triple
1. copy the battle group + rename all the files
2. rename the base core's name
3. double the units spawned in the SetVarsFor trigger
4. add/remove the battleGroup's HandCore to/from SetVarsForCoreSpawnUnits
5. add/remove the snowtag and HandCore to/from DetermineTripleVersionOfCoreToSpawn
6. add/rm tag to General_GetNumberOfUnitsWithTag
5. if there's a PerformEndOfBuyPhase, add/rm to BuyPhase_PerformEndOfBuyPhase