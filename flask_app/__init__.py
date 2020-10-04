#INSERT INTO user_info (username, user_id) VALUES ("Caleb",8000003);

from flask import Flask, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'P@ssw0rd'
app.config['MYSQL_DATABASE_DB'] = 'flask_app'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)


@app.route('/')
def display_db():
    db = mysql.connect()
    cursor = db.cursor()
    cursor.execute('select * from user_info')
    rows = cursor.fetchall()

    print('Total Row(s):', cursor.rowcount)

    return render_template('index.html', rows=rows)
    #return str(rows)  

if __name__ == "__main__":
    app.run()