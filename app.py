from flask import Flask
from flask import render_template
from flask import request
from backend.gameClasses import *
from backend.main import *
import json
app = Flask('__Infected__')

games = {}  # {game_id: game_object}


@app.route("/")
def main_menu():
    return render_template('index.html')


@app.route("/logout", methods=['POST'])
def logout():
    game_id = request.form['game_id']
    game = games[game_id]
    username = request.form['username']
    game_logout(game, username)
    return render_template('index.html')


@app.route("/login", methods=['POST'])
def login():
    print(games)
    username = request.form['username']
    password = request.form['password']
    brand_new = request.form['new_user'].lower()
    if brand_new == 'yes':
        if not check_login(username, password):
            add_to_database(username, password)
        else:
            return render_template('index.html')
    if len(games) != 0:
        for i in range(1, next_id(games)):
            game = games[i]
            if game_login(game, username, password):
                return render_template('game.html')
            else:
                return render_template('index.html')
    else:
        new_game = Game()
        new_game.id = str(next_id(games))
        if game_login(new_game, username, password):
            games[new_game.id] = new_game
            return render_template('game.html')
        else:
            print("Those credentials are incorrect!")
            return render_template('index.html')

