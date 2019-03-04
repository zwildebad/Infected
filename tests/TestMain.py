import unittest
from backend.main import *
from backend.gameClasses import *


class TestMain(unittest.TestCase):
    def test_login(self):  # testing the login function in main
        game = Game()  # new game instance
        self.assertTrue(game_login(game))
        self.assertEqual(game.player_count, 1)
        self.assertFalse(game_login(game))

    def test_logout(self):  # testing the logout function in main
        game = Game()
        game.players["user0"] = User()
        self.assertTrue(game_logout(game, "user0"))
        self.assertEqual(game.player_count, 0)
        self.assertFalse(game_logout(game, "user0"))

    def test_winner(self):  # testing the winner function in main
        game = Game()
        game.healthy_players = 0
        is_winner(game)
        self.assertTrue(game.infected_win)
        game.healthy_players = 24
        game.time = 0
        is_winner(game)
        self.assertTrue(game.players_win)


if __name__ == '__main__':
    unittest.main()
