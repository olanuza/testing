# -*- coding: utf-8 -*-
"""Mastermind Verse Test - Server"""

__author__ = 'Oriol Lanuza Fisas'
__email__ = 'oriol@lanuza.eu'
__copyright__ = 'Copyright © 2019, Oriol Lanuza Fisas'
__license__ = 'MIT'

from flask import Flask, request, jsonify

app = Flask(__name__)

class Game:
    def __init__(self, code):   # init a game
        self.code = code
        self.turn = {}

    def check_guess(self, guess):
        black = 0
        white = 0
        checking_code = self.code
        checking_guess = guess
        for i in range(len(guess)):     # Check black
            if checking_guess[i]==checking_code[i]:
                black += 1
                checking_code[i] = "X"  # Already checked as black
                checking_guess[i] = "Y"
        for i in range(len(guess)):     # Check white
            if checking_guess[i] in checking_code:
                white += 1
                checking_code[checking_code.index(checking_guess[i])] = "X"
                checking_guess[i] = "Y"
        return [black, white]
    
    def guess(self, guess):     # add guess & response to turns historic, return result
        self.turn[str(guess)] = self.check_guess(guess)
        return self.turn[str(guess)]

    def __print__(self):
        print(self.turn)

@app.route('/newgame/<string:code>', methods=['POST'])
def new_game(code):
    x = Game(code)
    print(x)
    # check if code is valid (len, colors)
    return 0

@app.route('/game/<string:id>/<string:guess>', methods=['POST'])   # we use post instead of get (we store info to db)
def guess(guess):
    return x.guess(guess)

@app.route('/game/<string:id>', methods=['GET'])
def historic(id):
    # check if game exists and return historic of turn + guess + result
    return 0

x = Game(["Blue","Red","Blue","Green"])
print(x.code)
x.guess(["Blue","Blue","Red","Red"])
x.guess(["Blue","Blue","Red","Yellow"])
x.guess(["Blue","Blue","Red","Green"])
print(x.turn)


if __name__ == '__main__':
    app.run(debug=True)