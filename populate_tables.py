# This script writes data from input.csv to a sqlite tables

# Import required modules
import csv, sqlite3

# Creating connection to the database
conn = sqlite3.connect("census.db") 

# Enabling foreign keys
conn.execute('PRAGMA foreign_keys = ON')

# Creating a cursor object to execute SQL queries on a database table
cursor = conn.cursor()

# Opening and reading the contents of the input.csv file
# relevant to personal details like age and gender
with open('input.csv','r') as file:

    r = csv.DictReader(file)
    dt = [(i['id'], i['fnlwgt'], i['age'], i['gender'], i['race'], i['marital_status'], i['relationship'], i['country'], i['education_level']) for i in r]
    
# SQL query to insert data into the demographic table
cursor.executemany("INSERT INTO Demographic (id, fnlwgt, age, gender, race, marital_status, relationship, native_country, education_level) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", dt)

# Opening and reading the contents of the input.csv file
# relevant to income details
with open('input.csv','r') as file:

    r = csv.DictReader(file)
    it = [(i['id'], i['occupation'], i['workclass'], i['weekly_hours'], i['net_capital'], i['income']) for i in r]

# SQL query to insert data into the income table
cursor.executemany("INSERT INTO Income (d_id, occupation, workclass, hours_per_week, capital, total_income) VALUES (?, ?, ?, ?, ?, ?);", it)

# SQL query to retrieve all data from the demographic table
select_all_demographic = "SELECT * FROM Demographic"
rows_d = cursor.execute(select_all_demographic).fetchall()

# Printing SELECT query result
for r in rows_d:
	print(r)

# SQL query to retrieve all data from the income table
select_all_income = "SELECT * FROM Income"
rows_i = cursor.execute(select_all_income).fetchall()

# Printing SELECT query result
for r in rows_i:
	print(r)

# Committing the changes
conn.commit()

# Closing the database connection
conn.close()
