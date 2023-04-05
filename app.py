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
    

