from logic_utils import (
    check_guess,
    get_outcome_message,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_check_guess_invalid_input_returns_invalid():
    result = check_guess("abc", 50)
    assert result == "Invalid"


def test_parse_guess_empty_string():
    ok, guess, err = parse_guess("   ")
    assert ok is False
    assert guess is None
    assert err == "Enter a guess."


def test_parse_guess_decimal_truncates_toward_zero():
    ok, guess, err = parse_guess("12.9")
    assert ok is True
    assert guess == 12
    assert err is None


def test_parse_guess_invalid_text():
    ok, guess, err = parse_guess("not-a-number")
    assert ok is False
    assert guess is None
    assert err == "That is not a number."


def test_difficulty_ranges():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)
    assert get_range_for_difficulty("Unknown") == (1, 100)


def test_update_score_win_has_minimum_points():
    # For very late wins, score bonus should never drop below 10.
    score = update_score(current_score=0, outcome="Win", attempt_number=50)
    assert score == 10


def test_update_score_too_high_even_attempt_adds_points():
    score = update_score(current_score=10, outcome="Too High", attempt_number=2)
    assert score == 15


def test_update_score_too_high_odd_attempt_subtracts_points():
    score = update_score(current_score=10, outcome="Too High", attempt_number=3)
    assert score == 5


def test_update_score_too_low_subtracts_points():
    score = update_score(current_score=10, outcome="Too Low", attempt_number=3)
    assert score == 5


def test_get_outcome_message_values():
    assert get_outcome_message("Win") == "🎉 Correct!"
    assert get_outcome_message("Too High") == "📉 Go LOWER!"
    assert get_outcome_message("Too Low") == "📈 Go HIGHER!"


def test_get_outcome_message_fallback():
    assert get_outcome_message("Invalid") == "Invalid guess comparison."
