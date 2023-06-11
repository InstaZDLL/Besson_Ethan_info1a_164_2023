from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from FlaskWebS import cnx, cursor
import json

bp = Blueprint('categorie', __name__)


@bp.route('/delete_row_categorie', methods=['POST'])
def delete_row_categorie():
    id = request.form['id']
    cursor = cnx.cursor()
    # delete any referencing rows in the t_marque_avoir_materiel table
    cursor.execute('DELETE FROM t_categorie_avoir_materiel WHERE fk_categorie=%s', (id,))
    # delete the row in the t_marque table
    cursor.execute('DELETE FROM t_categorie WHERE id_categorie=%s', (id,))
    cnx.commit()
    cursor.close()
    return 'Row deleted'


@bp.route('/get_data_to_delete', methods=['GET'])
def get_data_to_delete():
    id = request.args.get('id')
    cursor = cnx.cursor()
    # query the database for the data that will be deleted
    query = '''
        SELECT t_materiel.id_materiel, t_materiel.nom_mat
        FROM t_categorie_avoir_materiel
        JOIN t_materiel ON t_categorie_avoir_materiel.fk_materiel = t_materiel.id_materiel
        WHERE t_categorie_avoir_materiel.fk_categorie = %s
    '''
    cursor.execute(query, (id,))
    data = cursor.fetchall()
    # determine which tables will be affected
    affected_tables = []
    if len(data) > 0:
        affected_tables.append('t_categorie_avoir_materiel')
        affected_tables.append('t_materiel')
    cursor.close()
    # return the data and affected tables as a JSON object
    return jsonify({'data': data, 'affected_tables': affected_tables})


@bp.route('/add_categorie_form')
def add_categorie_form():
    """
    Displays the add person form.
    """
    return render_template('/categorie/actions/add_categorie_form.html')


@bp.route('/modify_categorie', methods=['GET', 'POST'])
def modify_categorie():
    """
    Processes the data from the mark modification form.
    """
    if request.method == 'POST':
        id = request.form['id']
        nom_cat = request.form['nom_cat']
        description_cat = request.form['description_cat']

        query = """
            UPDATE t_categorie
            SET nom_cat = %s, description_cat = %s
            WHERE id_categorie = %s
        """
        values = (nom_cat, description_cat, id)

        try:
            cursor.execute(query, values)
            cnx.commit()
            flash('La marque a été modifiée avec succès.', 'success')
        except Exception as e:
            cnx.rollback()
            flash('Une erreur est survenue lors de la modification de la marque. Veuillez réessayer plus tard.',
                  'danger')
            print(e)

        return redirect(url_for('success.success_cat'))

    else:
        return render_template('/categorie/actions/modify_categorie_form.html')


@bp.route('/get_row_data_categorie')
def get_row_data_categorie():
    # Get the id from the request parameters
    id = request.args.get('id')

    # Execute the SQL query to fetch the data for the row with the given id
    cursor.execute("SELECT * FROM t_categorie WHERE id_categorie=%s", (id,))
    row = cursor.fetchone()

    # Return the data as a JSON object
    return {
        "id": row[0],
        "nom_cat": row[1],
        "description_cat": row[2]
    }


@bp.route('/add_categorie', methods=['GET', 'POST'])
def add_categorie():
    """
    Processes the data from the add mark form and adds it to the MySQL database.
    """
    if request.method == 'POST':
        id_categorie = request.form['id_categorie']
        nom_cat = request.form['nom_cat']
        description_cat = request.form['description_cat']

        # check if id_marque already exists
        query = "SELECT id_categorie FROM t_categorie WHERE id_categorie = %s"
        values = (id_categorie,)
        cursor.execute(query, values)
        result = cursor.fetchone()
        if result is not None:
            return redirect(url_for('success.error_cat'))

        # insert new record
        query = """
            INSERT INTO t_categorie (id_categorie, nom_cat, description_cat)
            VALUES (%s, %s, %s)
        """
        values = (id_categorie, nom_cat, description_cat)

        try:
            cursor.execute(query, values)
            cnx.commit()
        except Exception as e:
            cnx.rollback()
            print(e)

        # Redirects to the 'marques' endpoint within the 'marque' Blueprint.
        # Using 'marque.marques' instead of just 'marques' specifies the endpoint within the Blueprint.
        # This ensures Flask can correctly build the URL for the 'marques' endpoint.
        return redirect(url_for('success.success_cat'))
    else:
        return render_template('/categorie/actions/add_categorie_form.html')


@bp.route('/categorie')
def categorie():
    """
    Retrieves the data from the t_brand table in the MySQL database and displays it on the "brands.html" page.
    """
    query = """
        SELECT id_categorie, nom_cat, description_cat FROM t_categorie;
    """
    cursor.execute(query)
    data = cursor.fetchall()

    headers = [column[0] for column in cursor.description]

    return render_template('/categorie/categorie.html', data=data, headers=headers)
