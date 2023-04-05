import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://lab10db_user:t43K9ALBZmgBQRax2uqi6xoypoR3awHc@dpg-cgme5qjk9u59cru7vd60-a/lab10db")
    conn.close()
    return "Database Connection Successful"
@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgres://lab10db_user:t43K9ALBZmgBQRax2uqi6xoypoR3awHc@dpg-cgme5qjk9u59cru7vd60-a/lab10db")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball (
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Sucessfully Created"

    
    
    

