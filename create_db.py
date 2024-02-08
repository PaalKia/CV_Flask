import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO clients (nom, prenom, message) VALUES (?, ?, ?)",('DUPONT', 'Emilie', 'Je veux te recruter'))
cur.execute("INSERT INTO clients (nom, prenom, message) VALUES (?, ?, ?)",('PaalKia', 'LeBoss', 'Help'))
cur.execute("INSERT INTO clients (nom, prenom, message) VALUES (?, ?, ?)",('The', 'Grinch', 'SOS'))
cur.execute("INSERT INTO clients (nom, prenom, message) VALUES (?, ?, ?)",('SHE/HER', 'LomeBronzé', 'Pourquoi moi ?'))
cur.execute("INSERT INTO clients (nom, prenom, message) VALUES (?, ?, ?)",('M.', 'Farceur', 'Salut c'est moi monisuer farceur !'))



connection.commit()
connection.close()
