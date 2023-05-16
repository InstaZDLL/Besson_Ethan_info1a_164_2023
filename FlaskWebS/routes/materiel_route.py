from flask import render_template, Blueprint
from FlaskWebS import cursor

bp = Blueprint('materiel', __name__)


@bp.route('/materiel')
def materiel():
    """
    Retrieves the data from the table t_materiel in the MySQL database and displays it on the page "materiel.html".
    """
    query = "SELECT * FROM t_materiel"
    cursor.execute(query)
    data = cursor.fetchall()

    return render_template('materiel.html', data=data)
