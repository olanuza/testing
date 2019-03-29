# -*- coding: utf-8 -*-
"""Mastermind Verse Test - Server"""

__author__ = 'Oriol Lanuza Fisas'
__email__ = 'oriol@lanuza.eu'
__copyright__ = 'Copyright © 2019, Oriol Lanuza Fisas'
__license__ = 'MIT'

from flask import Flask, request, jsonify
from mastermind import *
import requests, json

app = Flask(__name__)
game = Game([])

@app.route('/api/newgame', methods=['POST'])
def new_game():
    content = request.json
    code = list(content["code"])        # get the code from json!
    game.code = code    #print(code)
    game.turn = {}
    print(game.code)
    return jsonify({"game":"New game! Start guessing now!"}), 200

@app.route('/api/guess', methods=['PUT'])   # we use post instead of get (we store info to db)
def guess():
    content = request.json
    guess = list(content["guess"])        # get the guess from json!
    #print(guess)
    result = game.guess(guess)
    return jsonify(result), 200

@app.route('/api/turns', methods=['GET'])
def historic():
    return jsonify(game.turn), 200

if __name__ == '__main__':
    app.run(debug=True)