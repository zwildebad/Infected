import unittest
from backend.main import *
from backend.gameClasses import *
from backend.databaseProcess import *


class TestMain(unittest.TestCase):
    game = Game()

    def test_login(self):  # testing the login function in main
        self.assertTrue(game_login(self.game))
        self.assertEqual(self.game.get_players(), 1)
        self.assertEqual(next_id(), 8)

    def test_logout(self):  # testing the logout function in main
        self.assertTrue(game_logout(self.game, "6"))
        self.assertEqual(self.game.get_players(), 0)
        self.assertFalse(game_logout(self.game, "6"))

    def test_winner(self):  # testing the winner function in main
        self.game.healthy_players = 0
        is_winner(self.game)
        self.assertTrue(self.game.infected_win)
        self.game.healthy_players = 24
        self.game.time = 0
        is_winner(self.game)
        self.assertTrue(self.game.players_win)


if __name__ == '__main__':
    unittest.main()
