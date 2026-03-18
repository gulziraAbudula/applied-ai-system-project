# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
1. I selected normal level game, the range was between 1 to 100, the secret was 62 and when I enter 50, it shows that I should "Go Lower" instead it should be go higher.
2. After clicking on New game after a round that I have won, it did not start a new game, it shows that “You already won. Start a new game to play again,” and after I enter a number again it did not do anything. New game did not refresh the score. 
3. For easy level game, the range was 1 to 20, but the secret was 82. When I enter anything out of range, it did not display error message, and showed me to go lower (I entered 50). 
---

## 2. How did you use AI as a teammate?

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

## 3. Debugging and testing your fixes

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

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
You have a Python script. Every time you click a button, type in a box, or move a slider, Streamlit re-executes the entire file from the top. Rerun is basically the page is rebuilt by running your Python code again, not just updating one small part.
Session state is how Streamlit remembers things between reruns.
Rerun = restarting a game.
Session state = your saved progress.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
I will start using agent to help debug my code be specific when I ask it to generate the code/debug, and provide meaningful prompt. An I will be using copilot to run the pytest to help with the validation process. A prompting strategy that I will use is to add #name_of_the_file when I try to debug the code to help identify the problem, and after I read the code comprehensively and fully understood the code, before copilot identify any problems I will add a #FIXME comment where I think it needs a fix. 
- What is one thing you would do differently next time you work with AI on a coding task?
I will not justs accept the generated code without having a complete understanding, I will first understand the code and if it makes sense, then I will accept the coe.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
AI generated code is not perfect, but it is very useful to set a base, I still need to have a very good understanding of the code and confidence in my coding skills. 

