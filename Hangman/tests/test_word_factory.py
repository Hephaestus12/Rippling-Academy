
import pytest
from hangman.word_factory import WordFactory

def test_get_random():
    factory = WordFactory('hangman/data/words.txt')
    word = factory.get_random()
    assert word.isalpha()
