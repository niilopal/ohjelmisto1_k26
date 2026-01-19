gallons = 0
liters = 0
def convert(gallons):
    liters = gallons * 3.785
    if liters < 0:
        print('Program finished.')
        exit()
    print(f'{gallons} American gallons is {liters:.2f} liters.')
while 1 == 1:
    convert(float(input('Enter a volume in American gallons (negative value to quit): ')))