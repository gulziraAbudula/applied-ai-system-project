# Reflection: Glitchy Guesser

## 1. What are the limitations or biases in your system?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
1. I selected normal level game, the range was between 1 to 100, the secret was 62 and when I enter 50, it shows that I should "Go Lower" instead it should be go higher.
2. After clicking on New game after a round that I have won, it did not start a new game, it shows that “You already won. Start a new game to play again,” and after I enter a number again it did not do anything. New game did not refresh the score. 
3. For easy level game, the range was 1 to 20, but the secret was 82. When I enter anything out of range, it did not display error message, and showed me to go lower (I entered 50). 
---

## 2. Could your AI be misused, and how would you prevent that?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used copilot.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {max(0, attempt_limit - st.session_state.attempts)}"
)
The original one was "f"Attempts left: {attempt_limit - st.session_state.attempts}" " without max(0, ...). I verified this by confirming that an attempt should not be below zero. This verifies it always be 0 or above. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
I di not encounter incorrect or misleading one.
---

## 3.What surprised you while testing your AI's reliability?

- How did you decide whether a bug was really fixed?
I retested the app with the same function (3 bugs) that I mentioned in part 1 and everything looked as expected.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  def test_guess_too_high():
  # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"
    This test shows that if the user entered value which is the first parameter (guess) is greater than the targeted score, it should display "Too high" and it did display as expected.
- Did AI help you design or understand any tests? How?
yes, it generated all the possible test cases, and it all ran successfully. it checked each functions with edge cases.

---

## 4. Describe your collaboration with AI during this project. Identify one instance when the AI gave a helpful suggestion and one instance where its suggestion was flawed or incorrect.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
You have a Python script. Every time you click a button, type in a box, or move a slider, Streamlit re-executes the entire file from the top. Rerun is basically the page is rebuilt by running your Python code again, not just updating one small part.
Session state is how Streamlit remembers things between reruns.
Rerun = restarting a game.
Session state = your saved progress.
---

