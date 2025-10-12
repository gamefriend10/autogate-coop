// When placed, Gain 2 Veterancy Level.
LancerArmstrongTriple_PerformWhenXIsPlaced():
  Set `IV_GiveCoreAndUnitsVeterancy_Core` = Unit_GetTriggeringUnit()
  Set `IV_GiveCoreAndUnitsVeterancy_NumXP` = 200
  GiveCoreAndUnitsVeterancy(`IV_GiveCoreAndUnitsVeterancy_Core`, `IV_GiveCoreAndUnitsVeterancy_NumXP`)