
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

    WALL_PENALTY = 1000

    # Defining the functions

    def distance(x1, y1, x2, y2) -> int:
        return abs(x1 - x2) + abs(y1 - y2)
    
    def is_wall(x, y):
        return (x, y) in walls
    
    def is_inside_map(x:int, y:int) -> bool: # Coming soon
        pass

    def best_direction(tmp_player_x, tmp_player_y):
        up = distance(tmp_player_x, tmp_player_y - 1, goal_x, goal_y)
        down = distance(tmp_player_x, tmp_player_y + 1, goal_x, goal_y)
        right = distance(tmp_player_x + 1, tmp_player_y, goal_x, goal_y)
        left = distance(tmp_player_x - 1, tmp_player_y, goal_x, goal_y)

        if is_wall(tmp_player_x, tmp_player_y -1):
            up += WALL_PENALTY

        if is_wall(tmp_player_x, tmp_player_y + 1):
            down += WALL_PENALTY

        if is_wall(tmp_player_x + 1, tmp_player_y):
            right += WALL_PENALTY

        if is_wall(tmp_player_x - 1, tmp_player_y):
            left += WALL_PENALTY



        lowest_distance = min(up, down, right, left)

        if up == lowest_distance:
            return 'w'
        
        elif down == lowest_distance:
            return 's'
        
        elif right == lowest_distance:
            return 'd'
        
        elif left == lowest_distance:
            return 'a'
        







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

    walls = state["walls"]

    # Defining the goal

    if has_key == False: # If want to get the key
        goal_x = key_x
        goal_y = key_y

    elif has_key:
        goal_x = exit_x
        goal_y = exit_y

    else:
        raise ValueError("Invalid state: has_key must be True or False")
    


    return best_direction(player_x, player_y)
    


    

    # Defining the moves (WASD)

    # if goal_x < player_x:
    #     return "a" # Move LEFT
    # 
    # if goal_x > player_x:
    #     return "d" # Move RIGHT
    # 
    # if goal_y < player_y:
    #     return "w" # Move UP
    # 
    # if goal_y > player_y:
    #     return "s" # Move DOWN
        