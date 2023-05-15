from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static', template_folder='templates')

# Import and register the route blueprint
from FlaskWebS.routes.index_route import bp as index_bp
from FlaskWebS.routes.about_route import bp as about_bp

app.register_blueprint(index_bp)
app.register_blueprint(about_bp)


@app.errorhandler(404)
def not_found_error(error):
    """
    Handles the 404 error (page not found) and displays a custom error page.
    """
    return render_template('404.html'), 404
