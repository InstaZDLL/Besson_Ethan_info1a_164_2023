from FlaskWebS import app, adresse_srv_flask, port_flask, debug_flask
from FlaskWebS.database import mysql_dump_import

if __name__ == '__main__':

    """
        If you want to enable the https, trust the crt file to Trusted Root Certificates and uncomment these two lines
        context = ('ssl/cert.crt', 'ssl/cert.key')
        ssl_context=context
    """

    # Run the file mysql_dump_import.py
    # mysql_dump_import.run()
    # Remove the debug=debug_flask to avoid the double execution of the mysql_dump_import
    app.run(host=adresse_srv_flask, port=port_flask, debug=debug_flask)
