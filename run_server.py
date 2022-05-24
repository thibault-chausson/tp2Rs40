# -*- coding: utf-8 -*-
"""

Created on May 2022
@author: Mr ABBAS-TURKI

"""
import pem
from flask import Flask, render_template, request
from build import SERVER_PUBLIC_KEY_FILENAME, SERVER_PRIVATE_KEY_FILENAME
import sqlite3



#conn = sqlite3.connect('myDB.db')
#cur = conn.cursor()
#reqSup = "DELETE FROM log WHERE userName='jean'"
#reqLog = "create table log (id integer primary key autoincrement, userName text, pass text)"
#reqAdd="insert into log (userName, pass) values ('jean', 'pierre')"
#reqSuperLog = "create table superLog (id integer primary key autoincrement, userName text, pass text)"
#reqSuperAdd="insert into log (userName, pass) values ('tibo2', 'arti')"
#cur.execute(reqSuperAdd)
#conn.commit()
#conn.close()


# définir le message secret
SECRET_MESSAGE = "nouveaumotsdepassesupersympatiquepastroplongenpluscestcool"  # hypsilophodon
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def connexion():
    return render_template("login.html")
def deconnexion():
    de1 = request.form['decon']
    if de1 == "deco":
        return render_template("login.html")

@app.route('/logSuper', methods=['POST', 'GET'])
def aller():
    return render_template("logSuperUser.html")





database = {'jean': 'pierre', 'christophe': 'voyage', 'dider': 'paul'}


@app.route('/motDePasse', methods=['POST', 'GET'])
def login():
    name1 = request.form['username']
    pwd = request.form['password']
    conn2 = sqlite3.connect('myDB.db')
    cur2 = conn2.cursor()
    cur2.execute("SELECT COUNT(pass) FROM log WHERE userName=?", (name1,))
    rows2 = cur2.fetchall()
    conn2.close()
    if rows2[0][0] ==0:
        return render_template('login.html', info='Utilisateur inconnu')
    else:
        conn3 = sqlite3.connect('myDB.db')
        cur3 = conn3.cursor()
        cur3.execute("SELECT pass FROM log WHERE userName=?", (name1,))
        rows3 = cur3.fetchall()
        conn3.close()
        if rows3[0][0] != pwd:
            return render_template('login.html', info='Mot de passe invalide')
        else:
            return render_template('home.html', name=name1, code=SECRET_MESSAGE)

@app.route('/ajout', methods=['POST', 'GET'])
def loginSuper():
    name1 = request.form['username']
    pwd = request.form['password']
    conn2 = sqlite3.connect('myDB.db')
    cur2 = conn2.cursor()
    cur2.execute("SELECT COUNT(pass) FROM superLog WHERE userName=?", (name1,))
    rows2 = cur2.fetchall()
    conn2.close()
    if rows2[0][0] == 0:
        return render_template('logSuperUser.html', info='Utilisateur inconnu')
    else:
        conn3 = sqlite3.connect('myDB.db')
        cur3 = conn3.cursor()
        cur3.execute("SELECT pass FROM superLog WHERE userName=?", (name1,))
        rows3 = cur3.fetchall()
        conn3.close()

        if rows3[0][0] != pwd:
            return render_template('logSuperUser.html', info='Mot de passe invalide')
        else:
            return render_template('addUser.html', name=name1, code=SECRET_MESSAGE)


@app.route('/addOk', methods=['POST', 'GET'])
def addSuper():
    print("laaaa")
    name1 = request.form['username']
    pwd = request.form['password']

    conn3 = sqlite3.connect('myDB.db')
    cur3 = conn3.cursor()
    cur3.execute("SELECT COUNT(pass) FROM log WHERE userName=?", (name1,))
    rows3 = cur3.fetchall()
    conn3.close()
    if rows3[0][0] != 0:
        return render_template('addUser.html', info="Un utilisateur a déjà le même nom d'utilisateur")
    else:
        conn2 = sqlite3.connect('myDB.db')
        cur2 = conn2.cursor()
        cur2.execute("insert into log (userName, pass) values (? , ?)", (name1,pwd))
        conn2.commit()
        conn2.close()
        return render_template("addUser.html", info='Ok')



if __name__ == "__main__":
    # HTTP version
    app.run(debug=True, host="0.0.0.0", port=8081)
    # HTTPS version
    # A compléter  : nécessité de déplacer les bons fichiers vers ce répertoire
     # app.run(debug=True, host="0.0.0.0", port=8081, ssl_context=(SERVER_PUBLIC_KEY_FILENAME, SERVER_PRIVATE_KEY_FILENAME))

