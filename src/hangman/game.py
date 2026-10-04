"""!
@file game.py
@brief Game logic for Hangman, kept free of input/output so it can be tested.
"""

import random

from hangman.constants import BLANK, MAX_LIVES, WORD_LIST


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


class Game:
    """!
    @brief State of one Hangman game.
    """

    def __init__(self, word: str, lives: int = MAX_LIVES) -> None:
        """!
        @brief Start a new game.
        @param word The secret word.
        @param lives Wrong guesses allowed before losing.
        """
        ## The secret word.
        self.word = word.lower()
        ## Lives left.
        self.lives = lives
        ## Letters guessed so far.
        self.guesses: set[str] = set()

    def guess(self, letter: str) -> bool:
        """!
        @brief Process a guess; a wrong guess costs a life.
        @param letter A single letter.
        @return True if the letter is in the word.
        """
        letter = letter.lower()
        self.guesses.add(letter)
        correct = is_in_word(self.word, letter)
        if not correct:
            self.lives -= 1
        return correct

    def display(self) -> str:
        """!
        @brief The word with unguessed letters replaced by blanks.
        @return For example `"p _ n g _ i n"`.
        """
        return " ".join(c if c in self.guesses else BLANK for c in self.word)

    @property
    def won(self) -> bool:
        """!
        @brief True when every letter of the word has been guessed.
        """
        return all(c in self.guesses for c in self.word)

    @property
    def lost(self) -> bool:
        """!
        @brief True when no lives are left.
        """
        return self.lives <= 0

    @property
    def over(self) -> bool:
        """!
        @brief True when the game has been won or lost.
        """
        return self.won or self.lost
