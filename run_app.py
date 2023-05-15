from FlaskWebS import app, adresse_srv_flask,port_flask,debug_flask

if __name__ == '__main__':
    # context = ('ssl/cert.crt', 'ssl/cert.key')
    # ssl_context=context
    app.run(host=adresse_srv_flask, port=port_flask, debug=debug_flask)
