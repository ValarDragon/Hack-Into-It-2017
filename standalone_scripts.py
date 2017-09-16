import sqlite3
import db.dbconf
def create_db():
    #Meant to be ran in python3 -i dbutils.py
    conn = sqlite3.connect(db.dbconf.database_file)
    c=conn.cursor()
    schema = ""
    with open('db/schema.sql', 'r') as schema_file:
        schema = schema_file.read()
    for line in schema.split(';'):
        c.execute(line)
    conn.commit()
