from flask import Blueprint, render_template, request, redirect, url_for, flash
from FlaskWebS import cnx, cursor

bp = Blueprint('marque', __name__)


@bp.route('/delete_row_marque', methods=['POST'])
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


@bp.route('/add_marque_form')
def add_marque_form():
    """
    Displays the add person form.
    """
    return render_template('/actions/add_marque_form.html')


@bp.route('/modify_marque', methods=['GET', 'POST'])
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

        return redirect(url_for('marque.marques'))

    else:
        return render_template('/actions/modify_marque_form.html')


@bp.route('/get_row_data_marque')
def get_row_data_marque():
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


@bp.route('/add_marque', methods=['GET', 'POST'])
def add_marque():
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
            flash('La marque avec cet id existe déjà.', 'danger')
            return redirect(url_for('marque.add_marque'))

        # insert new record
        query = """
            INSERT INTO t_marque (id_marque, nom_marque, description_marque)
            VALUES (%s, %s, %s)
        """
        values = (id_marque, nom_marque, description_marque)

        try:
            cursor.execute(query, values)
            cnx.commit()
            flash('La marque a été ajoutée avec succès.', 'success')
        except Exception as e:
            cnx.rollback()
            flash('Une erreur est survenue lors de l\'ajout de la marque. Veuillez réessayer plus tard.', 'danger')
            print(e)

        # Redirects to the 'marques' endpoint within the 'marque' Blueprint.
        # Using 'marque.marques' instead of just 'marques' specifies the endpoint within the Blueprint.
        # This ensures Flask can correctly build the URL for the 'marques' endpoint.
        return redirect(url_for('marque.marques'))
    else:
        return render_template('/actions/add_marque_form.html')


@bp.route('/marques')
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
