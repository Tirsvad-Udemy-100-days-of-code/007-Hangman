"""!
@file main.py
@brief Command-line interface for Hangman.
"""

from hangman.constants import MSG_LOSE, MSG_WIN
from hangman.game import Game, choose_word


def say(message: str = "") -> None:
    """!
    @brief Show a message to the player; all output goes through here.
    @param message The text to show.
    """
    print(message)


def play(game: Game) -> None:
    """!
    @brief Ask for letters until the word is guessed or the lives run out.
    @param game The game to play.
    """
    say(game.display())
    while not game.over:
        letter = input("Guess a letter: ").strip()
        if game.guess(letter):
            say(f"Right, '{letter.lower()}' is in the word.")
        else:
            say(f"Wrong, '{letter.lower()}' is not in the word. Lives left: {game.lives}")
        say(game.display())
    say(MSG_WIN if game.won else MSG_LOSE + game.word)


def main() -> None:
    """!
    @brief Entry point: start a game with a random word.
    """
    play(Game(choose_word()))


if __name__ == "__main__":
    main()
