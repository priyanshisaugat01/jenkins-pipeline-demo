from app import guess_number

def test_guess(monkeypatch):
    # Simulate user guessing correctly
    monkeypatch.setattr('builtins.input', lambda _: "3")
    monkeypatch.setattr('random.randint', lambda a, b: 3)

    result = guess_number()
    assert "Correct" in result
