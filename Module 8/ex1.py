import mysql.connector
def c():
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='user1',
        password='proMethean26',
        autocommit=False,
        )
    return connection
connection = c()
icao = input('Enter the ICAO code of an airport: ').upper()
sql = f'select name, municipality from airport where ident = "{icao}"'
cursor = connection.cursor()
cursor.execute(sql)
result = [cursor.fetchone()]
if cursor.rowcount > 0:
    for row in result:
        print(f'Airport name: {row[0]}\nLocation: {row[1]}')
else:
    print("No airport was found")