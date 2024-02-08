from flask import Flask, render_template, request, redirect
import hashlib
import sqlite3

app = Flask(__name__) #creating flask app name

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/resume_1')
def resume_1():
    return render_template("resume_1.html")

@app.route('/resume_2')
def resume_2():
    return render_template("resume_2.html")

@app.route('/resume_template')
def resume_template():
    return render_template("resume_template.html")

@app.route('/consultation/<int:post_id>')
def ReadBDD(post_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients;')
    data = cursor.fetchall()
    conn.close()

    if post_id != 5625719273: 
        return "API_key not avalaible"
    else:
    # Rendre le template HTML et transmettre les données
    return render_template('read_data.html', data=data)

@app.route('/chart_data/<api_key>')
def chart_data(api_key):
    if api_key != '5625719273':
        return "API_key not available"

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT Jour, COUNT(*) as Messages FROM clients GROUP BY Jour;')
    data = cursor.fetchall()
    conn.close()

    # Convertir les données en un format compatible avec le graphique
    chart_data = [{'Jour': entry[0], 'Messages': entry[1]} for entry in data]

    return jsonify({'results': chart_data})

if(__name__ == "__main__"):
    app.run()
