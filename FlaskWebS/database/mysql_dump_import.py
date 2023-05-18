import mysql.connector
from prettytable import PrettyTable

# Database connection details
host = 'localhost'
user = 'root'
password = ''
database = 'besson_ethan_info_1a'

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
