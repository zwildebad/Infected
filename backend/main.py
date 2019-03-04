# should these be methods?? The world may never know....
# time limit for players to join before game starts
from backend.databaseProcess import *
from backend.gameClasses import *


def game_login(game):  # logs player into game with id from database, adds player to player list
    if game.player_count >= 50:
        return False
    elif game.player_count < 50 and not game.game_start:
        player_dict = game.players
        new_user_name = "user" + str(next_id())
        new_user_object = User()
        new_user_object.game_id = game.game_id
        player_dict[new_user_name] = new_user_object
        return True
        # connect to server


def game_logout(game, player_id):  # deletes player from game list
    if game.player_count == 0:
        return False
    else:
        del game.players[player_id]
        return True
        # disconnect from server


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
