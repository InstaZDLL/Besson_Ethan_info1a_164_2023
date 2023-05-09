from dotenv import load_dotenv
from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
import os
import mysql.connector
from datetime import datetime
from PyFormModify import ModifyMaterielForm
import requests

app = Flask(__name__, static_url_path='/static')
load_dotenv()

# Accessing variables in the .env file using os.environ
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

# Connection to the MySQL database
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
    Displays the home page of the Flask application.
    """
    return render_template('index.html')


@app.errorhandler(404)
def not_found_error(error):
    """
    Handles the 404 error (page not found) and displays a custom error page.
    """
    return render_template('404.html'), 404


@app.route('/materiel')
def materiel():
    """
    Retrieves the data from the table t_materiel in the MySQL database and displays it on the page "materiel.html".
    """
    query = "SELECT * FROM t_materiel"
    cursor.execute(query)
    data = cursor.fetchall()

    return render_template('materiel.html', data=data)


@app.route('/personnes')
def personnes():
    """
    Retrieves the data from the table t_persons_have_equipment (by joining them with the tables t_persons and t_material)
    in the MySQL database and displays them on the page "personnes.html".
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


# Begin New code block

@app.route("/show_modify_materiel")
def show_modify_materiel():
    # get the id parameter from the query string
    id_materiel = request.args.get("id")

    # retrieve data from the t_materiel table
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM t_materiel WHERE id_materiel=%s", (id_materiel,))
    row = cursor.fetchone()

    # check if a row was found
    if row is None:
        cursor.close()
        return "No row found with the given id"

    # retrieve the category name for the selected row
    cursor.execute("SELECT t_categorie.nom_cat FROM t_categorie_avoir_materiel JOIN t_categorie ON t_categorie_avoir_materiel.fk_categorie = t_categorie.id_categorie WHERE t_categorie_avoir_materiel.fk_materiel=%s", (id_materiel,))
    categorie_row = cursor.fetchone()
    categorie_name = categorie_row[0] if categorie_row else None

    # retrieve a list of all categories
    cursor.execute("SELECT nom_cat FROM t_categorie")
    categories = [row[0] for row in cursor.fetchall()]

    # close the cursor
    cursor.close()

    # assign the date values directly
    date_achat = row[4]
    date_expi = row[5]

    # convert the row data into a dictionary
    data = {
        "id_mat": row[0],
        "nom_mat": row[1],
        "model_mat": row[2],
        "serial_num": row[3],
        "date_achat": date_achat,
        "date_expi": date_expi,
        "prix_mat": row[6],
        "nom_cat": categorie_name
    }

    form = ModifyMaterielForm(data=data)

    # render the modify_materiel.html template and pass the data and categories to it
    return render_template("/actions/modify_materiel.html", data=data, form=form, categories=categories)


@app.route("/modify_materiel", methods=["POST"])
def modify_materiel():
    # get the form data
    id_mat = request.form["id_mat"]
    nom_mat = request.form["nom_mat"]
    model_mat = request.form["model_mat"]
    serial_num = request.form["serial_num"]
    date_achat = request.form["date_achat"]
    date_expi = request.form["date_expi"]
    prix_mat = request.form["prix_mat"]
    nom_cat = request.form["nom_cat"]

    # validate and convert the date values
    try:
        date_achat = datetime.strptime(date_achat, "%Y-%m-%dT%H:%M").strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        date_achat = None
    try:
        date_expi = datetime.strptime(date_expi, "%Y-%m-%dT%H:%M").strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        date_expi = None

    # update the data in the t_materiel table
    cursor.execute("UPDATE t_materiel SET nom_mat=%s, model_mat=%s, serial_num=%s, date_achat=%s, date_expi=%s, prix_mat=%s WHERE id_materiel=%s", (nom_mat, model_mat, serial_num, date_achat, date_expi, prix_mat, id_mat))

    # update the data in the t_categorie_avoir_materiel and t_categorie tables
    cursor.execute("SELECT * FROM t_categorie WHERE nom_cat=%s", (nom_cat,))
    categorie_data = cursor.fetchone()
    if categorie_data:
        cursor.execute("UPDATE t_categorie_avoir_materiel SET fk_categorie=%s WHERE fk_materiel=%s", (categorie_data[0], id_mat))
    else:
        cursor.execute("INSERT INTO t_categorie (nom_cat) VALUES (%s)", (nom_cat,))
        cursor.execute("UPDATE t_categorie_avoir_materiel SET fk_categorie=%s WHERE fk_materiel=%s", (cursor.lastrowid, id_mat))

    # commit the changes
    cnx.commit()

    # redirect to the success page
    return redirect(url_for("categorie"))


