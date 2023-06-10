from flask import render_template, Blueprint

bp = Blueprint('success', __name__)


@bp.route('/success_cat')
def success_cat():
    # render the success-materiel.html template
    return render_template('/materiel/intermediate-pages/success-materiel.html')


@bp.route('/success_marq')
def success_marq():
    # render the success-materiel.html template
    return render_template('/marque/intermediate-pages/success-marques.html')


@bp.route('/error_cat')
def error_cat():
    # render the success-materiel.html template
    return render_template('/materiel/intermediate-pages/error_materiel.html')


@bp.route('/error_marq')
def error_marq():
    # render the success-materiel.html template
    return render_template('/marque/intermediate-pages/error_marques.html')
