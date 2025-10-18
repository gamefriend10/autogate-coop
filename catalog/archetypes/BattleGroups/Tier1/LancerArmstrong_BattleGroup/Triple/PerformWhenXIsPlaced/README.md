// When placed, Gain 2 Veterancy Level.
LancerArmstrongTriple_PerformWhenXIsPlaced():
  Set `IV_GiveCoreUnitsVeterancy_Core` = Unit_GetTriggeringUnit()
  Set `IV_GiveCoreUnitsVeterancy_NumXP` = 200
  GiveCoreUnitsVeterancy(`IV_GiveCoreUnitsVeterancy_Core`, `IV_GiveCoreUnitsVeterancy_NumXP`)