from hangman import main as cli
from hangman.game import Game


def run(monkeypatch, capsys, word, inputs):
    it = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _="": next(it))
    cli.play(Game(word))
    return capsys.readouterr().out


def test_play_until_won(monkeypatch, capsys):
    out = run(monkeypatch, capsys, "hi", ["z", "h", "i"])
    assert out.splitlines() == [
        "_ _",
        "Wrong, 'z' is not in the word.",
        "_ _",
        "Right, 'h' is in the word.",
        "h _",
        "Right, 'i' is in the word.",
        "h i",
        "You win!",
    ]


def test_repeated_letter_fills_all_blanks(monkeypatch, capsys):
    out = run(monkeypatch, capsys, "aa", ["a"])
    assert out.splitlines()[-2:] == ["a a", "You win!"]
