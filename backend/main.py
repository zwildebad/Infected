# should these be methods?? The world may never know....
# time limit for players to join before game starts
from backend.databaseProcess import *
from backend.gameClasses import *


def game_login(game):  # logs player into game with id from database, adds player to player list
    if game.get_players() >= 50:
        return False
    elif game.get_players() < 50 and not game.game_start:  # TODO add user to database upon calling function
        new_user_name = str(next_id())  # name of new user, which is just the next available id number
        new_user_object = User()  # new User object for the new user
        add_to_database()
        game.add_player(new_user_name, new_user_object)
        return True
        # connect to server?


def game_logout(game, player_id):  # deletes player from game list
    if game.get_players() == 0:
        return False
    else:
        game.remove_player(player_id)  # delete player from games player dictionary
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
