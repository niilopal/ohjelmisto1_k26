def get_season(month):
    if month > 12 or month < 1:
        print(f"You entered: {month}")
        print("Please enter a number between 1 and 12.")
    else:
        if month == 1 or month == 2 or month == 12:
            print(f"You entered: {month}")
            print('The season is winter.')
        elif month == 3 or month == 4 or month == 5:
            print(f"You entered: {month}")
            print('The season is spring.')
        elif month == 6 or month == 7 or month == 8:
            print(f"You entered: {month}")
            print('The season is summer.')
        elif month == 9 or month == 10 or month == 11:
            print(f"You entered: {month}")
            print('The season is autumn.')
month = int(input("Enter the number of a month (1-12): "))
get_season(month)