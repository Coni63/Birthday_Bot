import sqlite3
import re

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/add/', methods=['POST'])
def add_people():
    if request.method == 'POST':
        for key, val in request.values.items():
            if key == "name":
                name = val
            elif key == "date":
                date = val
            elif key == "twitter":
                twitter = val
            elif key == "country":
                country = val
            elif key == "status":
                status = val

        conn = sqlite3.connect('databases/proposition.db')
        c = conn.cursor()
        q = "INSERT INTO birthday VALUES ('{}','{}','{}', '{}', '{}', '{}')".format(date, name, twitter, "", country, status)
        c.execute(q)
        conn.commit()
        conn.close()
        return ""

@app.route('/listing/')
def listing():
    conn = sqlite3.connect('databases/birthday.db')
    c = conn.cursor()
    c.execute('SELECT name, twitter, country, birthday FROM birthday WHERE country = "France"')
    results = c.fetchall()
    conn.close()
    return render_template('listing.html', results = results)

@app.route('/')
def index():
    conn = sqlite3.connect('databases/birthday.db')
    c = conn.cursor()
    c.execute('SELECT DISTINCT country FROM birthday ORDER BY country')
    result = c.fetchall()
    result = [x[0] for x in result]
    conn.close()
    return render_template('main.html', countries = result)

if __name__ == "__main__":
    app.run(debug=True)