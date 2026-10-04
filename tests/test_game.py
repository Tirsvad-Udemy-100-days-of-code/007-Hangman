from hangman.constants import WORD_LIST
from hangman.game import choose_word, is_in_word


def test_choose_word_from_list():
    assert choose_word(["Cat"]) == "cat"
    assert choose_word() in WORD_LIST


def test_letter_in_word():
    assert is_in_word("camel", "a")
    assert is_in_word("camel", "A")


def test_letter_not_in_word():
    assert not is_in_word("camel", "z")
