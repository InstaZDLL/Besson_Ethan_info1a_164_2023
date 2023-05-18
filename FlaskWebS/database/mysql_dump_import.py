from dotenv import load_dotenv
import os
import mysql.connector
from prettytable import PrettyTable

load_dotenv()

# Database connection details
host_mysql = os.environ.get('HOST_MYSQL')
user_mysql = os.environ.get('USER_MYSQL')
pass_mysql = os.environ.get('PASS_MYSQL')
port_mysql = os.environ.get('PORT_MYSQL')
name_bd_mysql = os.environ.get('NAME_BD_MYSQL')
name_file_dump_sql_bd = os.environ.get('NAME_FILE_DUMP_SQL_BD')


def run():

    # SQL dump file path
    dump_file = 'besson_ethan_info_1a.sql'

    # Connect to the database
    conn = mysql.connector.connect(host=host_mysql, user=user_mysql, password=pass_mysql, port=port_mysql)
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
    conn = mysql.connector.connect(host=host_mysql, user=user_mysql, password=pass_mysql, port=port_mysql, database=name_bd_mysql)
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


if __name__ == '__main__':
    run()
