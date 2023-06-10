from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from FlaskWebS import cnx, cursor
import json

bp = Blueprint('categorie', __name__)


@bp.route('/delete_row_categorie', methods=['POST'])
def delete_row_categorie():
    id = request.form['id']
    cursor = cnx.cursor()
    # delete any referencing rows in the t_marque_avoir_materiel table
    cursor.execute('DELETE FROM t_marque_avoir_materiel WHERE fk_marque=%s', (id,))
    # delete the row in the t_marque table
    cursor.execute('DELETE FROM t_marque WHERE id_marque=%s', (id,))
    cnx.commit()
    cursor.close()
    return 'Row deleted'


@bp.route('/add_marque_form')
def add_categorie_form():
    """
    Displays the add person form.
    """
    return render_template('categorie/actions/add_categorie_form.html')


@bp.route('/modify_categorie', methods=['GET', 'POST'])
def modify_categorie():
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

        return redirect(url_for('success.success_categorie'))

    else:
        return render_template('categorie/actions/modify_categorie_form.html')


@bp.route('/get_row_data_categorie')
def get_row_data_categorie():
    # Get the id from the request parameters
    id = request.args.get('id')

    # Execute the SQL query to fetch the data for the row with the given id
    cursor.execute("SELECT * FROM t_marque WHERE id_marque=%s", (id,))
    row = cursor.fetchone()

    # Return the data as a JSON object
    return {
        "id": row[0],
        "nom_marque": row[1],
        "description_marque": row[2]
    }


@bp.route('/add_categorie', methods=['GET', 'POST'])
def add_categorie():
    """
    Processes the data from the add mark form and adds it to the MySQL database.
    """
    if request.method == 'POST':
        id_marque = request.form['id_marque']
        nom_marque = request.form['nom_marque']
        description_marque = request.form['description_marque']

        # check if id_marque already exists
        query = "SELECT id_marque FROM t_marque WHERE id_marque = %s"
        values = (id_marque,)
        cursor.execute(query, values)
        result = cursor.fetchone()
        if result is not None:
            return redirect(url_for('success.error_categorie'))

        # insert new record
        query = """
            INSERT INTO t_marque (id_marque, nom_marque, description_marque)
            VALUES (%s, %s, %s)
        """
        values = (id_marque, nom_marque, description_marque)

        try:
            cursor.execute(query, values)
            cnx.commit()
        except Exception as e:
            cnx.rollback()
            print(e)

        # Redirects to the 'marques' endpoint within the 'marque' Blueprint.
        # Using 'marque.marques' instead of just 'marques' specifies the endpoint within the Blueprint.
        # This ensures Flask can correctly build the URL for the 'marques' endpoint.
        return redirect(url_for('success.success_categorie'))
    else:
        return render_template('categorie/actions/add_categorie_form.html')


@bp.route('/categorie')
def categorie():
    """
    Retrieves the data from the t_brand table in the MySQL database and displays it on the "brands.html" page.
    """
    query = """
        SELECT * FROM t_categorie;
    """
    cursor.execute(query)
    data = cursor.fetchall()

    headers = [column[0] for column in cursor.description]

    return render_template('categorie/categorie.html', data=data, headers=headers)
