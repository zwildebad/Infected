import unittest
from backend.databaseProcess import number_of_players, add_to_database


class TestDatabase(unittest.TestCase):
    def test_number_of_players(self):  # tests the number of players as well as the add to database function
        number = number_of_players()
        self.assertEqual(number, 3)
        add_to_database()
        number = number_of_players()
        self.assertEqual(number, 4)


if __name__ == '__main__':
    unittest.main()
