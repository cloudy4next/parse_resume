import mysql.connector
from mysql.connector import Error

class DBConnection:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',                    
                database='resume_test',
                user='root',
                password='password'
                )
            # print(self.connection)
            
            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = self.connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)

        except Error as e:
            print("Error while connecting to MySQL", e)

# finally:
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")

if __name__ == "__main__":
    db = DBConnection()
    print(db.connection)