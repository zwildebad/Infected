import threading


class User:  # this is the healthy player class
    username = ""
    health = 100
    dead = False  # if user object has dead = True, create a new object of class infected for that user
    speed = 1
    game_id = 0

    def is_infected(self):  # if user object was damaged, they are infected
        if self.health <= 0:
            self.dead = True

    def got_hit(self):  # alter user object state after taking damage
        self.health -= 100
        User.is_infected(self)


class Infected:  # this is the infected player class
    username = ""
    health = 100
    speed = 1.2
    dead = False  # if infected object has dead = true, player must respawn
    game_id = 0

    def is_dead(self):  # same as is_infected, except already infected so must respawn instead
        if self.health <= 0:
            self.dead = True

    def got_hit(self):
        self.health -= 25
        self.is_dead()


class Game:  # this is a game class
    players = {}
    player_count = len(players)
    infected_players = 1
    healthy_players = len(players) - infected_players
    game_over = False  # true when winner is established
    infected_win = False
    players_win = False
    game_start = False
    time = 180  # length of game/match
    allow_join = 120  # time before game starts after first player joins
    game_id = 0

    def start_game(self):
        self.game_start = True

    def start_timer(self):
        self.allow_join -= 1

    def game_timer(self):
        self.time -= 1

