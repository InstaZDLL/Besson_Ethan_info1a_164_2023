import mysql.connector
from prettytable import PrettyTable

# Database connection details
host = 'localhost'
user = 'root'
password = ''
database = 'besson_ethan_info_1a'


# SQL dump file path
dump_file = 'besson_ethan_info_1a.sql'

# Connect to the database
conn = mysql.connector.connect(host=host, user=user, password=password)
cursor = conn.cursor()

# Read the SQL dump file
with open(dump_file, 'r') as file:
    sql_statements = file.read()

# Split SQL statements by semicolon and execute them one by one
statements = sql_statements.split(';')
for statement in statements:
    # Ignore empty statements
    if not statement.strip():
        continue

    try:
        # Execute the statement
        cursor.execute(statement)
        conn.commit()
    except mysql.connector.Error as e:
        print(f'Error executing statement: {statement}')
        print(f'Error message: {str(e)}')

# Connect to the database
conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
cursor = conn.cursor()

# Execute a SELECT query
cursor.execute("SELECT * FROM t_categorie")

# Retrieve all rows from the result set
rows = cursor.fetchall()

# Create a pretty table object
table = PrettyTable()
table.field_names = [i[0] for i in cursor.description]

# Add rows to the table
for row in rows:
    table.add_row(row)

# Print the table
print(table)

# Close the database connection
cursor.close()
conn.close()
print("Finished")

# import mysql.connector
#
# # Connect to the MySQL server
# cnx = mysql.connector.connect(
#     host='localhost',
#     user='your_username',
#     password='your_password'
# )
#
# # Create a cursor object to interact with the database
# cursor = cnx.cursor()
#
# # Create the database
# database_name = 'besson_ethan_info_1a'
# create_database_query = f"CREATE DATABASE {database_name}"
# cursor.execute(create_database_query)
#
# # Switch to the newly created database
# use_database_query = f"USE {database_name}"
# cursor.execute(use_database_query)
#
# # Read the SQL dump file
# sql_dump_file = 'path_to_your_sql_dump_file.sql'
# with open(sql_dump_file, 'r') as file:
#     sql_script = file.read()
#
# # Execute the SQL script to import the dump
# cursor.execute(sql_script)
#
# # Commit the changes and close the connection
# cnx.commit()
# cnx.close()
