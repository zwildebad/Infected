import requests

# for i in range(0, 100):
#     payload = {"username": str(i), "new_user": "", "password": str(i)}

r = requests.post('http://127.0.0.1:5000/login', data={"username": "1", "new_user": "", "password": str(1)})
