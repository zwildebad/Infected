# should these be methods?? The world may never know....
# time limit for players to join before game starts


def game_login(game):
    if game.player_count >= 50:
        return False
    elif game.player_count < 50 and not game.game_start:
        game.player_count += 1
        return True
        # connect to server


def game_logout(game):
    if game.player_count == 0:
        return False
    else:
        game.player_count -= 1
        return True
        # disconnect from server


def is_winner(game):
    if game.healthy_players == 0:
        game.infected_win = True
    elif game.healthy_players != 0 and game.time == 0:
        game.players_win = True
#
# def do_damage(player):
#     player.got_hit()
#     if player.dead:
#         # convert to infected OR if already infected respawn.
