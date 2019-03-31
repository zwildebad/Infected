from model import game_login, game_logout, is_winner
import unittest


class TestMain(unittest.TestCase):
    def testLogin(self):
        new_game = Game()
        self.assertTrue(game_login(new_game, "John", "password"))
        self.assertFalse(game_login(new_game, "Tod", "not password"))

    def testLogout(self):
        new_game = Game()
        new_guy = Player()
        self.assertFalse(game_logout(new_game, new_guy))

    def testDamage(self):
        new_game = Game()
        new_guy = Player()
        new_guy.username = "Al"
        self.assertTrue(new_game.add_player(new_guy))
        new_guy.got_hit(100)
        self.assertTrue(new_guy.dead)

    def testWinner(self):
        new_game = Game()
        new_guy1 = Player()
        new_guy2 = Player()
        is_winner(new_game)
        self.assertTrue(new_game.infected_win)
        new_game.infected_win = False
        new_game.add_player(new_guy1)
        new_game.add_player(new_guy2)
        self.assertFalse(is_winner(new_game))
