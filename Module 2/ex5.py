talents = float(input('Enter talents: '))
pounds = float(input('Enter pounds: '))
lots = float(input('Enter lots: '))
total_grams = talents * 8512 + pounds * 425.6 + lots * 13.30
kilograms = total_grams // 1000
remaining_grams = round(total_grams % 1000, 2)

print('The weight in modern units:')
print(f'{kilograms:.0f} kilograms and {remaining_grams:.2f} grams.')