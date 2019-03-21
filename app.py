from flask import Flask, send_from_directory
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from backend.main import *
from backend.gameClasses import Game
app = Flask('__Infected__')


@app.route("/")
def main_menu():
    return render_template('index.html')


@app.route("/logout", methods=['POST'])
def logout():
    # TODO: Fix this shit
    return


@app.route("/login", methods=['POST'])
def login():
    new_game = Game()
    username = request.form['username']
    password = request.form['password']
    brand_new = request.form['new_user'].lower()
    if brand_new == 'yes':
        if not check_login(username, password):
            add_to_database(username, password)
        else:
            return render_template('index.html')
    # ABOVE THIS LINE ^^^ IS GOOD
    # TODO below: Find a way to make game lobbies
    if game_login(new_game, username, password):
        return redirect(url_for('game'))  # sends them to game
    else:
        return render_template('index.html')


@app.route("/game")
def game():
    return render_template('game.html')


@app.route('/templates/assets/backgrounds/background1')
def b1():
    return send_from_directory('templates', 'assets/backgrounds/background1.png')


@app.route('/templates/assets/sprites/human')
def h():
    return send_from_directory('templates', 'assets/sprites/human.png')


@app.route('/templates/assets/sprites/zombie')
def z():
    return send_from_directory('templates', 'assets/sprites/zombie.png')


@app.route('/templates/assets/ui/ExitButton')
def e():
    return send_from_directory('templates', 'assets/ui/ExitButton.png')
