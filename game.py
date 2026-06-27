import os
import time


def run_game(ai_func, sleep):

    WIDTH = 10
    HEIGHT = 10

    player_x = 5
    player_y = 5

    key_x = 2
    key_y = 4

    exit_x = 9
    exit_y = 9

    has_key = False
    running = True


    def clear():
        os.system("cls" if os.name == "nt" else "clear")


    def is_wall(x, y):
        return (x, y) in [
            (3, 3),
            (6, 3),
            (3, 6),
            (6, 6),
            (3, 4),
        ]


    while running:
        clear()

        for y in range(HEIGHT):
            for x in range(WIDTH):

                if (x, y) == (player_x, player_y):
                    print("@", end=" ")

                elif is_wall(x, y):
                    print("#", end=" ")

                elif (x, y) == (key_x, key_y) and not has_key:
                    print("*", end=" ")

                elif (x, y) == (exit_x, exit_y):
                    print("E", end=" ")

                else:
                    print(".", end=" ")

            print()


        state = {
            "player_x": player_x,
            "player_y": player_y,
            "key_x": key_x,
            "key_y": key_y,
            "exit_x": exit_x,
            "exit_y": exit_y,
            "has_key": has_key,
            "walls": [
                (3, 3),
                (6, 3),
                (6, 6),
                (3, 6),
                (3, 4),
            ]
        }


        move = ai_func(state)   # Change to `ai_func(state)` for using AI and change it to `input("\nMove (WASD): ").lower()` for manual input
 
        new_x = player_x
        new_y = player_y

        if move == "w":
            new_y -= 1
        elif move == "s":
            new_y += 1
        elif move == "a":
            new_x -= 1
        elif move == "d":
            new_x += 1
        
        time.sleep(sleep)  # Add a small delay to make the game more playable

        # Stay inside the map
        if 0 <= new_x < WIDTH and 0 <= new_y < HEIGHT:
            if not is_wall(new_x, new_y):
                player_x = new_x
                player_y = new_y

        # Pick up key
        if (player_x, player_y) == (key_x, key_y):
            has_key = True

        # Reach exit
        if (player_x, player_y) == (exit_x, exit_y):
            if has_key:
                running = False
            else:
                input("\nYou need the key! Press Enter...")

    print("\nYou won!")



if __name__ == "__main__":
    print("Please run main.py!")