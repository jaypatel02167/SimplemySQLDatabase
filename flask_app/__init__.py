from flask import Flask, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'P@ssw0rd'
app.config['MYSQL_DATABASE_DB'] = 'flask_app'


mysql.init_app(app)


@app.route('/')
def display_db():
    db = mysql.connect()
    cursor = db.cursor()
    cursor.execute('select * from user_info')
    rows = cursor.fetchall()

    #print('Total Row(s):', cursor.rowcount)
    # for x in rows:
    #     print(x)

    return render_template('index.html', token=rows)

if __name__ == "__main__":
    app.run()