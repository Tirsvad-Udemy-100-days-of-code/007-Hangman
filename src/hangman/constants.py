"""!
@file constants.py
@brief Constants shared across the Hangman game.
"""

## Number of wrong guesses the player may make before losing.
MAX_LIVES = 6
## Character shown for a letter that has not been guessed yet.
BLANK = "_"
## Words the computer picks from.
WORD_LIST = [
    "aardvark",
    "baboon",
    "camel",
    "dolphin",
    "elephant",
    "flamingo",
    "giraffe",
    "hedgehog",
    "iguana",
    "kangaroo",
    "leopard",
    "octopus",
    "penguin",
    "squirrel",
    "tortoise",
]

## ASCII-art gallows, indexed by the number of lives left (0..MAX_LIVES).
STAGES = [
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========""",
]

## Message shown when the player wins.
MSG_WIN = "You win!"
## Message shown when the player loses (the word is appended).
MSG_LOSE = "You lose. The word was: "

## ANSI escape code that resets all colors and styles.
ANSI_RESET = "\033[0m"
## ANSI escape code for bold text.
ANSI_BOLD = "\033[1m"
## ANSI escape code for red text.
ANSI_RED = "\033[31m"

## ASCII-art title shown on start-up.
TITLE_ART = r"""
 _   _
| | | | __ _ _ __   __ _ _ __ ___   __ _ _ __
| |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
|  _  | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                   |___/
"""