# TODO make the succes page and the redirection to the /categorie
@app.route("/success")
def success():
    # render the success.html template
    return render_template("success.html")


@app.route('/delete_row_materiel', methods=['POST'])
def delete_row_materiel():
    """
        This route allows for the deletion of a row in the t_materiel table and any referencing rows in other tables.
        The id of the row to be deleted is obtained from a form submission. The function then uses this id to execute
        a series of DELETE statements on the relevant tables. Finally, the function returns a message indicating that
        the row has been deleted.
    """
    id = request.form['id']
    cursor = cnx.cursor()
    # delete any referencing rows in the t_categorie_avoir_materiel table
    cursor.execute('DELETE FROM t_categorie_avoir_materiel WHERE fk_materiel=%s', (id,))
    # delete any referencing rows in the t_departement_avoir_materiel table
    cursor.execute('DELETE FROM t_departement_avoir_materiel WHERE fk_materiel=%s', (id,))
    # delete any referencing rows in the t_fournisseur_avoir_materiel table
    cursor.execute('DELETE FROM t_fournisseur_avoir_materiel WHERE fk_materiel=%s', (id,))
    # delete any referencing rows in the t_marque_avoir_materiel table
    cursor.execute('DELETE FROM t_marque_avoir_materiel WHERE fk_materiel=%s', (id,))
    # delete any referencing rows in the t_personnes_ajout_materiel table
    cursor.execute('DELETE FROM t_personnes_ajout_materiel WHERE fk_materiel=%s', (id,))
    # delete the row in the t_materiel table
    cursor.execute('DELETE FROM t_materiel WHERE id_materiel=%s', (id,))
    cnx.commit()
    cursor.close()
    return 'Row deleted'


