from hangman.exceptions import GameLost, GameWon
from hangman.view import View
from hangman.model import Hangman

class Game:

    def __init__(self, game=Hangman()) -> None:
        self.game = game
        self.view = View(self.game)
        self.view.welcome()


    def game_loop(self) -> None:

        while True:
            try:
                letter = self.view.prompt_guess()
                guess_is_correct = self.game.guess(letter)
    
                if guess_is_correct :
                    self.view.display_correct()
                else:
                    self.view.display_incorrect()

            except GameLost:
                self.view.display_lost()
                break
            except GameWon:
                self.view.display_won()
                break
            except ValueError as e:
                self.view.inappropriate_guess(e)


    def run(self) -> None:

        while True:
            try:
                self.game_loop()
            except KeyboardInterrupt:  # exit immediately
                break

            if not self.view.prompt_play_again():
                break

            # setup next game
            self.game = Hangman()
            self.view = View(self.game)

        self.view.goodbye()
