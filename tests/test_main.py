from hangman import main as cli
from hangman.constants import ANSI_BOLD, ANSI_RED, ANSI_RESET, STAGES
from hangman.game import Game


def run(monkeypatch, capsys, word, inputs):
    it = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _="": next(it))
    cli.play(Game(word))
    return capsys.readouterr().out


def test_play_until_won(monkeypatch, capsys):
    out = run(monkeypatch, capsys, "hi", ["z", "h", "i"])
    assert "'z' is not in the word. You lose a life." in out
    assert "h i" in out
    assert out.splitlines()[-1] == "You win!"


def test_repeated_and_invalid_input(monkeypatch, capsys):
    out = run(monkeypatch, capsys, "hi", ["h", "h", "?", "ab", "i"])
    assert "You already guessed 'h'." in out
    assert out.count("Please enter a single letter.") == 2
    assert out.splitlines()[-1] == "You win!"


def test_play_until_lost(monkeypatch, capsys):
    out = run(monkeypatch, capsys, "a", list("bcdefg"))
    assert STAGES[0] in out
    assert out.splitlines()[-1] == "You lose. The word was: a"


def test_gallows_grows_with_wrong_guesses(monkeypatch, capsys):
    out = run(monkeypatch, capsys, "a", ["b", "a"])
    assert STAGES[6] in out and STAGES[5] in out


def test_title_plain_when_not_a_terminal(capsys):
    cli.show_title()
    out = capsys.readouterr().out
    assert "" not in out
    assert "|___/" in out


def test_title_colored_in_a_terminal(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdout.isatty", lambda: True, raising=False)
    monkeypatch.delenv("NO_COLOR", raising=False)
    monkeypatch.setattr(cli.os, "system", lambda _: 0)
    cli.show_title()
    out = capsys.readouterr().out
    assert out.startswith(ANSI_BOLD + ANSI_RED) and ANSI_RESET in out
