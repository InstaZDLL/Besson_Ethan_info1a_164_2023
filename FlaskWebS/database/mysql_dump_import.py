import mysql.connector
from prettytable import PrettyTable
import re
host_mysql = "localhost"
user_mysql = "root"
pass_mysql = ""
port_mysql = 3306


def before():
    connection = mysql.connector.connect(
        host=host_mysql,
        user=user_mysql,
        password=pass_mysql,
        port=port_mysql,
    )

    # Create a cursor object
    cursor = connection.cursor()

    # Create the database
    cursor.execute("CREATE DATABASE IF NOT EXISTS besson_ethan_info_1a")


# def run():
#     # Read the SQL dump file
#     with open("besson_ethan_info_1a.sql", "r") as f:
#         sql_dump = f.read()
#
#     # Extract the name of the database from the CREATE DATABASE statement
#     database_name = re.search(r"CREATE DATABASE IF NOT EXISTS `(.+?)`", sql_dump).group(1)
#
#     # Connect to MySQL without specifying a database
#     try:
#         connection = mysql.connector.connect(
#             host=host_mysql,
#             user=user_mysql,
#             password=pass_mysql,
#             port=port_mysql,
#         )
#         print("Connexion à MySQL réussie.\U00002705")
#     except mysql.connector.Error as e:
#         if e.errno == 2003:
#             print(f"\U0000274C Erreur lors de la connexion à la base de données : {e}\n1. Vérifier que vous avez démarré "
#                   f"votre base "
#                   f"de données.\n2. Vérifier que les informations de connexion sont correctes dans le fichier \033[1m.env\033["
#                   f"0m")
#             exit(1)
#         else:
#             print(f"Erreur : {e} \U0000274C")
#             exit(1)
#
#     # Create a cursor object
#     cursor = connection.cursor()
#
#     # Import the SQL dump file
#     try:
#         # Split the SQL dump into individual queries
#         queries = sql_dump.split(";")
#
#         cursor = connection.cursor(buffered=True)
#
#         for query in queries:
#             # Check if the request is not empty
#             if query.strip():
#                 # Execute the request
#                 cursor.execute(query)
#
#                 # Check if the request returns data
#                 if cursor.description:
#                     # Retrieve all rows from the result set
#                     rows = cursor.fetchall()
#
#                     # Process the result set
#                     for row in rows:
#                         # Do something with the line
#                         pass
#
#                     # Release the memory associated with the result set
#                     cursor.free_result()
#
#         connection.commit()
#         print("Importation du fichier de dump SQL réussie. \U00002705")
#     except FileNotFoundError:
#         print("Erreur : fichier de dump SQL introuvable. \U0000274C")
#     except Exception as e:
#         print(f"Erreur : {e} \U0000274C")
#     finally:
#         cursor.close()
#         connection.close()
#
#     try:
#         # create a connection to the MySQL database
#         mydb = mysql.connector.connect(
#             host=host_mysql,
#             user=user_mysql,
#             password=pass_mysql,
#             port=port_mysql,
#             database=name_bd_mysql
#         )
#         print("Connexion à la base de données réussie. \U00002705")
#     except mysql.connector.Error as e:
#         if e.errno == 1049:
#             print(f"La connexion à la base de données a réussi \U00002705, mais la base de données \033[1m{name_bd_mysql}\033["
#                   f"m n'existe pas. \U0000274C\n1. Lancer le script \033[1mmysql_dump_import.py\033[0m pour importer la base de données.")
#             exit(1)
#         elif e.errno == 2003:
#             print(f"\U0000274C Erreur lors de la connexion à la base de données : {e}\n1. Vérifier que vous avez démarré "
#                   f"votre base "
#                   f"de données.\n2. Vérifier que les informations de connexion sont correctes dans le fichier \033[1m.env\033["
#                   f"0m")
#             exit(1)
#         else:
#             print(f"Erreur : {e} \U0000274C")
#             exit(1)
#
#     try:
#         # create a cursor object to execute SQL queries
#         mycursor = mydb.cursor()
#
#         # execute a SELECT query
#         table_name = "t_categorie"
#         mycursor.execute(f"SELECT * FROM {table_name}")
#
#         # retrieve all rows from the result set
#         rows = mycursor.fetchall()
#
#         # create a pretty table object
#         table = PrettyTable()
#         table.field_names = [i[0] for i in mycursor.description]
#
#         # add rows to the table
#         for row in rows:
#             table.add_row(row)
#
#         # afficher le tableau dans le terminal
#         print(table)
#
#         # display a success message
#         print(f"Affichage réussi de la table {table_name}. \U00002705")
#     except mysql.connector.Error as e:
#         if e.errno == 1146:
#             print(f"La connexion à la base de données a réussi \U00002705, mais la table \033[1m{table_name}\033[0m "
#                   f"n'existe pas. \U0000274C\n1. Lancer le script \033[1mmysql_dump_import.py\033[0m pour importer la "
#                   f"base de données.")
#             print(f"Erreur : La table n'existe pas. ({e}) \U0000274C")
#         else:
#             print(f"Erreur : {e} \U0000274C")
#     finally:
#         # close the cursor and the connection to the database
#         mycursor.close
#         mydb.close()


if __name__ == "__main__":
    before()
    # run()