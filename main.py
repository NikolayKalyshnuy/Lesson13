print('hello')
print('world')

with open('outputs/1.txt', 'w'):
    pass

import requests

lat = 44.34
lon = 10.99
api_key = ''
with open('keys.txt', 'r') as file:
    api_key = file.readline()
req = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
resp = requests.get(req)
print(api_key)
print(resp.text)