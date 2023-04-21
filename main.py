from dotenv import load_dotenv
from flask import Flask, render_template, request, flash, redirect, url_for
import os
import mysql.connector

app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')
load_dotenv()

# Accéder aux variables du fichier .env en utilisant os.environ
host_mysql = os.environ.get('HOST_MYSQL')
user_mysql = os.environ.get('USER_MYSQL')
pass_mysql = os.environ.get('PASS_MYSQL')
port_mysql = int(os.environ.get('PORT_MYSQL'))
name_bd_mysql = os.environ.get('NAME_BD_MYSQL')
name_file_dump_sql_bd = os.environ.get('NAME_FILE_DUMP_SQL_BD')

adresse_srv_flask = os.environ.get('ADRESSE_SRV_FLASK')
debug_flask = os.environ.get('DEBUG_FLASK') == 'true'
port_flask = int(os.environ.get('PORT_FLASK'))
app.secret_key = os.environ.get('SECRET_KEY_FLASK')

# Connexion à la base de données MySQL
try:
    cnx = mysql.connector.connect(user=user_mysql, password=pass_mysql, host=host_mysql, port=port_mysql,
                                  database=name_bd_mysql)
except mysql.connector.Error as e:
    print(f"Erreur lors de la connexion à MySQL : {e}")
    exit(1)
cursor = cnx.cursor()


@app.route('/')
def index():
    """
    Affiche la page d'accueil de l'application Flask.
    """
    return render_template('index.html')


@app.errorhandler(404)
def not_found_error(error):
    """
    Gère l'erreur 404 (page non trouvée) et affiche une page d'erreur personnalisée.
    """
    return render_template('404.html'), 404


@app.route('/materiel')
def materiel():
    """
    Récupère les données de la table t_materiel dans la base de données MySQL et les affiche sur la page "materiel.html".
    """
    query = "SELECT * FROM t_materiel"
    cursor.execute(query)
    data = cursor.fetchall()

    return render_template('materiel.html', data=data)


@app.route('/personnes')
def personnes():
    """
    Récupère les données de la table t_personnes_avoir_materiel (en les joignant avec les tables t_personnes et t_materiel)
    dans la base de données MySQL et les affiche sur la page "personnes.html".
    """
    query = """
        SELECT t_personnes_avoir_materiel.id_personnes_avoir_materiel, t_personnes.prenom_pers, t_personnes.nom_pers, t_materiel.nom_mat
        FROM t_personnes
        INNER JOIN t_personnes_avoir_materiel ON t_personnes.id_personnes = t_personnes_avoir_materiel.fk_personnes
        INNER JOIN t_materiel ON t_personnes_avoir_materiel.fk_materiel = t_materiel.id_materiel
        WHERE t_personnes.id_personnes;
    """
    cursor.execute(query)
    data = cursor.fetchall()

    headers = [column[0] for column in cursor.description]

    return render_template('personnes.html', data=data, headers=headers)


@app.route('/delete_row')
def delete_row():
    # Get the row id from the request parameters
    row_id = request.args.get('id')

    # Execute the SQL query to delete the row with the given id
    cursor.execute(f"DELETE FROM t_personnes_avoir_materiel WHERE id_personnes_avoir_materiel={row_id}")

    # Commit the changes to the database
    cnx.commit()

    # Return a JSON response indicating success
    return {"status": "success"}


@app.route('/delete_row_marque', methods=['POST'])
def delete_row_marque():
    id = request.form['id']
    cursor = cnx.cursor()
    # delete any referencing rows in the t_marque_avoir_materiel table
    cursor.execute('DELETE FROM t_marque_avoir_materiel WHERE fk_marque=%s', (id,))
    # delete the row in the t_marque table
    cursor.execute('DELETE FROM t_marque WHERE id_marque=%s', (id,))
    cnx.commit()
    cursor.close()
    return 'Row deleted'


@app.route('/add_marque_form')
def add_marque_form():
    """
    Affiche le formulaire d'ajout de marque.
    """
    return render_template('/actions/add_marque_form.html')


@app.route('/add_marque', methods=['GET', 'POST'])
def add_marque():
    """
    Traite les données du formulaire d'ajout de marque.
    """
    if request.method == 'POST':
        nom_marque = request.form['nom_marque']
        description_marque = request.form['description_marque']

        query = """
            INSERT INTO t_marque (nom_marque, description_marque)
            VALUES (%s, %s)
        """
        values = (nom_marque, description_marque)

        try:
            cursor.execute(query, values)
            cnx.commit()
            flash('La marque a été ajoutée avec succès.', 'success')
        except Exception as e:
            cnx.rollback()
            flash('Une erreur est survenue lors de l\'ajout de la marque. Veuillez réessayer plus tard.', 'danger')
            print(e)

        return redirect(url_for('marques'))

    else:
        return render_template('/actions/add_marque_form.html')


@app.route('/marques')
def marques():
    """
    Récupère les données de la table t_marque dans la base de données MySQL et les affiche sur la page "marques.html".
    """
    query = """
        SELECT t_marque.id_marque, t_marque.nom_marque, description_marque
        FROM t_marque
        WHERE t_marque.id_marque;
    """
    cursor.execute(query)
    data = cursor.fetchall()

    headers = [column[0] for column in cursor.description]

    return render_template('marques.html', data=data, headers=headers)


@app.route('/about')
def about():
    """
    Affiche la page "about.html".
    """
    return render_template('about.html')


if __name__ == '__main__':
    # context = ('ssl/cert.crt', 'ssl/cert.key')
    # ssl_context=context
    app.run(host=adresse_srv_flask, port=port_flask, debug=debug_flask)
