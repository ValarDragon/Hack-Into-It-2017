import sqlite3
import db.dbconf
import hashlib
import os
import Calculator
import json

def create_db():
    #Meant to be ran in python3 -i dbutils.py
    if os.path.isfile(db.dbconf.database_file):
        os.remove(db.dbconf.database_file)
    conn = sqlite3.connect(db.dbconf.database_file)
    c=conn.cursor()
    schema = ""
    with open('db/schema.sql', 'r') as schema_file:
        schema = schema_file.read()
    for line in schema.split(';'):
        c.execute(line)
    conn.commit()
    add_sample_users()
    add_sample_calculator()
    x= get_calculator('admin')
    print(x)
    print(dir(x))

def add_sample_calculator():
    calculator = Calculator.Calculator(1,2,3,4,5,6)
    add_calculator('admin',calculator)


def add_calculator(username, calculator):
    conn = sqlite3.connect(db.dbconf.database_file)
    cursor = conn.cursor()
    cursor.execute("SELECT userID FROM users WHERE username=lower((?))",(username,))
    userID = cursor.fetchone()[0]
    calc_dat = serialize_calculator(calculator)
    cursor.execute("INSERT INTO calculator (userID, calculatorDat) VALUES ((?), (?))", (userID, calc_dat))
    conn.commit()

def get_calculator(username):
    conn = sqlite3.connect(db.dbconf.database_file)
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

def add_sample_users():
    sample_users = {'admin':'admin', 'potatoman':'lol'}
    for k in sample_users:
        add_user(k, sample_users[k])

def add_user(username, password):
    hash_func = hashlib.new("sha256")
    hash_func.update(bytes(password, 'utf-8'))
    conn = sqlite3.connect(db.dbconf.database_file)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (lower(?), (?))", (username, hash_func.digest()))
    conn.commit()

def check_user(username, password):
    conn = sqlite3.connect(db.dbconf.database_file)
    cursor = conn.cursor()
    hash_func = hashlib.new("sha256")
    hash_func.update(bytes(password, 'utf-8'))
    password = hash_func.digest()
    cursor.execute("SELECT count(*) FROM users WHERE username=lower((?)) AND password=(?)",(username, password))
    return cursor.fetchone()[0] != 0
