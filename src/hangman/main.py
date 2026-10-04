"""!
@file main.py
@brief Command-line interface for Hangman.
"""

import os
import sys

from hangman.constants import (
    ANSI_BOLD,
    ANSI_RED,
    ANSI_RESET,
    MSG_LOSE,
    MSG_WIN,
    STAGES,
    TITLE_ART,
)
from hangman.game import Game, choose_word


def say(message: str = "") -> None:
    """!
    @brief Show a message to the player; all output goes through here.
    @param message The text to show.
    """
    print(message)


def _colorize(text: str, *codes: str) -> str:
    """!
    @brief Wrap text in ANSI color codes when the output supports colors.
    @details Colors are skipped when stdout is not a terminal or NO_COLOR is set.
    @param text Text to colorize.
    @param codes ANSI escape codes to apply.
    @return The (possibly) colorized text.
    """
    if not sys.stdout.isatty() or "NO_COLOR" in os.environ:
        return text
    return "".join(codes) + text + ANSI_RESET


def show_title() -> None:
    """!
    @brief Show the colored ASCII-art title.
    """
    if sys.stdout.isatty():
        os.system("")  # Enables ANSI escape sequences in Windows terminals.
    say(_colorize(TITLE_ART, ANSI_BOLD, ANSI_RED))


def show(game: Game) -> None:
    """!
    @brief Show the gallows for the lives left and the word with blanks.
    @param game The game to show.
    """
    say(STAGES[max(game.lives, 0)])
    say(game.display())


def play(game: Game) -> None:
    """!
    @brief Ask for letters until the word is guessed or the lives run out.
    @param game The game to play.
    """
    while not game.over:
        show(game)
        raw = input("Guess a letter: ").strip()
        try:
            result = game.guess(raw)
        except ValueError:
            say("Please enter a single letter.")
            continue
        letter = raw.lower()
        if result is None:
            say(f"You already guessed '{letter}'.")
        elif result:
            say(f"'{letter}' is in the word.")
        else:
            say(f"'{letter}' is not in the word. You lose a life.")
    show(game)
    say(MSG_WIN if game.won else MSG_LOSE + game.word)


def main() -> None:
    """!
    @brief Entry point: start a game with a random word.
    """
    show_title()
    play(Game(choose_word()))


if __name__ == "__main__":
    main()
