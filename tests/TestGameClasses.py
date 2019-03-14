import unittest
from backend import gameClasses


class TestUserClass(unittest.TestCase):
    def test_infected(self):  # testing zombie death and health
        big_zomb = gameClasses.Infected()
        self.assertFalse(big_zomb.dead)
        for num in range(0, 5):
            big_zomb.got_hit()
        self.assertTrue(big_zomb.dead)

    def test_user(self):  # testing user death and health
        big_al = gameClasses.User()
        self.assertTrue(big_al.health, 100)
        self.assertFalse(big_al.dead)
        big_al.got_hit()
        self.assertTrue(big_al.dead)

    def test_game(self):  # testing the game class prior to anything being done
        big_game = gameClasses.Game()
        self.assertEqual(big_game.get_players(), 0)
        self.assertEqual(big_game.infected_players, 1)
        self.assertFalse(big_game.game_over)


if __name__ == '__main__':
    unittest.main()
