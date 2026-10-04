"""!
@file main.py
@brief Command-line interface for Hangman.
"""

from hangman.game import choose_word, is_in_word


def main() -> None:
    """!
    @brief Entry point: pick a random word and check one guessed letter.
    """
    word = choose_word()
    guess = input("Guess a letter: ").strip()
    if is_in_word(word, guess):
        print(f"Right, '{guess.lower()}' is in the word.")
    else:
        print(f"Wrong, '{guess.lower()}' is not in the word.")


if __name__ == "__main__":
    main()
