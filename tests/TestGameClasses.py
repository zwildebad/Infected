import unittest
from backend import gameClasses


class TestUserClass(unittest.TestCase):
    def test_infected(self):
        big_zomb = gameClasses.Infected()
        self.assertTrue(big_zomb.damage, 100)
        self.assertFalse(big_zomb.dead)
        for num in range(0, 5):
            big_zomb.got_hit()
        self.assertTrue(big_zomb.dead)

    def test_user(self):
        big_al = gameClasses.User()
        self.assertTrue(big_al.health, 100)
        self.assertFalse(big_al.infected)
        self.assertEqual(big_al.damage, 25)
        big_al.got_hit()
        self.assertTrue(big_al.infected)


if __name__ == '__main__':
    unittest.main()
