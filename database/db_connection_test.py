import os
import mysql.connector
from prettytable import PrettyTable
from dotenv import load_dotenv

# charger les variables d'environnement à partir du fichier .env
load_dotenv()

try:
    # créer une connexion à la base de données MySQL
    mydb = mysql.connector.connect(
        host=os.getenv("HOST_MYSQL"),
        user=os.getenv("USER_MYSQL"),
        password=os.getenv("PASS_MYSQL"),
        database=os.getenv("NAME_BD_MYSQL")
    )
    print("Connexion à la base de données réussie.")
except mysql.connector.Error as e:
    print(f"Erreur lors de la connexion à la base de données : {e}\nImporter la base de données avec le fichier mysql_dump_import")
    exit(1)

try:
    # créer un objet curseur pour exécuter des requêtes SQL
    mycursor = mydb.cursor()

    # exécuter une requête SELECT
    table_name = "t_materiel"
    mycursor.execute(f"SELECT * FROM {table_name}")

    # récupérer toutes les lignes de l'ensemble des résultats
    rows = mycursor.fetchall()

    # créer un joli objet table
    table = PrettyTable()
    table.field_names = [i[0] for i in mycursor.description]

    # ajouter des lignes au tableau
    for row in rows:
        table.add_row(row)

    # afficher le tableau dans le terminal
    print(table)

    # afficher un message de succès
    print(f"Affichage réussi de la table {table_name}.")
except mysql.connector.Error as e:
    if e.errno == 1146:
        print(f"Erreur : La table n'existe pas. ({e})")
    else:
        print(f"Erreur : {e}")
finally:
    # fermer le curseur et la connexion à la base de données
    mycursor.close()
    mydb.close()