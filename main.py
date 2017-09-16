from flask import Flask, render_template, render_template_string, abort, request, send_from_directory, session, redirect
import numpy as np
import hashlib
import db.dbutils as dbutils

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
    template_render = lambda local_error: render_template('login.html', error=local_error)
    if request.method == 'POST':
        db = dbutils.get_db()
        if not ('username' in request.form and 'password' in request.form):
            return template_render('Enter both the username and password.')
        if not dbutils.user_exists(request.form['username']):
            return template_render("That username does not exist in our system")
        if not check_username_password(request.form['username'], request.form['password']):
            return template_render('Invalid Credentials. Please try again.')
        else:
            session['username'] = request.form['username']
            session['logged_in'] = True
            return redirect('/loggedin')
    return render_template('login.html')


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
