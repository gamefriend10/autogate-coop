# Staging

Staging is laid out as a 3x3 grid with positions as follows:

|      | col0 | col1 | col2 |
|------|------|------|------|
|row2  |  20  |  21  |  22  |
|row1  |  10  |  11  |  12  |
|row0  |  00  |  01  |  02  |

The player blackboard keys should be just the indexes concatted as above e.g. exactly `00` for bottom left.

--------------------

AddStagingCoreToPlayerBlackboard(String `GV_ClosestStagingPosition`):

Blackboard_SetValue_Unit(TriggeringPlayer, `GV_ClosestStagingPosition`, TriggeringUnit)