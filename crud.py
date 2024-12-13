import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='adhya',
        database = 'indigo'
        #auth_plugin='mysql_native_password'  # Change to 'caching_sha2_password' if needed
    )
    mycursor =  conn.cursor()
    print("Connection Established")
except Error as e:
    print(f"Connection Error: {e}")

# create a database on the db server.
#mycursor.execute("CREATE DATABASE indigo")
#conn.commit()
#mycursor.execute("""
   # CREATE TABLE airport(
    #    airport_id INTEGER PRIMARY KEY,
     #   code VARCHAR(20) NOT NULL,
      #  CITY VARCHAR(50) NOT NULL,
       # name VARCHAR(255) NOT NULL
#    )
#""")
#conn.commit()

# insert data to the table

#mycursor.execute("""
#INSERT INTO airport
#VALUES
#(1,'DEL','New Delhi','IGIA'),
#(2,'CCU','Kolkata','NSCA'),
#(3,'BOM','Mumbai','CSMA')
#""")
#conn.commit()

# search/retrive
#mycursor.execute("SELECT * FROM airport")
#data = mycursor.fetchall()
#print(data)

#for i in data:
 #   print(i[3])

 # update
# mycursor.execute("""
#      UPDATE airport
#      SET name = 'Bombay'
#      WHERE airport_id = 3
#  """)
# conn.commit()

mycursor.execute("SELECT * FROM airport")
data = mycursor.fetchall()
print(data)

# DELETE
mycursor.execute("DELETE FROM airport WHERE airport_id = 3")
conn.commit()

mycursor.execute("SELECT * FROM airport")
data = mycursor.fetchall()
print(data)