import requests
import server
import unittest


class TestServer(unittest.TestCase):
    def test_main_menu(self):
        r = requests.get('http://127.0.0.1:5000/')
        self.assertEqual(r.status_code, 200)

    def test_login(self):
        r = requests.get('http://127.0.0.1:5000/login')
        self.assertEqual(r.status_code, 200)

    def test_logout(self):
        r = requests.get('http://127.0.0.1:5000/logout')
        self.assertEqual(r.status_code, 200)

    def test_settings(self):
        r = requests.get('http://127.0.0.1:5000/settings')
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()