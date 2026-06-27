import random

def ai(state):
    move = random.randint(0, 3)
    state = state # preventing crash

    if move == 0:
        return "w"
    
    elif move == 1:
        return 's'
    
    elif move == 2:
        return 'd'
    
    elif move == 3:
        return 'a'