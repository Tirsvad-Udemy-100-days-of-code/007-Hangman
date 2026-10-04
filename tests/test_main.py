from hangman import main as cli


def run(monkeypatch, capsys, word, letter):
    monkeypatch.setattr(cli, "choose_word", lambda: word)
    monkeypatch.setattr("builtins.input", lambda _="": letter)
    cli.main()
    return capsys.readouterr().out


def test_right_guess(monkeypatch, capsys):
    assert "Right" in run(monkeypatch, capsys, "camel", "a")


def test_wrong_guess(monkeypatch, capsys):
    assert "Wrong" in run(monkeypatch, capsys, "camel", "z")
