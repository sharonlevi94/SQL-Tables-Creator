import psycopg2
import os

print("First, make sure you have the tables in your PostgreSQL data base with the names of the csv file")

# Get an inputs from the user
directory = str(input("Please enter a directory path:\n"))
userName = str(input("Please enter your DB user name:\n"))
password = str(input("Please enter your DB password:\n"))
db = str(input("Please enter DB name:\n"))
host = str(input("Please enter an host:\n"))
port = str(input("Please enter a port:\n"))

# establishing the connection
conn = psycopg2.connect(
     database="mydb", user='postgres', password='123456', host='127.0.0.1', port='5432'
)
# conn = psycopg2.connect(
#    database=db, user=userName, password=password, host=host, port=port
# )
conn.autocommit = True

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing query to create a database
sql = ''''''

for fileName in os.listdir(directory):
    tableName = fileName.split(".")[0]

    sql += "copy " + tableName + "\n"\
           "from " \
           "'{}\{}'".format(directory, fileName) + "\n" \
           "delimiter ','" + "\n"\
           "csv header;\n" + "\n"
print(sql)

# Creating a database | Execute the query
cursor.execute(sql)
print("Database created successfully........")

# Closing the connection
conn.close()
