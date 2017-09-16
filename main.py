from flask import Flask, render_template, render_template_string, \
abort, request, send_from_directory, session, redirect
from flask_login import LoginManager, UserMixin, \
login_required, login_user, logout_user
import hashlib
import db.dbutils as dbutils

app = Flask(__name__)

pages = []

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'
login_manager.login_message = 'Please login to view the page'

@app.route('/')
@app.route('/index')
def list_articles():
    return render_template('index.html', title='kewl game', pages=pages)

@app.route('/loggedin')
@login_required
def logged_in():
    return render_template('logged_in.html', message='YOUR LOGGED IN, ARENT YOU COOL NOW!!!', title='kewl game')


@app.route('/login', methods=['GET', 'POST'])
def login():
    template_render = lambda local_error: render_template('login.html', error=local_error)
    if request.method == 'POST':
        if not ('username' in request.form and 'password' in request.form):
            return template_render('Enter both the username and password.')
        if not dbutils.check_username_password(request.form['username'], request.form['password']):
            return template_render('Invalid Credentials. Please try again.')
        else:
            session['username'] = request.form['username']
            current_user = user(request.form['username'])
            login_user(current_user)
            return redirect('/loggedin')
    return render_template('login.html')


@app.route('/<path:path>')
def send_static(path): # Give source over web - for development purposes.
    return send_from_directory('.', path)

@app.errorhandler(404)
def error_404(error):
    return render_template("errors/404.html")

class page:
    def __init__(self, url, name):
        self.url = url
        self.name = name

class user(UserMixin):
    def __init__(self, username):
        self.id = username

# callback to reload the user object
@login_manager.user_loader
def load_user(username):
    return user(username)

def loadPages():
    global pages
    pages = []
    pages.append(page('/login',    'login'))
    pages.append(page('/register', 'register'))

if __name__ == '__main__':
    #Not really sure what the secret key is for, but I need it to set a session var.
    import random
    x = str(random.getrandbits(100))
    print('superdupercoolkey-' + x)
    loadPages()
    app.secret_key = 'superdupercoolkey-' + x
    app.run(threaded=True, debug=True)
