from flask import Flask, render_template, request, redirect
import hashlib
import sqlite3

app = Flask(__name__) #creating flask app name

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/consultation/<int:api_key>')
def afficheListe(api_key):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients')
    data = cursor.fetchall()
    conn.close()

    if api_key == 5625719273:
        return render_template('read_data.html', data=data)
    return "api_key !!"

@app.route('/fiche_client/<int:post_id>')
def Readfiche(post_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients WHERE id = ?', (post_id,))
    data = cursor.fetchall()
    conn.close()

@app.route('/paris/<int:api_key>')
def meteo(api_key):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients')
    data = cursor.fetchall()
    conn.close()
    if api_key == 5625719273:
        return jsonify(results=data)
    return "api_key !!"

@app.route('/graphique/<int:api_key>')
def afficheGraph(api_key):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients')
    data = cursor.fetchall()
    conn.close()
    if api_key == 5625719273:
        return render_template('graphique.html', data=data)
    return "api_key !!"

if(__name__ == "__main__"):
    app.run() (modifié)
