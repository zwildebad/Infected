from flask import Flask
from flask import render_template
from backend.gameClasses import *
from backend.main import *
app = Flask('__Infected__')

games = []


@app.route("/")
def main_menu():
    return render_template('index.html')


@app.route("/logout")
def logout():
    # game_id = user.game_id
    # game = games[game_id]
    # game_logout(game, user)
    return render_template('index.html')


@app.route("/login")
def login():
    if len(games) != 0:
        for i in range(0, len(games)):
            game = games[i]
            if game_login(game):
                return render_template('game.html')
    else:
        new_game = Game()
        game_login(new_game)
        games.append(new_game)
        new_game.game_id = games.index(new_game)  # sets game id to place in list
    return render_template('game.html')


@app.route("/settings")
def settings():
    return render_template('settings.html')

