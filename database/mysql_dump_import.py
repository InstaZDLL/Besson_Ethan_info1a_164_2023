import sys

import mysql.connector
import os
import re
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
HOST_MYSQL = os.getenv("HOST_MYSQL")
USER_MYSQL = os.getenv("USER_MYSQL")
PASS_MYSQL = os.getenv("PASS_MYSQL")
PORT_MYSQL = os.getenv("PORT_MYSQL")
NAME_BD_MYSQL = os.getenv("NAME_BD_MYSQL")
NAME_FILE_DUMP_SQL_BD = os.getenv("NAME_FILE_DUMP_SQL_BD")

# Read the SQL dump file
with open(NAME_FILE_DUMP_SQL_BD, "r") as f:
    sql_dump = f.read()

# Extract the name of the database from the CREATE DATABASE statement
database_name = re.search(r"CREATE DATABASE IF NOT EXISTS `(.+?)`", sql_dump).group(1)

# Connect to MySQL without specifying a database
try:
    connection = mysql.connector.connect(
        host=HOST_MYSQL,
        user=USER_MYSQL,
        password=PASS_MYSQL,
        port=PORT_MYSQL,
    )
    print("Connexion à MySQL réussie.\U00002705")
except mysql.connector.Error as e:
    if e.errno == 2003:
        print(f"\U0000274C Erreur lors de la connexion à la base de données : {e}\n1. Vérifier que vous avez démarer "
              f"votre base "
              f"de données.\n2. Vérifier que les informations de connexion sont juste dans le fichier \033[1m.env\033["
              f"0m")
        exit(1)
    else:
        print(f"Erreur : {e} \U0000274C")
        exit(1)

# Create a cursor object
cursor = connection.cursor()

# Import the SQL dump file
try:
    # Split the SQL dump into individual queries
    queries = sql_dump.split(";")

    cursor = connection.cursor(buffered=True)

    for query in queries:
        # Check if the request is not empty
        if query.strip():
            # Execute the request
            cursor.execute(query)

            # Check if the request returns data
            if cursor.description:
                # Retrieve all rows from the result set
                rows = cursor.fetchall()

                # Process the result set
                for row in rows:
                    # Do something with the line
                    pass

                # Release the memory associated with the result set
                cursor.free_result()

    connection.commit()
    print("Importation du fichier de dump SQL réussie. \U00002705")
except FileNotFoundError:
    print("Erreur : fichier de dump SQL introuvable. \U0000274C")
except Exception as e:
    print(f"Erreur : {e} \U0000274C")
finally:
    cursor.close()
    connection.close()

sys.exit(0)