from flask import Flask
import mysql.connector as mysql

app = Flask(__name__)

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "P@ssw0rd",
    database = "flask_app"
)

cursor = db.cursor()


@app.route('/')
def hello_world():
    return 'TEST'

if __name__ == "__main__":
    app.run()


db.close() 