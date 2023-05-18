import mysql.connector
from FlaskWebS import name_bd_mysql as db_name
from FlaskWebS import name_file_dump_sql_bd as sql_file_path
from FlaskWebS import user_mysql, pass_mysql, host_mysql


def run():
    # Create a connection to the MySQL server
    cnx = mysql.connector.connect(
        user=user_mysql,
        password=pass_mysql,
        host=host_mysql
    )

    # Create a cursor object to execute SQL statements
    cursor = cnx.cursor()

    # Create a new database using a prepared statement with a parameterized query
    create_database_query = 'CREATE DATABASE %s'
    cursor.execute(create_database_query, (db_name,))

    # Connect to the new database
    cursor.execute(f'USE {db_name}')

    # Open and read the SQL file
    with open(sql_file_path, 'r') as sql_file:
        sql_script = sql_file.read()

    # Split the SQL script into separate statements
    statements = sql_script.split(';')

    # Execute each statement in the script
    for statement in statements:
        if statement.strip() != '':
            cursor.execute(statement)

    # Commit the changes and close the cursor and connection
    cnx.commit()
    cursor.close()
    cnx.close()


if __name__ == "__main__":
    run()
