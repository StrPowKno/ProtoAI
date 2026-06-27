
"""
Coordinates:

      x →
      0 1 2 3 4 5 6 7 8 9
    +---------------------+
y 0 | . . . . . . . . . . |
↓ 1 | . . . . . . . . . . |
  2 | . . . . . . . . . . |
  3 | . . . # . . # . . . |
  4 | . . * . . . . . . . |
  5 | . . . . . @ . . . . |   <-- Starting player position (5,5)
  6 | . . . # . . # . . . |
  7 | . . . . . . . . . . |
  8 | . . . . . . . . . . |
  9 | . . . . . . . . . E |
    +---------------------+

Legend:
@ = Player (starts at 5,5)
* = Key    (2,4)
E = Exit   (9,9)
# = Wall

Movement:
W = y - 1   (Up)
S = y + 1   (Down)
A = x - 1   (Left)
D = x + 1   (Right)

Comparisons:

goal_x < player_x  -> Goal is LEFT
goal_x > player_x  -> Goal is RIGHT

goal_y < player_y  -> Goal is UP
goal_y > player_y  -> Goal is DOWN
"""


def ai(state:dict) -> str: 
    # print(state)

    """ state = {
            "player_x": player_x,
            "player_y": player_y,
            "key_x": key_x,
            "key_y": key_y,
            "exit_x": exit_x,
            "exit_y": exit_y,
            "has_key": has_key,
        }
    """

    player_x = state["player_x"]
    player_y = state["player_y"]

    key_x = state["key_x"]
    key_y = state["key_y"]

    exit_x = state["exit_x"]
    exit_y = state["exit_y"]

    has_key = state["has_key"]


    # Defining the goal

    if has_key == False: # If want to get the key
        goal_x = key_x
        goal_y = key_y

    elif has_key:
        goal_x = exit_x
        goal_y = exit_y

    else:
        raise Exception
    

    # Defining the moves (WASD)

    if goal_x < player_x:
        return "a" # Move LEFT
    
    if goal_x > player_x:
        return "d" # Move RIGHT
    
    if goal_y < player_y:
        return "w" # Move UP
    
    if goal_y > player_y:
        return "s" # Move DOWN
        

    return ""