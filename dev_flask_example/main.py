from flask import Flask, render_template, render_template_string, abort, request, send_from_directory, session, redirect
import numpy as np

app = Flask(__name__)

@app.route('/')
@app.route('/news/')
def list_articles():
    return render_template('index.html', title='kewl game')

@app.route('/loggedin')
def logged_in():
    return render_template('logged_in.html', message='YOUR LOGGED IN, ARENT YOU COOL NOW!!!', title='kewl game')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['username'] = request.form['username']
            session['logged_in'] = True
            return redirect('/loggedin')
    return render_template('login.html', error=error)


@app.route('/<path:path>')
def send_static(path): # Give source over web - for development purposes.
    return send_from_directory('.', path)

@app.errorhandler(404)
def error_404(error):
    return render_template("errors/404.html")

if __name__ == '__main__':
    #Not really sure what the secret key is for, but I need it to set a session var.
    import random
    x = str(random.getrandbits(100))
    print('superdupercoolkey-' + x)
    app.secret_key = 'superdupercoolkey-' + x
    app.run(threaded=True, debug=True)
