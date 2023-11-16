*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***                  StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
Move in the middle of the board         3             2             1                     NORTH         3           3           2
Move from corner                        0             0             3                     NORTH         0           1           4
Move from origin SOUTH                  0             0             5                     SOUTH         0           0           6
Move from origin NORTH                  0             0             5                     NORTH         0           1           6
Move from origin WEST                   0             0             5                     WEST          0           0           6
Move from origin EAST                   0             0             5                     EAST          1           0           6
Move from 0,9 NORTH                     0             9             5                     NORTH         0           9           6
Move from 0,9 SOUTH                     0             9             5                     SOUTH         0           8           6
Move from 0,9 WEST                      0             9             5                     WEST          0           9           6
Move from 0,9 EAST                      0             9             5                     EAST          1           9           6
Move from 9,9 NORTH                     9             9             5                     NORTH         9           9           6
Move from 9,9 SOUTH                     9             9             5                     SOUTH         9           8           6
Move from 9,9 WEST                      9             9             5                     WEST          8           9           6
Move from 9,9 EAST                      9             9             5                     EAST          9           9           6
Move from 9,0 NORTH                     9             0             5                     NORTH         9           1           6
Move from 9,0 SOUTH                     9             0             5                     SOUTH         9           0           6
Move from 9,0 WEST                      9             0             5                     WEST          8           0           6
Move from 9,0 EAST                      9             0             5                     EAST          9           0           6
Move from 5,0 NORTH                     5             0             5                     NORTH         5           1           6
Move from 5,0 SOUTH                     5             0             5                     SOUTH         5           0           6
Move from 5,0 WEST                      5             0             5                     WEST          4           0           6
Move from 5,0 EAST                      5             0             5                     EAST          6           0           6
Move from 0,5 NORTH                     0             5             5                     NORTH         0           6           6
Move from 0,5 SOUTH                     0             5             5                     SOUTH         0           4           6
Move from 0,5 WEST                      0             5             5                     WEST          0           5           6
Move from 0,5 EAST                      0             5             5                     EAST          1           5           6
Move from 9,5 NORTH                     9             5             5                     NORTH         9           6           6
Move from 9,5 SOUTH                     9             5             5                     SOUTH         9           4           6
Move from 9,5 WEST                      9             5             5                     WEST          8           5           6
Move from 9,5 EAST                      9             5             5                     EAST          9           5           6
Move from 5,9 NORTH                     5             9             5                     NORTH         5           9           6
Move from 5,9 SOUTH                     5             9             5                     SOUTH         5           8           6
Move from 5,9 WEST                      5             9             5                     WEST          4           9           6
Move from 5,9 EAST                      5             9             5                     EAST          6           9           6






*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}