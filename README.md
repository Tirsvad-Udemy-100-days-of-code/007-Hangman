# 🚀 Hangman

A beginner-friendly Python program that lets you play Hangman in the terminal against a randomly chosen word.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)

## 🧭 Overview

Day 7 of Udemy's *100 Days of Code™: The Complete Python Pro Bootcamp*. The game is built in five steps that follow the course:

1. Picking a random word and checking answers
2. Replacing blanks with guesses
3. Checking if the player has won *(this step)*
4. Keeping track of the player's lives
5. Improving the user experience

**Step 1:** the program picks a random word, asks for one letter and tells you whether the letter is in the word.

**Step 2:** the word is shown as blanks (`_ _ _ _ _`). After your guess every matching blank is replaced by the letter.

**Step 3:** the game keeps asking for letters until every blank is filled, then prints "You win!". (There are no lives yet, so wrong guesses cost nothing.)

## 📋 Requirements

- Python 3.13 or newer
- No runtime dependencies (the standard library is enough)
- `pytest` (only for running the tests)
- [Doxygen](https://www.doxygen.nl/) (optional, to build the API documentation)

## 🛠️ Setup

Create and activate a local virtual environment named `.venv`, then install the project in editable mode together with the test extra.

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Windows (cmd):

```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

macOS / Linux / Git Bash:

```bash
python3 -m venv .venv
source .venv/bin/activate        # Git Bash on Windows: source .venv/Scripts/activate
```

Then install:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[test]"
```

Run `deactivate` to leave the environment.

The `.env` file (access tokens for repository tooling) is ignored by git and is not needed to run the game.

To build the API documentation with Doxygen (output in `docs/api`):

```bash
doxygen Doxyfile
```

## ▶️ Run

```bash
python -m hangman
```

or, after installing:

```bash
hangman
```

## 🧪 Tests

```bash
python -m pytest
```

## 📄 License

GNU Affero General Public License v3.0 or later (AGPL-3.0-or-later). See [LICENSE](LICENSE).

## 🔗 Links

- [Repository](https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/007-Hangman)
- [Documentation](https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/007-Hangman#readme)
- [Issue tracker](https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/007-Hangman/issues)
