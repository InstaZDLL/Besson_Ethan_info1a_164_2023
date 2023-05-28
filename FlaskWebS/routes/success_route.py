from flask import render_template, Blueprint

bp = Blueprint('success', __name__)


@bp.route('/success')
def about():
    # render the success.html template
    return render_template('/intermediate-pages/success.html')
