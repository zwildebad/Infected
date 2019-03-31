import time
import math


class Player:  # this is the player class
    username = ""
    health = 100
    dead = False
    game_id = 0
    speed = 1
    x = 0
    y = 0

    def respawn(self):
        self.x = 0
        self.y = 0
        self.dead = False

    def is_dead(self):
        if self.health <= 0:
            self.dead = True

    def got_hit(self, damage):  # alter user object state after taking damage
        self.health -= damage
        self.is_dead()
        if self.dead:
            self.respawn()


class Game:  # this is a game class
    players = {}
    infected_players = 1
    healthy_players = len(players) - infected_players
    game_start = False
    infected_win = False
    players_win = False
    start_time = 0  # time when the game object was created in seconds since the ep
    current_time = 0  # current time in seconds since the epoch
    display_time = 0  # time to display in game
    lobby_timer = 1  # time to allow players to join, in seconds
    game_timer = 1  # time allotted to game, in seconds
    game_time = 300  # total time from lobby to end of game in seconds

    def stop_game(self):
        if self.infected_win:
            return
        else:
            return

    def start_game(self):
        self.game_start = True
        self.display_time = 0
        while self.current_time - self.start_time < self.game_timer:
            replacement = math.ceil(self.current_time - self.start_time) - self.lobby_timer
            if replacement != self.display_time:
                self.display_time = replacement
                self.game_time -= 1
            self.current_time = time.time()
        self.stop_game()

    def start_timer(self):
        while self.current_time - self.start_time < self.lobby_timer:
            if math.ceil(self.current_time - self.start_time) != self.display_time:
                self.display_time = math.ceil(self.current_time - self.start_time)
            self.current_time = time.time()
        self.start_game()

    def add_player(self, player_model):
        if player_model.username not in self.players:
            self.players[player_model.username] = [player_model.x, player_model.y]
            return True
        else:
            return False

    def remove_player(self, player_model):
        if self.players[player_model.username]:
            del self.players[player_model.username]
            return True
        else:
            return False

    def __init__(self):
        self.current_time = time.time()
        self.start_time = time.time()
        self.start_timer()

