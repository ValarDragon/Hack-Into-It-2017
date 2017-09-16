import sqlite3
from flask import Flask, g
import db.dbconf
import hashlib

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
    if not user_exists(username):
        return False
    cursor = get_db().cursor()
    cursor.execute("SELECT count(*) FROM users WHERE username=lower((?)) AND password=(?)",(username, password))
    return cursor.fetchone()[0] != 0
