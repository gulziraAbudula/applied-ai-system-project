# test_logic_utils.py

from logic_utils import (
    check_guess,
    get_outcome_message,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


# -----------------------------
# check_guess tests
# -----------------------------

def test_winning_guess():
    assert check_guess(50, 50) == "Win"


def test_guess_too_high():
    assert check_guess(60, 50) == "Too High"


def test_guess_too_low():
    assert check_guess(40, 50) == "Too Low"


# -----------------------------
# parse_guess tests
# -----------------------------

def test_parse_guess_valid():
    ok, guess, err = parse_guess("42")
    assert ok is True
    assert guess == 42
    assert err == ""


def test_parse_guess_empty():
    ok, guess, err = parse_guess("   ")
    assert ok is False
    assert guess is None
    assert err == "Please enter a number."


def test_parse_guess_invalid_text():
    ok, guess, err = parse_guess("abc")
    assert ok is False
    assert guess is None
    assert err == "Invalid input. Please enter a whole number."


def test_parse_guess_negative():
    ok, guess, err = parse_guess("-5")
    assert ok is False
    assert guess is None
    assert err == "Negative numbers are not allowed."


# -----------------------------
# difficulty tests
# -----------------------------

def test_difficulty_ranges():
    assert get_range_for_difficulty("Easy") == (1, 50)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 200)
    assert get_range_for_difficulty("Unknown") == (1, 100)


# -----------------------------
# update_score tests
# -----------------------------

def test_update_score_win_early():
    score = update_score(0, "Win", 1)
    assert score == 45  # 50 - 5


def test_update_score_win_minimum():
    score = update_score(0, "Win", 20)
    assert score == 10  # minimum


def test_update_score_wrong_guess():
    score = update_score(10, "Too High", 1)
    assert score == 9

    score = update_score(10, "Too Low", 1)
    assert score == 9


# -----------------------------
# outcome message tests
# -----------------------------

def test_get_outcome_message_values():
    assert get_outcome_message("Win") == "Correct! You cracked the system 🎉"
    assert get_outcome_message("Too High") == "Glitch detected: number is lower than your guess."
    assert get_outcome_message("Too Low") == "System anomaly: number is higher than your guess."


def test_get_outcome_message_fallback():
    assert get_outcome_message("Unknown") == "Unknown state detected."