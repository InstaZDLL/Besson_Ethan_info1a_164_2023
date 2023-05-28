from flask import render_template, Blueprint

bp = Blueprint('success', __name__)


@bp.route('/success')
def about():
    # render the success-categorie.html template
    return render_template('/intermediate-pages/success-categorie.html')
