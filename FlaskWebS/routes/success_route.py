from flask import render_template, Blueprint

bp = Blueprint('success', __name__)


@bp.route('/success_cat')
def success_cat():
    # render the success-categorie.html template
    return render_template('/intermediate-pages/success-categorie.html')


@bp.route('/success_marq')
def success_marq():
    # render the success-categorie.html template
    return render_template('/intermediate-pages/success-marques.html')
