from random import choice

class WordFactory:

    def __init__(self, filepath = 'hangman/data/words.txt'):
        with open(filepath, encoding="utf-8") as f:
            lines = f.readlines()
        self.words = [str.strip() for str in lines]

    def get_random(self):
        return choice(self.words)
