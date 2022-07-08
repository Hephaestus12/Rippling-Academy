class View():

    def __init__(self, game) -> None:
        self.game = game

    def welcome(self) -> None:
        print("Welcome to Hangman!")

    def prompt_guess(self) -> str:
        print()
        game_status = self.game.status
        spaced_string = ' '.join([game_status[i] for i in range(len(game_status))])
        print(spaced_string)
        guess = input(">>> Guess your letter:  ")
        return guess

    def display_incorrect(self) -> None:
        print("Incorrect!")
        print(f"You have {self.game.remaining_turns} attemps left.")

    def display_correct(self) -> None:
        print("Correct!")
        print(f"You have {self.game.remaining_turns} attemps left.")

    def display_won(self) -> None:
        print("You have won xD")

    def display_lost(self) -> None:
        print("You lose the game :(")

    def prompt_play_again(self) -> bool:
        print()
        while(True):
            play_again = input(">>> Do you want to play again? (y/n): ")
            if play_again.upper() == 'Y':
                return True
            if play_again.upper() == 'N':
                return False

    def inappropriate_guess(self, exception) -> None:
        print(exception)

    def goodbye(self) -> None:
        print()
        print("Exiting game")
        print("Have a nice day!")