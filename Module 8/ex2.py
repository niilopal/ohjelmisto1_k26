import mysql.connector
def c():
    connection = mysql.connector.connect(
        host = "127.0.0.1",
        port = 3306,
        database = "flight_game",
        user = "user1",
        password = "proMethean26",
        autocommit = False,
        )
    return connection
def get_airport_by_country(country_code):
    connection = c()
    cursor = connection.cursor()
    cursor.execute(f'select type, count(*) from airport where iso_country = "{country_code}" group by type')
    return cursor.fetchall()
def run_country_program():
    ident = input('Enter the country code (e.g., FI for Finland): ').upper()
    result = get_airport_by_country(ident)
    print(result)
    print(f'Airports in {ident}: ')
    for i in result:
        print(f'{i[1]} {i[0]} airports')
run_country_program()