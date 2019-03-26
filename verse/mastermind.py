# Mastermind Verse Test

from flask import Flask, request

app = Flask(__name__)

@app.route('/newgame/<string:id>/<string:code>')
def new_game(id, code):
    # if id exists, return error
    # check if code is valid (len, colors)
    # add new game to DB (id, code)

@app.route('/guess/<string:id>/<string:guess>')
def guess(id, guess):
    

if __name__ == '__main__':
    app.run(debug=True)