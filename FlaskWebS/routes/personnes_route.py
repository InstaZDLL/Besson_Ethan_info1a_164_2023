from flask import Blueprint, render_template, request
from FlaskWebS import cnx, cursor

# Import your MySQL connection and cursor here
# Replace 'cnx' and 'cursor' with your own connection and cursor objects

bp = Blueprint('personnes', __name__)


@bp.route('/personnes')
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

    return render_template('personnes/personnes.html', data=data, headers=headers)


@bp.route('/delete_row')
def delete_row():
    """
    Deletes a row from the table t_personnes_avoir_materiel in the MySQL database.
    """
    # Get the row id from the request parameters
    row_id = request.args.get('id')

    # Execute the SQL query to delete the row with the given id
    cursor.execute("DELETE FROM t_personnes_avoir_materiel WHERE id_personnes_avoir_materiel=%s", (row_id,))

    # Commit the changes to the database
    cnx.commit()

    # Return a JSON response indicating success
    return {"status": "success"}
