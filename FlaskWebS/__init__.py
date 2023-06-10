from dotenv import load_dotenv
from flask import Flask, render_template
import os
import mysql.connector

app = Flask(__name__, static_url_path='/static', template_folder='templates')
load_dotenv()

# Accessing variables in the .env file using os.environ
host_mysql = os.environ.get('HOST_MYSQL')
user_mysql = os.environ.get('USER_MYSQL')
pass_mysql = os.environ.get('PASS_MYSQL')
port_mysql = int(os.environ.get('PORT_MYSQL'))
name_bd_mysql = os.environ.get('NAME_BD_MYSQL')
name_file_dump_sql_bd = os.environ.get('NAME_FILE_DUMP_SQL_BD')

adresse_srv_flask = os.environ.get('ADRESSE_SRV_FLASK')
debug_flask = os.environ.get('DEBUG_FLASK') == 'true'
port_flask = int(os.environ.get('PORT_FLASK'))
app.secret_key = os.environ.get('SECRET_KEY_FLASK')

# Connection to the MySQL database
try:
    cnx = mysql.connector.connect(user=user_mysql, password=pass_mysql, host=host_mysql, port=port_mysql,
                                  database=name_bd_mysql)
except mysql.connector.Error as e:
    if e.errno == 1049:
        # Unknown database error
        print(f'La base de données \'{name_bd_mysql}\' n\'existe pas. création...')
        # Create a new connection without specifying a database name
        cnx = mysql.connector.connect(user=user_mysql, password=pass_mysql, host=host_mysql, port=port_mysql)
        cursor = cnx.cursor()
        # Execute a CREATE DATABASE statement
        cursor.execute(f'CREATE DATABASE {name_bd_mysql}')
        cursor.close()
        cnx.close()
        # Connect to the newly created database
        cnx = mysql.connector.connect(user=user_mysql, password=pass_mysql, host=host_mysql, port=port_mysql,
                                      database=name_bd_mysql)
    elif e.errno == 2003:
        print(
            f'\U0000274C Erreur lors de la connexion à la base de données : {str(e)}\n1. Vérifier que vous avez démarer '
            f'votre base '
            f'de données.\n2. Vérifier que les informations de connexion sont juste dans le fichier \033[1m.env\033['
            f'0m')
        exit(1)
    else:
        print(f'Message d\'erreur: {str(e)}')
        exit(1)

cursor = cnx.cursor()

# Import and register the route blueprint
from FlaskWebS.routes.index_route import bp as index_bp
from FlaskWebS.routes.about_route import bp as about_bp
from FlaskWebS.routes.categorie_route import bp as categorie_bp
from FlaskWebS.routes.marque_route import bp as marque_bp
from FlaskWebS.routes.personnes_route import bp as personnes_bp
from FlaskWebS.routes.stock_route import bp as stock_bp
from FlaskWebS.routes.success_route import bp as success_bp

app.register_blueprint(stock_bp)
app.register_blueprint(personnes_bp)
app.register_blueprint(marque_bp)
app.register_blueprint(categorie_bp)
app.register_blueprint(index_bp)
app.register_blueprint(about_bp)
app.register_blueprint(success_bp)


@app.errorhandler(404)
def not_found_error(error):
    """
    Handles the 404 error (page not found) and displays a custom error page.
    """
    return render_template('404.html'), 404
