from flask import render_template, request, redirect, url_for, flash, jsonify, Blueprint
from FlaskWebS import cnx, cursor
from PyFormModify import ModifyMaterielForm
from datetime import datetime
import json

bp = Blueprint('categorie', __name__)


@bp.route("/show_modify_materiel")
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
    cursor.execute(
        "SELECT t_categorie.nom_cat FROM t_categorie_avoir_materiel JOIN t_categorie ON t_categorie_avoir_materiel.fk_categorie = t_categorie.id_categorie WHERE t_categorie_avoir_materiel.fk_materiel=%s",
        (id_materiel,))
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

    # render the modify_materiel_form.html template and pass the data and categories to it
    return render_template("/materiel/actions/modify_materiel_form.html", data=data, form=form, categories=categories,
                           id=id_materiel)


@bp.route("/modify_materiel_form", methods=["POST"])
def modify_materiel_form():
    # get the form data
    id_mat = request.form["id_mat"]
    old_id_mat = request.form["old_id_mat"]

    # check if the modified ID already exists
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM t_materiel WHERE id_materiel=%s", (id_mat,))
    existing_row = cursor.fetchone()

    if existing_row and id_mat != old_id_mat:
        cursor.close()
        return redirect(url_for("success.error_cat"))

    # get the form data
    id_mat = request.form["id_mat"]
    nom_mat = request.form["nom_mat"]
    model_mat = request.form["model_mat"]
    serial_num = request.form["serial_num"]
    date_achat = request.form["date_achat"]
    date_expi = request.form["date_expi"]
    prix_mat = request.form["prix_mat"]
    nom_cat = request.form.get("nom_cat")

    # validate and convert the date values
    try:
        date_achat = datetime.strptime(date_achat, "%Y-%m-%dT%H:%M").strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        date_achat = None
    try:
        date_expi = datetime.strptime(date_expi, "%Y-%m-%dT%H:%M").strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        date_expi = None

    # get the old value for id_materiel from the form data
    old_id_mat = request.form["old_id_mat"]

    try:
        # update the id_materiel value in the t_materiel table
        cursor.execute("UPDATE t_materiel SET id_materiel=%s WHERE id_materiel=%s", (id_mat, old_id_mat))

        # update the other fields in the t_materiel table
        cursor.execute(
            "UPDATE t_materiel SET nom_mat=%s, model_mat=%s, serial_num=%s, date_achat=%s, date_expi=%s, prix_mat=%s WHERE id_materiel=%s",
            (nom_mat, model_mat, serial_num, date_achat, date_expi, prix_mat, id_mat))

        # update the data in the t_categorie_avoir_materiel and t_categorie tables
        cursor.execute("SELECT * FROM t_categorie WHERE nom_cat=%s", (nom_cat,))
        categorie_data = cursor.fetchone()
        if categorie_data:
            cursor.execute("UPDATE t_categorie_avoir_materiel SET fk_categorie=%s WHERE fk_materiel=%s",
                           (categorie_data[0], id_mat))
        else:
            cursor.execute("INSERT INTO t_categorie (nom_cat) VALUES (%s)", (nom_cat,))
            cursor.execute("UPDATE t_categorie_avoir_materiel SET fk_categorie=%s WHERE fk_materiel=%s",
                           (cursor.lastrowid, id_mat))

        # commit the changes
        cnx.commit()
    except:
        # rollback the changes if an error occurs
        cnx.rollback()
        raise

    # redirect to the success page
    return redirect(url_for("success.success_cat"))


@bp.route('/delete_row_materiel', methods=['POST'])
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


@bp.route('/get_referencing_tables', methods=['POST'])
def get_referencing_tables():
    id = request.form['id']
    referencing_tables = []

    # Check if the id is present in t_categorie_avoir_materiel
    cursor.execute('SELECT * FROM t_categorie_avoir_materiel WHERE fk_materiel=%s', (id,))
    if cursor.fetchall():
        referencing_tables.append('t_categorie_avoir_materiel')

    # Check if the id is present in t_departement_avoir_materiel
    cursor.execute('SELECT * FROM t_departement_avoir_materiel WHERE fk_materiel=%s', (id,))
    if cursor.fetchall():
        referencing_tables.append('t_departement_avoir_materiel')

    # Check if the id is present in t_fournisseur_avoir_materiel
    cursor.execute('SELECT * FROM t_fournisseur_avoir_materiel WHERE fk_materiel=%s', (id,))
    if cursor.fetchall():
        referencing_tables.append('t_fournisseur_avoir_materiel')

    # Check if the id is present in t_marque_avoir_materiel
    cursor.execute('SELECT * FROM t_marque_avoir_materiel WHERE fk_materiel=%s', (id,))
    if cursor.fetchall():
        referencing_tables.append('t_marque_avoir_materiel')

    # Check if the id is present in t_personnes_ajout_materiel
    cursor.execute('SELECT * FROM t_personnes_ajout_materiel WHERE fk_materiel=%s', (id,))
    if cursor.fetchall():
        referencing_tables.append('t_personnes_ajout_materiel')

    # Check if the id is present in t_personnes_ajout_materiel
    cursor.execute('SELECT * FROM t_personnes_avoir_materiel WHERE fk_materiel=%s', (id,))
    if cursor.fetchall():
        referencing_tables.append('t_personnes_avoir_materiel')

    # Check if the id is present in t_personnes_ajout_materiel
    cursor.execute('SELECT * FROM t_personnes_retrait_materiel WHERE fk_materiel=%s', (id,))
    if cursor.fetchall():
        referencing_tables.append('t_personnes_retrait_materiel')

    # Construct the response as a JSON object
    response = {'referencing_tables': referencing_tables}

    # Return the response as JSON
    return json.dumps(response)


@bp.route('/add_materiel', methods=['GET', 'POST'])
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

        # Check if the id already exists in the database
        query = "SELECT * FROM t_materiel WHERE id_materiel = %s"
        cursor.execute(query, (id_materiel,))
        if cursor.fetchone():
            # The id already exists
            return redirect(url_for('success.error_cat'))
        else:
            # The id does not exist, you can insert a new record
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
                flash(
                    'Une erreur est survenue lors de l\'ajout de la catégorie du matériel. Veuillez réessayer plus tard.',
                    'danger')
                print(e)

            return redirect(url_for('success.success_cat'))

    else:
        return render_template('/materiel/actions/add_materiel_form.html', categories=categories)


@bp.route('/add_materiel_form')
def add_materiel_form():
    """
    Displays the add person form.
    """
    return render_template('/materiel/actions/add_materiel_form.html')


@bp.route('/filter', methods=['POST'])
def filter_data():
    hide_dates = request.form.get('hide_dates')
    if hide_dates == "1":
        headers = [h for h in headers if h not in ['date_achat', 'date_expi']]
        data = [[row[i] for i in range(len(row)) if headers[i] not in ['date_achat', 'date_expi']] for row in data]
    else:
        headers = [column[0] for column in cursor.description]
        data = cursor.fetchall()
    return render_template('data_table.html', headers=headers, data=data)


@bp.route('/materiel', methods=['GET', 'POST'])
def materiel():
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

    return render_template('/materiel/categorie.html', data=data, headers=headers)


# End New code block

@bp.route("/check_id")
def check_id():
    id_mat = request.args.get("id")

    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM t_materiel WHERE id_materiel=%s", (id_mat,))
    existing_row = cursor.fetchone()

    if existing_row:
        cursor.close()
        return "exists"
    else:
        cursor.close()
        return "not_exists"
