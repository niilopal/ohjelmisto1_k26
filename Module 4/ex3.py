num = 1
x = 0
while str(num) != '':
    num = input('Enter a number (or press Enter to quit): ')
    if str(num) != '':
        num = float(num)
        if x == 0:
            ln = num
            sn = num
            x += 1
        if num < sn:
            sn = num
        if num > ln:
            ln = num
print(f'Smallest number: {sn:.1f}')
print(f'Largest number: {ln:.1f}')