import sqlite3
from flask import Flask, g
import db.dbconf
import hashlib
from jinja2 import utils

app = Flask(__name__)
DATABASE = db.dbconf.database_file

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection():
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def user_exists(username):
    cursor = get_db().cursor()
    cursor.execute("SELECT count(*) FROM users WHERE username=lower((?))",(username,))
    return cursor.fetchone()[0] != 0

def check_username_password(username,password):
    hash_func = hashlib.new("sha256")
    hash_func.update(bytes(password, 'utf-8'))
    password = hash_func.digest()
    cursor = get_db().cursor()
    cursor.execute("SELECT count(*) FROM users WHERE username=lower((?)) AND password=(?)",(username, password))
    return cursor.fetchone()[0] != 0

def add_user(username, password):
    hash_func = hashlib.new("sha256")
    hash_func.update(bytes(password, 'utf-8'))
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (lower(?), (?))", (username, hash_func.digest()))
    conn.commit()

def sanitize(username):
    return str(utils.escape(username))
