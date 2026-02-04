from geopy import distance
import mysql.connector
def c():
    connection = mysql.connector.connect(
        host = "127.0.0.1",
        port = 3306,
        database = "flight_game",
        user = "user1",
        password = "proMethean26",
        autocommit = False
    )
    return connection
def get_airport_coordinates(icao_code):
    connection = c()
    cur = connection.cursor()
    cur.execute(f'select latitude_deg, longitude_deg from airport where ident = "{icao_code}"')
    return cur.fetchone()
def run_airport_distance():
    icao1 = input('Enter the ICAO-code of the first airport: ').upper()
    loc1 = get_airport_coordinates(icao1)
    icao2 = input('Enter the ICAO-code of the second airport: ').upper()
    loc2 = get_airport_coordinates(icao2)
    dis = distance.distance(loc1, loc2).km
    print(f'Distance between {icao1} and {icao2}: {dis:.2f} kilometers')
run_airport_distance()
