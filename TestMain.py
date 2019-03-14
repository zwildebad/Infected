import unittest
from backend.main import *
from backend.gameClasses import *
from backend.databaseProcess import *


class TestMain(unittest.TestCase):
    game = Game()

    def test_login(self):  # testing the login function in main
        self.assertTrue(game_login(self.game, "big_al", "123456"))
        self.assertEqual(self.game.get_players(), 1)

    def test_logout(self):  # testing the logout function in main
        self.assertTrue(game_logout(self.game, "big_al"))
        self.assertEqual(self.game.get_players(), 0)


if __name__ == '__main__':
    unittest.main()
