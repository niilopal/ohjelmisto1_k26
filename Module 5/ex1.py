import random
sum = 0
for i in range(int(input('How many dice to roll: '))):
    sum += random.randint(1, 6)
print(f'Sum of the dice: {sum}')