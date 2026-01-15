import random
rn = random.randint(1,10)
gn = 0
while gn != rn:
    gn = int(input('Guess a number (1-10): '))
    if gn != rn:
        if gn < rn:
            print('Too low')
        elif gn > rn:
            print('Too high')
    elif gn == rn:
        print('Correct')