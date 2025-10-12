// When placed, Gain 1 Veterancy Level.
LancerArmstrong_PerformWhenXIsPlaced():
  Set `IV_GiveCoreAndUnitsVeterancy_Core` = Unit_GetTriggeringUnit()
  Set `IV_GiveCoreAndUnitsVeterancy_NumXP` = 100
  GiveCoreAndUnitsVeterancy(`IV_GiveCoreAndUnitsVeterancy_Core`, `IV_GiveCoreAndUnitsVeterancy_NumXP`)