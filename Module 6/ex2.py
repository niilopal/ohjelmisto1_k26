import random
roll = 0
d = int(input('How many sides to a die: '))
def roll_dice(d):
    global roll
    roll = random.randint(1, d)
while roll != d:
    roll_dice(d)
    print(roll)