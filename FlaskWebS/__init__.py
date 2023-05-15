from flask import Flask

app = Flask(__name__, static_url_path='/static', template_folder='templates')

# Import and register the route blueprint
from FlaskWebS.routes.index_route import bp as index_bp
from FlaskWebS.routes.about_route import bp as about_bp

app.register_blueprint(index_bp)
app.register_blueprint(about_bp)

# Other configuration and code for your Flask application
# ...
