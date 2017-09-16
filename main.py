from flask import Flask, render_template, render_template_string, abort, request, send_from_directory, session, redirect
import numpy as np

app = Flask(__name__)

@app.route('/')
@app.route('/news/')
def list_articles():
    return render_template('index.html', title='kewl game')

@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('.', path)

@app.errorhandler(404)
def error_404(error):
    return render_template("errors/404.html")

if __name__ == '__main__':
    #Not really sure what the secret key is for, but I need it to set a session var.
    app.secret_key = 'superdupercoolkey'
    app.run(threaded=True, debug=True)
