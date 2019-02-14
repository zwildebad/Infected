class User:  # this is the healthy player class
    health = 100
    infected = False
    speed = 1

    def is_infected(self):
        if self.health <= 0:
            self.infected = True

    def got_hit(self):
        self.health -= 100
        User.is_infected(self)


class Infected:  # this is the infected player class
    health = 100
    speed = 1.2
    dead = False

    def is_dead(self):
        if self.health <= 0:
            self.dead = True

    def got_hit(self):
        self.health -= 25
        self.is_dead()


class Game:  # this is a game class
    player_count = 0
    infected_players = 1
    healthy_players = player_count - 1

    def login(self):
        if player_count == 50:
            print("Please wait for someone to rage quit.")
        else:
            self.player_count += 1

    def logout(self):
        self.player_count -= 1
