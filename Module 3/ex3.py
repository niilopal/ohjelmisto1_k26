sex = input('Enter biological gender (male/female): ')
sex = sex.lower()
hem = float(input('Enter hemoglobin value (g/l): '))
if sex == 'female':
    if hem < 117:
        print('Your hemoglobin is low.')
    elif hem > 155:
        print('Your hemoglobin is high.')
    else:
        print('Your hemoglobin is normal.')
elif sex == 'male':
    if hem < 134:
        print('Your hemoglobin is low.')
    elif hem > 167:
        print('Your hemoglobin is high.')
    else:
        print('Your hemoglobin is normal.')
else:
    print('Invalid gender.')