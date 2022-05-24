# -*- coding: utf-8 -*-
"""

Created on May 2022
@author: Mr ABBAS-TURKI

"""
import pem
from flask import Flask, render_template, request
from build import SERVER_PUBLIC_KEY_FILENAME, SERVER_PRIVATE_KEY_FILENAME

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


database = {'jean': 'pierre', 'christophe': 'voyage', 'dider': 'paul'}


@app.route('/motDePasse', methods=['POST', 'GET'])
def login():
    name1 = request.form['username']
    pwd = request.form['password']
    if name1 not in database:
        return render_template('login.html', info='Utilisateur inconnu')
    else:
        if database[name1] != pwd:
            return render_template('login.html', info='Mot de passe invalide')
        else:
            return render_template('home.html', name=name1, code=SECRET_MESSAGE)


if __name__ == "__main__":
    # HTTP version
    # app.run(debug=True, host="0.0.0.0", port=8081)
    # HTTPS version
    # A compléter  : nécessité de déplacer les bons fichiers vers ce répertoire
      app.run(debug=True, host="0.0.0.0", port=8081, ssl_context=(SERVER_PUBLIC_KEY_FILENAME, SERVER_PRIVATE_KEY_FILENAME))
