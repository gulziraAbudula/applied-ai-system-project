# logic_utils.py

from typing import Tuple, Union


# -----------------------------
# Difficulty Configuration
# -----------------------------

def get_range_for_difficulty(difficulty: str) -> Tuple[int, int]:
    """
    Returns number range based on difficulty level.
    """
    if difficulty == "Easy":
        return 1, 50
    elif difficulty == "Normal":
        return 1, 100
    elif difficulty == "Hard":
        return 1, 200
    else:
        return 1, 100  # fallback


# -----------------------------
# Input Parsing
# -----------------------------

def parse_guess(raw_input: str) -> Tuple[bool, Union[int, None], str]:
    """
    Validates and converts user input into an integer guess.

    Returns:
        (is_valid, guess_value, error_message)
    """
    if raw_input is None or raw_input.strip() == "":
        return False, None, "Please enter a number."

    try:
        guess = int(raw_input)

        if guess < 0:
            return False, None, "Negative numbers are not allowed."

        return True, guess, ""

    except ValueError:
        return False, None, "Invalid input. Please enter a whole number."


# -----------------------------
# Core Game Logic
# -----------------------------

def check_guess(guess: int, secret: int) -> str:
    """
    Compares guess with secret number and returns outcome.
    """
    if guess == secret:
        return "Win"
    elif guess > secret:
        return "Too High"
    else:
        return "Too Low"


# -----------------------------
# Feedback Layer (AI-style enhancement point)
# -----------------------------

def get_outcome_message(outcome: str) -> str:
    """
    Converts raw game outcome into user-friendly message.
    """
    if outcome == "Win":
        return "Correct! You cracked the system 🎉"
    elif outcome == "Too High":
        return "Glitch detected: number is lower than your guess."
    elif outcome == "Too Low":
        return "System anomaly: number is higher than your guess."
    else:
        return "Unknown state detected."


# -----------------------------
# Scoring System
# -----------------------------

def update_score(current_score: int, outcome: str, attempt_number: int) -> int:
    """
    Updates score based on performance.

    Simple scoring logic:
    - Win early = higher score
    - Wrong guesses = small penalty scaling with attempts
    """
    if outcome == "Win":
        return current_score + max(10, 50 - (attempt_number * 5))

    elif outcome in ("Too High", "Too Low"):
        return current_score - 1

    return current_score