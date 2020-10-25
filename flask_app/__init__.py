from flask import Flask, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'flask_app'


mysql.init_app(app)


@app.route('/')
def display_db():
    db = mysql.connect()
    cursor = db.cursor()
    cursor.execute('select * from user_info')
    rows = cursor.fetchall()
    tokens = []
    for row in rows:
        tokens += row
    
    tokensString = ' '.join([str(elem) for elem in tokens]) 

    return render_template('index.html', token=tokensString)

if __name__ == "__main__":
    app.run()