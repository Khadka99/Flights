import mysql.connector
from mysql.connector import Error

class DB:
    def __init__(self):
        #connect to the database
        from mysql.connector import Error

        try:
            self.conn = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='adhya',
                database='indigo'
                # auth_plugin='mysql_native_password'  # Change to 'caching_sha2_password' if needed
            )
            self.mycursor = self.conn.cursor()
            print("Connection Established")
        except Error as e:
            print(f"Connection Error: {e}")

    def fetch_city_names(self):

        city = []
        self.mycursor.execute("""
        SELECT DISTINCT(Source) FROM revision.flights
        UNION
        SELECT DISTINCT(Destination) FROM revision.flights
        """)
        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])

        return(city)

    def fetch_all_flights(self,Source,Destination):
        self.mycursor.execute("""
        SELECT Airline, Route, Dep_Time, Duration, Price FROM revision.flights
            WHERE Source = '{}' AND Destination = '{}'
        """.format(Source,Destination))
        data = self.mycursor.fetchall()
        return data

    def fetch_airline_frequency(self):
        airline = []
        frequency = []
        self.mycursor.execute("""
        SELECT Airline, COUNT(*) FROM revision.flights
        GROUP BY Airline
        """)
        data = self.mycursor.fetchall()

        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline,frequency

    def busy_airport(self):
        city = []
        frequency = []
        self.mycursor.execute("""
            SELECT Source,COUNT(*) FROM (SELECT Source FROM revision.flights
            UNION ALL
            SELECT Destination FROM revision.flights) t
            GROUP BY t.Source
            ORDER BY COUNT(*) DESC
        """)
        data = self.mycursor.fetchall()

        for items in data:
            city.append(items[0])
            frequency.append(items[1])

        return city, frequency

    def daily_frequency(self):
        date = []
        frequency = []
        self.mycursor.execute(("""
        SELECT Date_of_Journey,COUNT(*) FROM revision.flights
            GROUP BY Date_of_Journey;
        """))
        data = self.mycursor.fetchall()

        for items in data:
            date.append(items[0])
            frequency.append(items[1])

        return date,frequency

    def dep_time_and_price(self):
        time = []
        frequency = []
        price = []
        self.mycursor.execute("""
        SELECT dep_time,COUNT(*),Price FROM Revision.flights
            GROUP BY dep_time,Price
            ORDER BY COUNT(*) DESC
            LIMIT 20
        """)
        data = self.mycursor.fetchall()

        for items in data:
            time.append(items[0])
            frequency.append(items[1])
            price.append(items[2])

        return time,frequency,price



