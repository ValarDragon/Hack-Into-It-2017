import sqlite3
import db.dbconf
import hashlib
import os
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
