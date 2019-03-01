import unittest
import requests
from server.infected_mmo import views


class TestGameInstance(unittest.TestCase):
    def less_than_50(self):
        requests.get('http://127.0.0.1:8000/login')
        self.assertEqual(len(views.game_list), 1)
        for i in range(0, 48):
            requests.get('http://127.0.0.1:8000/login')
        self.assertEqual(len(views.game_list), 1)


if __name__ == '__main__':
    unittest.main()
