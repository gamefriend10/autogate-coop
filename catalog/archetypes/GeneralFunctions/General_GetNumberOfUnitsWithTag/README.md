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
    If(`IV_General_GetNumberOfUnitsWithTag_Tag` == dogpack_snowtag):
      If(Entity_HasAllTags(UnitGroup_GetCurrentUnit(), dogpack_snowtag)):
        `OV_General_GetNumberOfUnitsWithTag_Num` += 1
        General_Continue()
    If(`IV_General_GetNumberOfUnitsWithTag_Tag` == dogpacktriple_snowtag):
      If(Entity_HasAllTags(UnitGroup_GetCurrentUnit(), dogpacktriple_snowtag)):
        `OV_General_GetNumberOfUnitsWithTag_Num` += 1
        General_Continue()
    If(`IV_General_GetNumberOfUnitsWithTag_Tag` == dogpackbeta_snowtag):
      If(Entity_HasAllTags(UnitGroup_GetCurrentUnit(), dogpackbeta_snowtag)):
        `OV_General_GetNumberOfUnitsWithTag_Num` += 1
        General_Continue()
    If(`IV_General_GetNumberOfUnitsWithTag_Tag` == dogpackbetatriple_snowtag):
      If(Entity_HasAllTags(UnitGroup_GetCurrentUnit(), dogpackbetatriple_snowtag)):
        `OV_General_GetNumberOfUnitsWithTag_Num` += 1
        General_Continue()
    If(`IV_General_GetNumberOfUnitsWithTag_Tag` == bunkerrush_snowtag):
      If(Entity_HasAllTags(UnitGroup_GetCurrentUnit(), bunkerrush_snowtag)):
        `OV_General_GetNumberOfUnitsWithTag_Num` += 1
        General_Continue()
    If(`IV_General_GetNumberOfUnitsWithTag_Tag` == bunkerrushtriple_snowtag):
      If(Entity_HasAllTags(UnitGroup_GetCurrentUnit(), bunkerrushtriple_snowtag)):
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
    If(`IV_General_GetNumberOfUnitsWithTag_Tag` == bedtech_snowtag):
      If(Entity_HasAllTags(UnitGroup_GetCurrentUnit(), bedtech_snowtag)):
        `OV_General_GetNumberOfUnitsWithTag_Num` += 1
        General_Continue()
    If(`IV_General_GetNumberOfUnitsWithTag_Tag` == bedtechtriple_snowtag):
      If(Entity_HasAllTags(UnitGroup_GetCurrentUnit(), bedtechtriple_snowtag)):
        `OV_General_GetNumberOfUnitsWithTag_Num` += 1
        General_Continue()
    If(`IV_General_GetNumberOfUnitsWithTag_Tag` == blockhead_snowtag):
      If(Entity_HasAllTags(UnitGroup_GetCurrentUnit(), blockhead_snowtag)):
        `OV_General_GetNumberOfUnitsWithTag_Num` += 1
        General_Continue()
    If(`IV_General_GetNumberOfUnitsWithTag_Tag` == blockheadtriple_snowtag):
      If(Entity_HasAllTags(UnitGroup_GetCurrentUnit(), blockheadtriple_snowtag)):
        `OV_General_GetNumberOfUnitsWithTag_Num` += 1
        General_Continue()
    If(`IV_General_GetNumberOfUnitsWithTag_Tag` == sdfvanguard_snowtag):
      If(Entity_HasAllTags(UnitGroup_GetCurrentUnit(), sdfvanguard_snowtag)):
        `OV_General_GetNumberOfUnitsWithTag_Num` += 1
        General_Continue()
    If(`IV_General_GetNumberOfUnitsWithTag_Tag` == sdfvanguardtriple_snowtag):
      If(Entity_HasAllTags(UnitGroup_GetCurrentUnit(), sdfvanguardtriple_snowtag)):
        `OV_General_GetNumberOfUnitsWithTag_Num` += 1
        General_Continue()
    If(`IV_General_GetNumberOfUnitsWithTag_Tag` == vanguard_snowtag):
      If(Entity_HasAllTags(UnitGroup_GetCurrentUnit(), vanguard_snowtag)):
        `OV_General_GetNumberOfUnitsWithTag_Num` += 1
        General_Continue()