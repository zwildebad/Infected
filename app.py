from flask import Flask
from flask import render_template
from backend.gameClasses import Game, User, Infected
from backend.main import game_login, game_logout, is_winner
app = Flask('__Infected__')

games = []


@app.route("/")
@app.route("/logout")
def main_menu():
    return render_template('index.html')


@app.route("/login")
def login():
    if len(games) != 0:
        for i in range(0, len(games)):
            game = games[i]
            if game_login(game):
                # create new player, add to database, username and password??
                # USE FILES FROM BACKEND :D
                return render_template('game.html')
    else:
        new_game = Game()
        game_login(new_game)
        games.append(new_game)
    return render_template('game.html')


@app.route("/settings")
def settings():
    return render_template('settings.html')
