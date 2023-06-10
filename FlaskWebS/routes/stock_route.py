from flask import render_template, Blueprint
from FlaskWebS import cursor

bp = Blueprint('materiel', __name__)


@bp.route('/stock')
def stock():
    """
    Retrieves the data from the table t_materiel in the MySQL database and displays it on the page "stock.html".
    """
    query = "SELECT * FROM t_materiel"
    cursor.execute(query)
    data = cursor.fetchall()

    return render_template('stock/stock.html', data=data)
