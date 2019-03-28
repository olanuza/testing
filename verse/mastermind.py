# -*- coding: utf-8 -*-
"""Mastermind Verse Test"""

__author__ = 'Oriol Lanuza Fisas'
__email__ = 'oriol@lanuza.eu'
__copyright__ = 'Copyright © 2019, Oriol Lanuza Fisas'
__license__ = 'MIT'

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/game/<string:id>/<string:code>', methods=['POST'])
def new_game(id, code):
    # if id exists, return error
    # check if code is valid (len, colors)
    # add new active game to DB (id, code, active)
    return 0

@app.route('/game/<string:id>/<string:guess>', methods=['POST'])   # we use post instead of get (we store info to db)
def guess(id, guess):
    # if id exists, check active, if not, game does not exist
    # if is active, make guess (create new turn + result with id game) and return result
    return 0

@app.route('/game/<string:id>', methods=['GET'])
def historic(id):
    # check if game exists and return historic of turn + guess + result
    return 0
if __name__ == '__main__':
    app.run(debug=True)