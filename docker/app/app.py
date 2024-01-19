from flask import Flask, send_from_directory
import pymysql
import random

from db_init import InitializeDb

app = Flask(__name__)

@app.route('/')
def base():
    tix = get_all_tickets()
    return send_from_directory('client/public', 'index.html', tickets=tix)

@app.route('/<path:path>')
def home(path):
    return send_from_directory('client/public', path)


@app.route('/rand')
def hello():
    return str(random.randint(1, 100))


def get_mysql_connection():
    conn = pymysql.connect(
        host='db',
        user='root',
        password='root_password',
        db='my_database',
    )
    return conn

def get_all_tickets():
    conn = get_mysql_connection()
    try:
        with conn.cursor() as cursor:
            # Execute the SQL query
            cursor.execute("SELECT * FROM tickets")
            # Fetch all the rows
            result = cursor.fetchall()
    finally:
        # Close the connection
        conn.close()
    
    return result

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    # Need to initialize the database AFTER running the app
    InitializeDb()