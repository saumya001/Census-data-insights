# This script creates database called census and two tables:
# demographic and income

# Import required modules
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('census.db')

# Creating a cursor object to execute SQL queries on a database table
cursor = conn.cursor()

# Definition of table conatining income and occupation related data
create_table_income = '''CREATE TABLE IF NOT EXISTS Income
                        (id INTEGER PRIMARY KEY NOT NULL,
                        d_id INTEGER NOT NULL,
                        occupation TEXT,
                        workclass TEXT,
                        hours_per_week INTEGER,
                        capital INTEGER,
                        total_income TEXT,
                        FOREIGN KEY (d_id)
                            REFERENCES Demographic (id)
                        );
                    '''

# Definition of table containing education and demographic data
create_table_demographic = '''CREATE TABLE IF NOT EXISTS Demographic
                            (id INTEGER PRIMARY KEY NOT NULL,
                            fnlwgt INTEGER,
                            age INTEGER,
                            gender TEXT,
                            race TEXT,
                            marital_status TEXT,
                            relationship TEXT,
                            native_country TEXT,
                            education_level INTEGER
                            );
                        '''

# Creating the income table into the database
cursor.execute(create_table_income)

# Creating the demographic table into the database
cursor.execute(create_table_demographic)

# Committing the changes
conn.commit()

# Closing the database connection
conn.close()