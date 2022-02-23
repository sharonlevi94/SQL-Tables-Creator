import psycopg2
import os


directory = str(input("Please enter a directory path:\n"))
sql = ''''''

for fileName in os.listdir(directory):
    tableName = fileName.split(".")[0]

    sql += "copy " + tableName + "\n"\
           "from " \
           "'{}\{}'".format(directory, fileName) + "\n" \
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
