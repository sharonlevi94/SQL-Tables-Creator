import psycopg2
import os

sql = ''''''
directoryURL = 'C:\Program Files\PostgreSQL\Data\mydata'
for fileName in os.listdir(directoryURL):
    tableName = fileName.split(".")[0]

    sql += "copy " + tableName + "\n"\
           "from " \
           "'{}\{}'".format(directoryURL, fileName) + "\n" \
           "delimiter ','" + "\n"\
           "csv header;\n" + "\n"
print(sql)

# establishing the connection
conn = psycopg2.connect(
    database="mydb", user='postgres', password='123456', host='127.0.0.1', port='5432'
)
conn.autocommit = True

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing query to create a database


# Creating a database
cursor.execute(sql)
print("Database created successfully........")

# Closing the connection
conn.close()