@app.route('/add_materiel', methods=['GET', 'POST'])
def add_materiel():
    """
    Processes the data from the add material form and adds it to the MySQL database.
    """
    # Retrieve categories from the database
    cursor.execute("SELECT nom_cat FROM t_categorie")
    categories = [row for row in cursor.fetchall()]

    if request.method == 'POST':
        id_materiel = request.form['id_materiel']
        nom_mat = request.form['nom_mat']
        model_mat = request.form['model_mat']
        serial_num = request.form['serial_num']
        date_achat = datetime.strptime(request.form['date_achat'], '%Y-%m-%dT%H:%M')
        date_achat_str = date_achat.strftime('%Y-%m-%d %H:%M:%S')
        date_expi = datetime.strptime(request.form['date_expi'], '%Y-%m-%dT%H:%M')
        date_expi_str = date_expi.strftime('%Y-%m-%d %H:%M:%S')
        prix_mat = request.form['prix_mat']
        nom_cat = request.form['nom_cat']

        query = """
            INSERT INTO t_materiel (id_materiel, nom_mat, model_mat, serial_num, date_achat, date_expi, prix_mat)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (id_materiel, nom_mat, model_mat, serial_num, date_achat_str, date_expi_str, prix_mat)

        try:
            cursor.execute(query, values)
            cnx.commit()
            flash('Le matériel a été ajouté avec succès.', 'success')
        except Exception as e:
            cnx.rollback()
            flash('Une erreur est survenue lors de l\'ajout du matériel. Veuillez réessayer plus tard.', 'danger')
            print(e)

        # Add the category of the material
        query = """
            INSERT INTO t_categorie_avoir_materiel (fk_materiel, fk_categorie)
            VALUES (%s, (SELECT id_categorie FROM t_categorie WHERE nom_cat=%s))
        """
        values = (id_materiel, nom_cat)

        try:
            cursor.execute(query, values)
            cnx.commit()
            flash('La catégorie du matériel a été ajoutée avec succès.', 'success')
        except Exception as e:
            cnx.rollback()
            flash('Une erreur est survenue lors de l\'ajout de la catégorie du matériel. Veuillez réessayer plus tard.', 'danger')
            print(e)

        return redirect(url_for('categorie'))

    else:
        return render_template('/actions/add_materiel_form.html', categories=categories)




@app.route('/add_materiel_form')
def add_materiel_form():
    """
    Displays the add person form.
    """
    return render_template('/actions/add_materiel_form.html')


@app.route('/filter', methods=['POST'])
def filter_data():
    hide_dates = request.form.get('hide_dates')
    if hide_dates == "1":
        headers = [h for h in headers if h not in ['date_achat', 'date_expi']]
        data = [[row[i] for i in range(len(row)) if headers[i] not in ['date_achat', 'date_expi']] for row in data]
    else:
        headers = [column[0] for column in cursor.description]
        data = cursor.fetchall()
    return render_template('data_table.html', headers=headers, data=data)

@app.route('/categorie', methods=['GET', 'POST'])
def categorie():
    """
    Retrieves the data from the table t_persons_have_equipment (by joining them with the tables t_persons and t_material)
    in the MySQL database and displays them on the page "personnes.html".
    """
    query = """
        SELECT t_materiel.id_materiel, t_materiel.nom_mat, t_materiel.model_mat, t_materiel.serial_num, t_materiel.date_achat, t_materiel.date_expi, t_materiel.prix_mat, t_categorie.nom_cat
        FROM t_materiel
        LEFT JOIN t_categorie_avoir_materiel ON t_materiel.id_materiel = t_categorie_avoir_materiel.fk_materiel
        LEFT JOIN t_categorie ON t_categorie_avoir_materiel.fk_categorie = t_categorie.id_categorie;
    """
    cursor.execute(query)
    data = cursor.fetchall()

    headers = [column[0] for column in cursor.description]

    if request.method == 'POST':
        hide_dates = request.form.get('hide_dates')
        if hide_dates:
            headers = [h for h in headers if h not in ['date_expi', 'date_achat']]
            data = [[row[i] for i, h in enumerate(headers)] for row in data]

    return render_template('categorie.html', data=data, headers=headers)


# End New code block


@app.route('/delete_row')
def delete_row():
    """
    Deletes a row from the table t_personnes_avoir_materiel in the MySQL database.
    """
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
    Displays the add person form.
    """
    return render_template('/actions/add_marque_form.html')


@app.route('/modify_marque', methods=['GET', 'POST'])
def modify_marque():
    """
    Processes the data from the mark modification form.
    """
    if request.method == 'POST':
        id = request.form['id']
        nom_marque = request.form['nom_marque']
        description_marque = request.form['description_marque']

        query = """
            UPDATE t_marque
            SET nom_marque = %s, description_marque = %s
            WHERE id_marque = %s
        """
        values = (nom_marque, description_marque, id)

        try:
            cursor.execute(query, values)
            cnx.commit()
            flash('La marque a été modifiée avec succès.', 'success')
        except Exception as e:
            cnx.rollback()
            flash('Une erreur est survenue lors de la modification de la marque. Veuillez réessayer plus tard.',
                  'danger')
            print(e)

        return redirect(url_for('marques'))

    else:
        return render_template('/actions/modify_marque_form.html')


@app.route('/get_row_data_marque')
def get_row_data_marque():
    # Get the id from the request parameters
    id = request.args.get('id')

    # Execute the SQL query to fetch the data for the row with the given id
    cursor.execute(f"SELECT * FROM t_marque WHERE id_marque={id}")
    row = cursor.fetchone()

    # Return the data as a JSON object
    return {
        "id": row[0],
        "nom_marque": row[1],
        "description_marque": row[2]
    }


@app.route('/add_marque', methods=['GET', 'POST'])
def add_marque():
    """
    Processes the data from the add mark form and adds it to the MySQL database.
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
    Retrieves the data from the t_brand table in the MySQL database and displays it on the "brands.html" page.
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
    Displays the "about.html" page.
    """
    return render_template('about.html')


if __name__ == '__main__':
    # context = ('ssl/cert.crt', 'ssl/cert.key')
    # ssl_context=context
    app.run(host=adresse_srv_flask, port=port_flask, debug=debug_flask)
