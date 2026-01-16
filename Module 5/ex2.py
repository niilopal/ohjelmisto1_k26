x = 0
num = []
numAdd = input('Enter a number: ')
while numAdd != '':
    num.append(float(numAdd))
    numAdd = input('Enter a number: ')
num.sort(reverse=True)
print('The greatest numbers in descending order:')
for i in num:
    if x < 5:
        print(num[x])
        x += 1