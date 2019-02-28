import unittest
from backend import main
from backend import gameClasses


class TestMain(unittest.TestCase):
    def test_login(self):  # testing the login function in main
        game = gameClasses.Game()  # new game instance
        game.player_count = 49
        self.assertTrue(main.login(game))
        self.assertEqual(game.player_count, 50)
        self.assertFalse(main.login(game))

    def test_logout(self):  # testing the logout function in main
        game = gameClasses.Game()
        game.player_count = 1
        self.assertTrue(main.logout(game))
        self.assertEqual(game.player_count, 0)
        self.assertFalse(main.logout(game))

    def test_winner(self):  # testing the winner function in main
        game = gameClasses.Game()
        game.healthy_players = 0
        main.is_winner(game)
        self.assertTrue(game.infected_win)
        game.healthy_players = 24
        game.time = 0
        main.is_winner(game)
        self.assertTrue(game.players_win)


if __name__ == '__main__':
    unittest.main()
