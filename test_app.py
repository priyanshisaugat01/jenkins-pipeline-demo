from app import guess_number

def test_guess(monkeypatch):
    # Fake user input and random number
    monkeypatch.setattr('builtins.input', lambda _: "3")
    monkeypatch.setattr('random.randint', lambda a, b: 3)

    result = guess_number()
    assert "Correct" in result
