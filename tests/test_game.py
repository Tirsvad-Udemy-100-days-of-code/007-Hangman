import pytest

from hangman.constants import MAX_LIVES, STAGES, WORD_LIST
from hangman.game import Game, choose_word, is_in_word


def test_choose_word_from_list():
    assert choose_word(["Cat"]) == "cat"
    assert choose_word() in WORD_LIST


def test_letter_in_word():
    assert is_in_word("camel", "a")
    assert is_in_word("camel", "A")


def test_letter_not_in_word():
    assert not is_in_word("camel", "z")


def test_display_starts_blank():
    assert Game("cat").display() == "_ _ _"


def test_correct_guess_reveals_letters():
    g = Game("banana")
    assert g.guess("a") is True
    assert g.display() == "_ a _ a _ a"


def test_wrong_guess_keeps_blanks():
    g = Game("cat")
    assert g.guess("z") is False
    assert g.display() == "_ _ _"


def test_not_won_until_all_letters_guessed():
    g = Game("hi")
    assert not g.won
    g.guess("h")
    assert not g.won
    g.guess("i")
    assert g.won


def test_wrong_guesses_do_not_win():
    g = Game("hi")
    g.guess("x")
    assert not g.won


def test_wrong_guess_loses_life():
    g = Game("cat")
    assert g.lives == MAX_LIVES
    g.guess("z")
    assert g.lives == MAX_LIVES - 1


def test_correct_guess_keeps_lives():
    g = Game("cat")
    g.guess("c")
    assert g.lives == MAX_LIVES


def test_lost_when_out_of_lives():
    g = Game("hi", lives=2)
    g.guess("x")
    assert not g.lost
    g.guess("y")
    assert g.lost and g.over and not g.won


def test_stages_cover_all_lives():
    assert len(STAGES) == MAX_LIVES + 1


def test_repeated_guess_is_free():
    g = Game("cat")
    g.guess("z")
    assert g.guess("Z") is None
    assert g.lives == MAX_LIVES - 1


def test_invalid_guess():
    g = Game("cat")
    for bad in ("", "ab", "1", " "):
        with pytest.raises(ValueError):
            g.guess(bad)
    assert g.lives == MAX_LIVES
