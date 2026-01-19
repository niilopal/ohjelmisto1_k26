integ = int(input('Enter an integer: '))
n = 1
div = 0
for i in range(integ):
    if integ % n == 0:
        div += 1
    n += 1
if div == 2:
    print(f'{integ} is a prime number.')
else:
    print(f'{integ} is not a prime number.')