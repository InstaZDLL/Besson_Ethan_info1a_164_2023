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
select_query_enabled = os.environ.get('SELECT_QUERY_ENABLED') == 'true'


def run():

    # SQL dump file path
    dump_file = name_file_dump_sql_bd #'besson_ethan_info_1a.sql'

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
            if e.errno == 2003:
                print(f"\U0000274C Erreur lors de la connexion à la base de données : {str(e)}\n1. Vérifier que vous avez démarer "
                      f"votre base "
                      f"de données.\n2. Vérifier que les informations de connexion sont juste dans le fichier \033[1m.env\033["
                      f"0m")
                exit(1)
            else:
                print(f'Erreur dans l\'exécution de l\'instruction : {statement}')
                print(f'Message d\'erreur: {str(e)}')

    # Connect to the database
    conn = mysql.connector.connect(host=host_mysql, user=user_mysql, password=pass_mysql, port=port_mysql, database=name_bd_mysql)
    cursor = conn.cursor()

    # Execute a SELECT query
    if select_query_enabled:
        cursor.execute("SELECT * FROM t_categorie")
        rows = cursor.fetchall()
        table = PrettyTable()
        table.field_names = [i[0] for i in cursor.description]
        for row in rows:
            table.add_row(row)
        print(table)
    else:
        print('Le test de connexion à la base de données / Affichage de la table est \033[1mdésactivé\033[0m')

    # Close the database connection
    cursor.close()
    conn.close()
    print("Terminé")


if __name__ == '__main__':
    run()
