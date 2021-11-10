import sys
import os
import mysql.connector
from .db_connects import DBConnection

# from Relation import *

class TODatabase():
    def __init__(self, data_list):
        self.db = DBConnection()
        self.lists = [item for item in data_list.values()]
        # os.system('clear')
        # data = [item for item in data_list.values()]
        # key = [item for item in data_list.keys()]
        # print(len(data), len(key))
        print('\n\nGoing to database in format as below......')
        for index, item in data_list.items():
            print(index)
            print('----------------------')
            print(item)
            print('---------------------------------------------------')
        
    def insert_data(self):
        try:
            connection = self.db.connection
            cursor = connection.cursor()
            # check the queries
            mysql_insert_query = """INSERT INTO table_m (resume_id,  phone, email, career_objective, summary, education, work_experience, skills, research, 
                competitive_programming, projects, organizations, personal_information, courses, achievements, certifications, language, 
                contact, refer, others, image_filename)
            VALUES (%s,  %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s) """
            # record = []
            record = self.lists
            # os.system('clear')
            # print("Records--> ", record)
            # print(len(record))
            
            cursor.execute(mysql_insert_query, record)
            connection.commit()
            print("Record inserted successfully into resume_test table")
            
        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table {}".format(error))
        
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
                

# if __name__ == "__main__":
#     li = Relation.standrad_alike()
#     print(li)

    # query = TODatabase(li)
    # query.insert_data()
    
    