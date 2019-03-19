# Testing requests

from requests import put, get

put('http://localhost:5000/todo1', data={'data': 'Remember the milk'}).json()
get('http://localhost:5000/todo1').json()

put('http://localhost:5000/todo2', data={'data': 'Change my brakepads'}).json()
get('http://localhost:5000/todo2').json()
