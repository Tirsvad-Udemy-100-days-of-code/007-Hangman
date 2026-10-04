from hangman.constants import WORD_LIST
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
