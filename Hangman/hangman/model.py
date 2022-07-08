import re
from hangman.exceptions import GameLost, GameWon
from hangman.word_factory import WordFactory


class Hangman(object):

    MAX_TURNS = 6
    answer_rules = re.compile('^[A-Z]{1,50}$')
    guess_rules = re.compile('^[A-Z]$')

    def __init__(self, answer=None) -> None:

        self.factory = WordFactory()

        if not answer:
            # Populate answer
            answer = self.factory.get_random()

        # Validate answer.
        if not self.is_valid_answer(answer):
            raise ValueError("Word must be letters A-Z")

        self.answer = answer.upper()
        self._wrong_guesses = set()
        self._correct_guesses = set()

    def guess(self, letter:str) -> bool:

        # validate input
        if not self.is_valid_guess(letter):
            raise ValueError('Error: Your guess must be a letter A-Z')

        # add to correct_guesses or wrong_guesses
        is_miss = letter.upper() not in self.answer
        if is_miss:
            self._add_wrong_guess(letter)
            return False
        else:
            self._add_correct_guess(letter)
            return True


    @property
    def wrong_guesses(self):
        return sorted(list(self._wrong_guesses))

    @wrong_guesses.setter
    def wrong_guesses(self, letters):
        for letter in letters:
            self._add_wrong_guess(letter)

    @property
    def correct_guesses(self):
        return sorted(list(self._correct_guesses))

    @correct_guesses.setter
    def correct_guesses(self, letters):
        for letter in letters:
            self._add_correct_guess(letter)

    @property
    def remaining_turns(self):
        return self.MAX_TURNS - len(self.wrong_guesses)

    @property
    def status(self):

        correct_guesses = self.correct_guesses

        def fill_in(letter:str) -> str:

            return letter if letter in correct_guesses else '_'

        return ''.join(fill_in(letter) for letter in self.answer)

    def _add_wrong_guess(self, value:str) -> None:

        self._wrong_guesses.add(value.upper())
        if self.remaining_turns <= 0:
            raise GameLost

    def _add_correct_guess(self, value:str) -> None:

        self._correct_guesses.add(value.upper())
        if self._correct_guesses == set(self.answer):
            raise GameWon

    def is_valid_answer(self, word:str) -> bool:

        word = str(word).upper()
        return self.answer_rules.search(word)

    def is_valid_guess(self, letter:str) -> bool:

        letter = str(letter).upper()
        return self.guess_rules.search(letter)
