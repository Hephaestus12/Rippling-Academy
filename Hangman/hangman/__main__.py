"""
Entry point for ``hangman`` command.
"""
from game import Game
from model import Hangman


if __name__ == '__main__':
    new_game = Game(Hangman())
    new_game.run()