import os
import mysql.connector
from prettytable import PrettyTable
from dotenv import load_dotenv

# load environment variables from the .env file
load_dotenv()
database=os.getenv("NAME_BD_MYSQL")
try:
    # create a connection to the MySQL database
    mydb = mysql.connector.connect(
        host=os.getenv("HOST_MYSQL"),
        user=os.getenv("USER_MYSQL"),
        password=os.getenv("PASS_MYSQL"),
        database=os.getenv("NAME_BD_MYSQL")
    )
    print("Connexion à la base de données réussie. \U00002705")
except mysql.connector.Error as e:
    if e.errno == 1049:
        print(f"La connexion à la base de données a réussi \U00002705, mais la base de données \033[1m{database}\033["
              f"0m n'existe pas. \U0000274C\n1. Lancer le scripte \033[1mmysql_dump_import.py\033[0m pour importer la "
              f"base de données.")
        exit(1)
    elif e.errno == 2003:
        print(f"\U0000274C Erreur lors de la connexion à la base de données : {e}\n1. Vérifier que vous avez démarer "
              f"votre base "
              f"de données.\n2. Vérifier que les informations de connexion sont juste dans le fichier \033[1m.env\033["
              f"0m")
        exit(1)
    else:
        print(f"Erreur : {e} \U0000274C")
        exit(1)

try:
    # create a cursor object to execute SQL queries
    mycursor = mydb.cursor()

    # execute a SELECT query
    table_name = "t_materiel"
    mycursor.execute(f"SELECT * FROM {table_name}")

    # retrieve all rows from the result set
    rows = mycursor.fetchall()

    # create a pretty table object
    table = PrettyTable()
    table.field_names = [i[0] for i in mycursor.description]

    # add rows to the table
    for row in rows:
        table.add_row(row)

    # afficher le tableau dans le terminal
    print(table)

    # display a success message
    print(f"Affichage réussi de la table {table_name}. \U00002705")
except mysql.connector.Error as e:
    if e.errno == 1146:
        print(f"La connexion à la base de données a réussi \U00002705, mais la table \033[1m{table_name}\033[0m "
              f"n'existe pas. \U0000274C\n1. Lancer le scripte \033[1mmysql_dump_import.py\033[0m pour importer la "
              f"base de données.")
        print(f"Erreur : La table n'existe pas. ({e}) \U0000274C")
    else:
        print(f"Erreur : {e} \U0000274C")
finally:
    # close the cursor and the connection to the database
    mycursor.close()
    mydb.close()