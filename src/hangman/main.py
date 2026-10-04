"""!
@file main.py
@brief Command-line interface for Hangman.
"""

from hangman.constants import MSG_WIN
from hangman.game import Game, choose_word


def say(message: str = "") -> None:
    """!
    @brief Show a message to the player; all output goes through here.
    @param message The text to show.
    """
    print(message)


def play(game: Game) -> None:
    """!
    @brief Ask for letters until every blank is filled.
    @param game The game to play.
    """
    say(game.display())
    while not game.won:
        letter = input("Guess a letter: ").strip()
        if game.guess(letter):
            say(f"Right, '{letter.lower()}' is in the word.")
        else:
            say(f"Wrong, '{letter.lower()}' is not in the word.")
        say(game.display())
    say(MSG_WIN)


def main() -> None:
    """!
    @brief Entry point: start a game with a random word.
    """
    play(Game(choose_word()))


if __name__ == "__main__":
    main()
