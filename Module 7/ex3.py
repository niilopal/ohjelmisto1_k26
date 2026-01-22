airports = dict()
def adda():
    global airports
    ICAO = input('Enter the ICAO code: ')
    airport = input('Enter the airport name: ')
    airports.update({ICAO: airport})
    print(f'Airport {airport} with ICAO code {ICAO} has been added.')
def fetcha():
    global airports
    fetch = input('Enter the ICAO code: ')
    if fetch in airports:
        print(f"The airport with ICAO code {fetch} is {airports[fetch]}.")
    else:
        print(f'No airport found with ICAO code {fetch}.')
while 0 == 0:
    act = input('\nAirport Data Management\n1. Enter a new airport\n2. Fetch airport information\n3. Quit\nPlease choose an option (1-3): ')
    if int(act) == 1:
        adda()
    elif int(act) == 2:
        fetcha()
    elif int(act) == 3:
        print('Thank you for using the Airport Data Management system. Goodbye!')
        quit()