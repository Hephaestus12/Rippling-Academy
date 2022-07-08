
import pytest
from hangman.model import Hangman, GameWon, GameLost
from settings.config import MAX_ATTEMPTS

@pytest.fixture
def sample_game():
    return Hangman(answer='rippling')

def test_game_instance_with_answer(sample_game):
    assert sample_game.answer == 'RIPPLING'


def test_game_instance_with_wrong_guesses(sample_game):
    assert sample_game.wrong_guesses == []


def test_game_instance_with_remaining_turns(sample_game):
    assert sample_game.remaining_turns == MAX_ATTEMPTS


def test_game_instance_with_status(sample_game):
    assert sample_game.status == '________'


def test_answer_validation_rules():
    with pytest.raises(ValueError):
        Hangman('1234567')

    with pytest.raises(ValueError):
        Hangman('rippling12')

    with pytest.raises(ValueError):
        Hangman(1232145678995462313)

    with pytest.raises(ValueError):
        Hangman('a' * 100)

    with pytest.raises(ValueError):
        Hangman('tej_sukhatme')


def test_wrong_guess_removes_1_turn(sample_game):
    sample_game.guess('e')
    assert sample_game.remaining_turns == MAX_ATTEMPTS-1


def test_wrong_guess_updates_wrong_guesses(sample_game):
    sample_game.guess('e')
    assert sample_game.wrong_guesses == ['E']

def test_wrong_guess_no_change_status(sample_game):
    expected = sample_game.status
    sample_game.guess('e')
    assert sample_game.status == expected == '________'


def test_guess_must_be_a_single_letter_number(sample_game):
    with pytest.raises(ValueError):
        sample_game.guess(1)

    with pytest.raises(ValueError):
        sample_game.guess('EE')

    with pytest.raises(ValueError):
        sample_game.guess('')


def test_wrong_guess_duplicate_is_ignored(sample_game):
    sample_game.guess('e')
    sample_game.guess('e')
    assert sample_game.remaining_turns == MAX_ATTEMPTS-1


def test_correct_guess_updates_status(sample_game):
    sample_game.guess('i')
    assert sample_game.status == '_I___I__'

    sample_game.guess('r')
    assert sample_game.status == 'RI___I__'


def test_corect_guess_leaves_remaining_turns_and_wrong_guesses_untouched(sample_game):
    expected_wrong_guesses = sample_game.wrong_guesses
    expected_remaining_turns = sample_game.remaining_turns

    sample_game.guess('r')

    assert expected_wrong_guesses == sample_game.wrong_guesses
    assert expected_remaining_turns == sample_game.remaining_turns


def test_game_winning_guess(sample_game):
    sample_game.guess('r')
    sample_game.guess('i')
    sample_game.guess('p')
    sample_game.guess('l')
    sample_game.guess('n')

    with pytest.raises(GameWon):
        sample_game.guess('g')

    assert sample_game.status == 'RIPPLING'


def test_game_losing_guess(sample_game):
    sample_game.guess('b')
    sample_game.guess('c')
    sample_game.guess('d')
    sample_game.guess('e')
    sample_game.guess('f')

    with pytest.raises(GameLost):
        sample_game.guess('o')
    assert sample_game.status == '________'
    assert sample_game.remaining_turns == 0
