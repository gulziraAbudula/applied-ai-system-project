#  Game Glitch Investigator: The Impossible Guesser (AI Guessing Game)

## Original Project

Glitchy Guesser is a number-guessing game built using Python and Streamlit. In its original version, the project focused on core game logic where the user selects a difficulty level and tries to guess a randomly generated number within a range. The system provides feedback such as “too high” or “too low” until the correct number is found. The goal was to practice modular Python design, user input handling, and separating game logic from the UI layer.

## Title & Summary

Game Glitch Investigator: The Impossible Guesser (AI Guessing Game)

Glitchy Guesser is an interactive web-based number guessing game where users attempt to identify a randomly generated hidden number across different difficulty levels. The original version relied purely on rule-based logic for generating numbers, validating guesses, and providing feedback such as “too high” or “too low.”

In the AI-enhanced version, the system goes beyond static game logic by incorporating AI-assisted reasoning to improve feedback clarity, generate more adaptive and user-friendly hints, and better guide the player through the guessing process. This makes the gameplay feel more dynamic and intelligent compared to the original deterministic version. The project demonstrates how AI can augment traditional application logic to create a more engaging user experience using Python and Streamlit.

## Architecture Overview

The system is split into two main components:
1. **Frontend (Streamlit UI - app.py)** 
   - Handles user interaction
   - Displays game state, messages, and inputs
   - Calls backend logic functions
2. **Backend (logic_utils.py)**
   - Contains core game functions:
      - Guess validation (check_guess)
      - Difficulty range selection (get_range_for_difficulty)
      - Score tracking (update_score)
      - Input parsing and messaging

**Flow:**
User Input -> Streamlit UI -> Logic Layer -> Result Returned -> UI Update


## Setup Instructions

1. **Clone the repository** 
git clone https://github.com/your-username/glitchy-guesser.git
cd glitchy-guesser

2. **Create virtual environment**
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. **Install dependencies**
pip install streamlit

4. **Run the application**
streamlit run app.py


## Sample Interactions

1. **Example 1**
Input: 
   - Difficulty: Easy
   - Guess: 42
Output: 
   - "Too low! Try a higher number."

2. **Example 2**
Input: 
   - Difficulty: Medium
   - Guess: 73
Output: 
   - "Too high! Try a lower number."

3. **Example 3**
Input: 
   - Difficulty: Hard
   - Guess: 58
Output: 
   - "Correct! You cracked the code 🎉 Score updated."

## Design Decisions

- **Separation of Logic and UI:**
   - I isolated game logic into a separate module.
- **Streamlit for UI:**
   - Chosen for fast prototyping and clean web interface without needing frontend frameworks.
- **Modular Function Design:**
   - Each function handles a single responsibility (e.g., parsing, scoring, validation).

**Trade-offs**
- Streamlit limits advanced UI customization.


## Testing Summary

- **What worked:**
   - Core guessing logic performed correctly across difficulty levels.
   - UI updates correctly reflected backend state.
   - Input validation prevented crashes from invalid guesses.
- **What didn't work:**
   - Some edge cases in input parsing (non-numeric input) initially caused errors.
- **What I learned:**
   - Importance of separating UI and logic early.
   - Writing modular Python code improves scalability significantly.

## Reflection
Through building this project, I learned how to structure a small but complete Python application with a clear separation between UI (Streamlit) and backend logic. Breaking the system into modules like app.py and logic_utils.py helped me understand how decoupling components improves maintainability, testing, and debugging. On the technical side, I also learned how to integrate rule-based logic with AI-assisted components in a controlled way—using AI to enhance user feedback and hints without replacing the deterministic core game engine.