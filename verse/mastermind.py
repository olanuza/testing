# -*- coding: utf-8 -*-
"""Mastermind Verse Test - Server"""

__author__ = 'Oriol Lanuza Fisas'
__email__ = 'oriol@lanuza.eu'
__copyright__ = 'Copyright © 2019, Oriol Lanuza Fisas'
__license__ = 'MIT'

class Game:
    def __init__(self, code):   # init a game
        self.code = code
        self.turn = {}

    def check_guess(self, guess):
        black = 0
        white = 0
        checking_code = list(self.code)     # Value, not pointer
        checking_guess = list(guess)
        for i in range(len(guess)):     # Check black
            if checking_guess[i]==checking_code[i]:
                black += 1
                checking_code[i] = "."  # Already checked as black
                checking_guess[i] = ","
        for i in range(len(guess)):     # Check white
            if checking_guess[i] in checking_code:
                white += 1
                checking_code[checking_code.index(checking_guess[i])] = "."
                checking_guess[i] = ","
        return [black, white]
    
    def guess(self, guess):     # add guess & response to turns historic, return result
        g = "".join(guess)
        self.turn[g] = self.check_guess(guess)
        return {g:str(self.turn[g])}