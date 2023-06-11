from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from FlaskWebS import cnx, cursor

# Import your MySQL connection and cursor here
# Replace 'cnx' and 'cursor' with your own connection and cursor objects

bp = Blueprint('personnes_edit', __name__)


@bp.route('/personnes_edit')
def personnes_edit():
    """
    Retrieves the data from the t_brand table in the MySQL database and displays it on the "brands.html" page.
    """
    query = """
        SELECT id_personnes, prenom_pers, nom_pers, dep_pers FROM t_personnes;
    """
    cursor.execute(query)
    data = cursor.fetchall()

    headers = [column[0] for column in cursor.description]

    return render_template('/personnes/personnes-edit/personnes_edit.html', data=data, headers=headers)


@bp.route('/add_personnes_edit', methods=['GET', 'POST'])
def add_personnes_edit():
    """
    Processes the data from the add mark form and adds it to the MySQL database.
    """
    if request.method == 'POST':
        id_personnes = request.form['id_personnes']
        prenom_pers = request.form['prenom_pers']
        nom_pers = request.form['nom_pers']
        dep_pers = request.form['dep_pers']

        # check if id_marque already exists
        query = "SELECT id_personnes FROM t_personnes WHERE id_personnes = %s"
        values = (id_personnes,)
        cursor.execute(query, values)
        result = cursor.fetchone()
        if result is not None:
            return redirect(url_for('success.error_pers_edit'))

        # insert new record
        query = """
            INSERT INTO t_personnes (id_personnes, prenom_pers, nom_pers, dep_pers)
            VALUES (%s, %s, %s, %s)
        """
        values = (id_personnes, prenom_pers, nom_pers, dep_pers)

        try:
            cursor.execute(query, values)
            cnx.commit()
        except Exception as e:
            cnx.rollback()
            print(e)

        # Redirects to the 'marques' endpoint within the 'marque' Blueprint.
        # Using 'marque.marques' instead of just 'marques' specifies the endpoint within the Blueprint.
        # This ensures Flask can correctly build the URL for the 'marques' endpoint.
        return redirect(url_for('success.success_pers_edit'))
    else:
        return render_template('personnes/personnes-edit/actions/personnes_edit_add.html')


@bp.route('/get_data_to_delete_personnes', methods=['GET'])
def get_data_to_delete_personnes():
    id = request.args.get('id')
    cursor = cnx.cursor()
    # query the database for the data that will be deleted
    query = '''
        SELECT t_materiel.id_materiel, t_materiel.nom_mat
        FROM t_personnes_avoir_materiel
        JOIN t_materiel ON t_personnes_avoir_materiel.fk_materiel = t_materiel.id_materiel
        WHERE t_personnes_avoir_materiel.fk_personnes = %s
        UNION
        SELECT t_materiel.id_materiel, t_materiel.nom_mat
        FROM t_personnes_retrait_materiel
        JOIN t_materiel ON t_personnes_retrait_materiel.fk_materiel = t_materiel.id_materiel
        WHERE t_personnes_retrait_materiel.fk_personnes = %s
        UNION
        SELECT t_materiel.id_materiel, t_materiel.nom_mat
        FROM t_personnes_ajout_materiel
        JOIN t_materiel ON t_personnes_ajout_materiel.fk_materiel = t_materiel.id_materiel
        WHERE t_personnes_ajout_materiel.fk_personnes = %s
    '''
    cursor.execute(query, (id, id, id))
    data = cursor.fetchall()
    # determine which tables will be affected
    affected_tables = ['t_personnes']
    if len(data) > 0:
        affected_tables.append('t_personnes_avoir_materiel')
        affected_tables.append('t_personnes_retrait_materiel')
        affected_tables.append('t_personnes_ajout_materiel')
        affected_tables.append('t_materiel')
    cursor.close()
    # return the data and affected tables as a JSON object
    return jsonify({'data': data, 'affected_tables': affected_tables})



@bp.route('/delete_row_personnes', methods=['POST'])
def delete_row_personnes():
    id = request.form['id']
    cursor = cnx.cursor()
    # delete any referencing rows in the t_personnes_avoir_materiel table
    cursor.execute('DELETE FROM t_personnes_avoir_materiel WHERE fk_personnes=%s', (id,))
    # delete any referencing rows in the t_personnes_ajout_materiel table
    cursor.execute('DELETE FROM t_personnes_ajout_materiel WHERE fk_personnes=%s', (id,))
    # delete any referencing rows in the t_personnes_retrait_materiel table
    cursor.execute('DELETE FROM t_personnes_retrait_materiel WHERE fk_personnes=%s', (id,))
    # delete the row in the t_personnes table
    cursor.execute('DELETE FROM t_personnes WHERE id_personnes=%s', (id,))
    cnx.commit()
    cursor.close()
    return 'Row deleted'


