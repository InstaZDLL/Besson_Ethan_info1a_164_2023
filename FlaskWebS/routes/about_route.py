from flask import render_template, Blueprint

bp = Blueprint('about', __name__)


@bp.route('/about')
def about():
    """
    Displays the "about.html" page.
    """
    return render_template('about.html')

# Other route functions and logic
# ...
