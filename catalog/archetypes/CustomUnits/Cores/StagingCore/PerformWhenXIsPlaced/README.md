PerformWhenXIsPlaced():
  // Perform the actions that can apply to multiple cores
  Trigger_Run(SDFVanguard_PerformWhenXIsPlaced)

  // Perform the actions that can only apply to one core, so we can end early
  If(Entity_HasAllTags(Unit_GetTriggeringUnit(), lancerarmstrong_snowtag)):
    LancerArmstrong_PerformWhenXIsPlaced()
    General_SkipRemainingActions()
  If(Entity_HasAllTags(Unit_GetTriggeringUnit(), lancerarmstrongtriple_snowtag)):
    LancerArmstrongTriple_PerformWhenXIsPlaced()
    General_SkipRemainingActions()
  If(Entity_HasAllTags(Unit_GetTriggeringUnit(), dogpack_snowtag)):
    DogPack_PerformWhenXIsPlaced()
    General_SkipRemainingActions()
  If(Entity_HasAllTags(Unit_GetTriggeringUnit(), dogpacktriple_snowtag)):
    DogPackTriple_PerformWhenXIsPlaced()
    General_SkipRemainingActions()