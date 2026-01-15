import random
import math
N = int(input())
n = 0
on = 0
while on < N:
    on += 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        n += 1
print('Approximation of pi:', 4*n/N)