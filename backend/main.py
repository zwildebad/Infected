from backend.databaseProcess import *
from backend.gameClasses import *


def game_login(game, username, password):  # logs player into game if room and if credentials match
    if len(game.players) >= 50:
        # TODO make a new game instance
        return False
    elif len(game.players) < 50 and not game.game_start:
        successful = check_login(username, password)
        if successful:
            game.add_player(username, User())
            return True
        else:
            print("Those credentials are incorrect(game_login)!")
            return False


def game_logout(game, username):  # deletes player from game list
    game.remove_player(username)
    # TODO ??


def is_winner(game):
    if game.healthy_players == 0:
        game.infected_win = True
    elif game.healthy_players != 0 and game.time == 0:
        player_dict = game.players
        game.players_win = True
        winners = []
        for player in player_dict:
            winners.append(player)
        return winners


def next_id(dict):
    return len(dict) + 1
