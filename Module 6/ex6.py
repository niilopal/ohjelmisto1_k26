import math
def calculate_unit_price(pd, pp):
    pr = pd / 2
    pa = math.pi * pr ** 2
    pa = pa / 10000
    pv = pp / pa
    return pv
fpd = float(input('Enter the diameter of the first pizza (cm): '))
fpp = float(input('Enter the price of the first pizza (euros): '))
spd = float(input('Enter the diameter of the second pizza (cm): '))
spp = float(input('Enter the price of the second pizza (euros): '))
fpv = calculate_unit_price(fpd, fpp)
print(f'Unit price of the first pizza: {fpv:.2f} euros/m²')
spv = calculate_unit_price(spd, spp)
print(f'Unit price of the second pizza: {spv:.2f} euros/m²')
if fpv > spv:
    print('The second pizza provides better value for money.')
else:
    print('The first pizza provides better value for money.')