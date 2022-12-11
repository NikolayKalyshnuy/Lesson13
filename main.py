print('hello')
print('world')
input("Get number")

with open('outputs/1.txt', 'w'):
    pass

import requests
req = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=144aad8b326f4a8ede3b1521eeadd6ed"
requests.get(req)