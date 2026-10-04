from hangman import main as cli


def run(monkeypatch, capsys, word, letter):
    monkeypatch.setattr(cli, "choose_word", lambda: word)
    monkeypatch.setattr("builtins.input", lambda _="": letter)
    cli.main()
    return capsys.readouterr().out


def test_right_guess_fills_blanks(monkeypatch, capsys):
    out = run(monkeypatch, capsys, "camel", "a")
    assert out.splitlines() == [
        "_ _ _ _ _",
        "Right, 'a' is in the word.",
        "_ a _ _ _",
    ]


def test_wrong_guess_keeps_blanks(monkeypatch, capsys):
    out = run(monkeypatch, capsys, "camel", "z")
    assert "Wrong" in out
    assert out.splitlines()[-1] == "_ _ _ _ _"
