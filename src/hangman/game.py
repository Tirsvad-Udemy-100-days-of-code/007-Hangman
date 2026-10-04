"""!
@file game.py
@brief Game logic for Hangman, kept free of input/output so it can be tested.
"""

import random

from hangman.constants import WORD_LIST


def choose_word(words: list[str] | None = None) -> str:
    """!
    @brief Pick a random word.
    @param words Candidate words; defaults to the built-in word list.
    @return The chosen word in lower case.
    """
    return random.choice(words if words is not None else WORD_LIST).lower()


def is_in_word(word: str, letter: str) -> bool:
    """!
    @brief Check whether a guessed letter occurs in the word.
    @param word The secret word.
    @param letter The guessed letter (case-insensitive).
    @return True if @p letter is in @p word.
    """
    return letter.lower() in word.lower()
