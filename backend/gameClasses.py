class User:  # this is the healthy player class
    username = ""
    health = 100
    dead = False  # if user object has dead = True, create a new object of class infected for that user
    speed = 1

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

    def is_dead(self):  # same as is_infected, except already infected so must respawn instead
        if self.health <= 0:
            self.dead = True

    def got_hit(self):
        self.health -= 25
        self.is_dead()


class Game:  # this is a game class
    player_count = 0  # number players in the game overall
    infected_players = 1
    healthy_players = player_count - 1
    game_over = False  # true when winner is established
    infected_win = False
    players_win = False
    time = 180  # length of game/match
    allow_join = 120  # time before game starts after first player joins
