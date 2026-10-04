"""!
@file main.py
@brief Command-line interface for Hangman.
"""

from hangman.game import Game, choose_word


def say(message: str = "") -> None:
    """!
    @brief Show a message to the player; all output goes through here.
    @param message The text to show.
    """
    print(message)


def main() -> None:
    """!
    @brief Entry point: show the blanks, take one guess and show the result.
    """
    game = Game(choose_word())
    say(game.display())
    letter = input("Guess a letter: ").strip()
    if game.guess(letter):
        say(f"Right, '{letter.lower()}' is in the word.")
    else:
        say(f"Wrong, '{letter.lower()}' is not in the word.")
    say(game.display())


if __name__ == "__main__":
    main()
