// Returns Integer `OV_General_GetNumberOfUnitsWithTag_Num`
General_GetNumberOfUnitsWithTag(
  UnitGroup `IV_General_GetNumberOfUnitsWithTag_Units`,
  SnowTag `IV_General_GetNumberOfUnitsWithTag_Tag`
):
  set `OV_General_GetNumberOfUnitsWithTag_Num` = 0
  UnitGroup_ForEachUnitInGroup(`IV_General_GetNumberOfUnitsWithTag_Units`):
    // Need an if for every tag bc compiled code for HasAllTags wont accept a ref to a SnowTag, only a SnowTag itself
    If(`IV_General_GetNumberOfUnitsWithTag_Tag` == lancerarmstrong_snowtag):
      If(Entity_HasAllTags(UnitGroup_GetCurrentUnit(), lancerarmstrong_snowtag)):
        `OV_General_GetNumberOfUnitsWithTag_Num` += 1
        General_Continue()
    If(`IV_General_GetNumberOfUnitsWithTag_Tag` == lancerarmstrongtriple_snowtag):
      If(Entity_HasAllTags(UnitGroup_GetCurrentUnit(), lancerarmstrongtriple_snowtag)):
        `OV_General_GetNumberOfUnitsWithTag_Num` += 1
        General_Continue()
    If(`IV_General_GetNumberOfUnitsWithTag_Tag` == loveletter_snowtag):
      If(Entity_HasAllTags(UnitGroup_GetCurrentUnit(), loveletter_snowtag)):
        `OV_General_GetNumberOfUnitsWithTag_Num` += 1
        General_Continue()
    If(`IV_General_GetNumberOfUnitsWithTag_Tag` == lovelettertriple_snowtag):
      If(Entity_HasAllTags(UnitGroup_GetCurrentUnit(), lovelettertriple_snowtag)):
        `OV_General_GetNumberOfUnitsWithTag_Num` += 1
        General_Continue()
    If(`IV_General_GetNumberOfUnitsWithTag_Tag` == vanguard_snowtag):
      If(Entity_HasAllTags(UnitGroup_GetCurrentUnit(), vanguard_snowtag)):
        `OV_General_GetNumberOfUnitsWithTag_Num` += 1
        General_Continue()