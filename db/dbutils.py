import sqlite3
from flask import Flask, g
import db.dbconf
import hashlib
import json
from jinja2 import utils
import Calculator

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

def add_user_with_email(username, password, email):
    hash_func = hashlib.new("sha256")
    hash_func.update(bytes(password, 'utf-8'))
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password, email) VALUES (lower(?), (?), (?))", (username, hash_func.digest(), email))
    conn.commit()

def sanitize(username):
    return str(utils.escape(username))

def add_calculator(username, calculator):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT userID FROM users WHERE username=lower((?))",(username,))
    userID = cursor.fetchone()[0]
    calc_dat = serialize_calculator(calculator)
    cursor.execute("INSERT INTO calculator (userID, calculatorDat) VALUES ((?), (?))", (userID, calc_dat))
    conn.commit()

def get_calculator(username):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT userID FROM users WHERE username=lower((?))",(username,))
    userID = cursor.fetchone()[0]
    cursor.execute("SELECT calculatorDat FROM calculator WHERE userID=(?)", (userID, ))
    calc_dat = deserialize_calculator(cursor.fetchone()[0])
    return calc_dat

def serialize_calculator(calculator):
    data = {}
    data['amount_saved'] = calculator.amount_saved
    data['daily_savings'] = calculator.daily_savings
    data['days_until_grad'] = calculator.days_until_grad
    data['income_bracket'] = calculator.income_bracket
    data['max_money_needed'] = calculator.max_money_needed
    data['min_money_needed'] = calculator.min_money_needed
    return json.dumps(data)

def deserialize_calculator(calculatorDat):
    calc_data = json.loads(calculatorDat)[0]
    return Calculator.Calculator(calc_data['amount_saved'], calc_data['daily_savings'],
      calc_data['days_until_grad'], calc_data['income_bracket'],
      calc_data['max_money_needed'], calc_data['min_money_needed'])
