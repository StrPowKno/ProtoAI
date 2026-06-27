from game import run_game
from protoai import ai

try:
    c = float(input("Enter the amount of time.sleep() \n > "))
except ValueError:
    print("Please enter a valid float number!")

run_game(ai, c)