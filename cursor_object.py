'''
To execute SQL queries in Python, you need to use a
cursor object from a database API module, such as
sqlite3, psycopg2 for PostgreSQL, or pymysql
 for MySQL. Here is an example of how to use a 
 cursor object to execute an SQL query in Python 
using sqlite3:
'''

import sqlite3

# connect to the database
conn = sqlite3.connect("mydatabase.db")

# create a cursor object
cursor = conn.cursor()

# execute an SQL query
cursor.execute("SELECT * FROM mytable")

# fetch the results
results = cursor.fetchall()

# print the results
for row in results:
    print(row)

# close the cursor and database connection
cursor.close()
conn.close()


'''
In this example, we first connect to a SQLite database 
using sqlite3.connect() and create a cursor object using
 conn.cursor(). We then execute an SQL query using 
 cursor.execute() and fetch the results using 
 cursor.fetchall(). Finally, we print the results 
 and close the cursor and database connection using 
 cursor.close() and conn.close(), respectively.

Note that the exact syntax for executing SQL queries 
may vary depending on the database API module you are
 using. Be sure to consult the documentation for the 
 specific module you are using for more information.
'''