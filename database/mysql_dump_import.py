import sys

import mysql.connector
import os
import re
from dotenv import load_dotenv

load_dotenv()

# Charger les variables d'environnement
HOST_MYSQL = os.getenv("HOST_MYSQL")
USER_MYSQL = os.getenv("USER_MYSQL")
PASS_MYSQL = os.getenv("PASS_MYSQL")
PORT_MYSQL = os.getenv("PORT_MYSQL")
NAME_BD_MYSQL = os.getenv("NAME_BD_MYSQL")
NAME_FILE_DUMP_SQL_BD = os.getenv("NAME_FILE_DUMP_SQL_BD")

# Lire le fichier de dump SQL
with open(NAME_FILE_DUMP_SQL_BD, "r") as f:
    sql_dump = f.read()

# Extraire le nom de la base de données de l'instruction CREATE DATABASE
database_name = re.search(r"CREATE DATABASE IF NOT EXISTS `(.+?)`", sql_dump).group(1)

# Se connecter à MySQL sans spécifier de base de données
try:
    connection = mysql.connector.connect(
        host=HOST_MYSQL,
        user=USER_MYSQL,
        password=PASS_MYSQL,
        port=PORT_MYSQL,
    )
    print("Connexion à MySQL réussie.")
except mysql.connector.Error as e:
    print(f"Erreur lors de la connexion à MySQL : {e}")
    exit(1)

# Créer un objet curseur
cursor = connection.cursor()

# Importer le fichier de dump SQL
try:
    # Diviser le dump SQL en requêtes individuelles
    queries = sql_dump.split(";")

    cursor = connection.cursor(buffered=True)

    for query in queries:
        # Vérifier si la requête n'est pas vide
        if query.strip():
            # Exécuter la requête
            cursor.execute(query)

            # Vérifier si la requête renvoie des données
            if cursor.description:
                # Récupérer toutes les lignes du jeu de résultats
                rows = cursor.fetchall()

                # Traiter le jeu de résultats
                for row in rows:
                    # Faire quelque chose avec la ligne
                    pass

                # Libérer la mémoire associée au jeu de résultats
                cursor.free_result()

    connection.commit()
    print("Importation du fichier de dump SQL réussie.")
except FileNotFoundError:
    print("Erreur : fichier de dump SQL introuvable.")
except Exception as e:
    print(f"Erreur : {e}")
finally:
    cursor.close()
    connection.close()

sys.exit(0)