import random
roll = 0
def roll_dice():
    global roll
    roll = random.randint(1, 6)
while roll != 6:
    roll_dice()
    print(roll)