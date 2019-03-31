from model.python.databaseProcess import *
from model.python.gameClasses import *


def game_login(game, username, password):  # logs player into game if room and if credentials match
    if len(game.players) >= 50:
        # TODO make a new game instance
        return False
    elif len(game.players) < 50 and not game.game_start:
        successful = check_login(username, password)
        if successful:
            new_guy = Player()
            game.add_player(new_guy)
            return True
        else:
            print("Those credentials are incorrect(game_login)!")
            return False


def game_logout(game, player_model):  # deletes player from game list
    game.remove_player(player_model)


def is_winner(game):
    if game.healthy_players <= 0:
        game.infected_win = True
    elif game.healthy_players != 0 and game.game_time == 0:
        player_dict = game.players
        game.players_win = True
        return game.players.keys
    else:
        return False
