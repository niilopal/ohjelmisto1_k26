inches = 1
while inches >= 0:
    inches = float(input('Enter length in inches (negative value to quit): '))
    if inches >= 0:
        cm = inches * 2.54
        print(f'{inches:.1f} inches is {cm:.2f} centimeters')
    else:
        print('Program ended.')