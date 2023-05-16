from flask import render_template, Blueprint

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    """
    Displays the home page of the Flask application.
    """
    return render_template('index.html')