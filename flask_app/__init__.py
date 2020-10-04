from flask import Flask, render_template
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
    cursor.execute('select * from user_info')
    rows = cursor.fetchall()

    print('Total Row(s):', cursor.rowcount)

    return render_template('index.html', rows=rows)
    

if __name__ == "__main__":
    app.run(debug=True)


db.close() 