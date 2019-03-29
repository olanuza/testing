# -*- coding: utf-8 -*-
"""Mastermind Verse Test - Testing requests"""

__author__ = 'Oriol Lanuza Fisas'
__email__ = 'oriol@lanuza.eu'
__copyright__ = 'Copyright © 2019, Oriol Lanuza Fisas'
__license__ = 'MIT'


import requests

r = requests.post('http://127.0.0.1:5000/api/newgame', json={"code": "BRBG"})
print("STARTED")
if r.ok:
    print(r.json())
else:
    print("ERR?")

r = requests.put('http://127.0.0.1:5000/api/guess', json={"guess": "BRTG"})
print("GUESS1")
if r.ok:
    print(r.json())
else:
    print("ERR?")

r = requests.put('http://127.0.0.1:5000/api/guess', json={"guess": "GRRG"})
print("GUESS2")
if r.ok:
    print(r.json())
else:
    print("ERR?")
r = requests.get('http://127.0.0.1:5000/api/turns')
print("TURNS")
if r.ok:
    print(r.json())
else:
    print("ERR?")