# Reflection: Glitchy Guesser

## 1. What are the limitations or biases in your system?

- This system is entirely rule-based, which means its behavior is deterministic and limited to predefined logic. It does not learn from user behavior or adapt over time. As a result, the “AI-like” feedback is constrained to a fixed set of responses and may feel repetitive or less intelligent after extended use. 
- Additionally, the system assumes valid numeric input within a specific range. While input validation is implemented, the system does not handle more complex or ambiguous user inputs (e.g., natural language guesses), which limits its flexibility compared to real AI systems.
---

## 2. Could your AI be misused, and how would you prevent that?

- Since this is a simple guessing game, the risk of harmful misuse is low.
---

## 3.What surprised you while testing your AI's reliability?

- Early tests showed that invalid inputs (empty strings or non-numeric values) could break the expected flow. After adding parse_guess() and proper validation checks, the system became significantly more stable and predictable.
---

## 4. Describe your collaboration with AI during this project. Identify one instance when the AI gave a helpful suggestion and one instance where its suggestion was flawed or incorrect.

- At one point, AI suggested test cases and behaviors that did not match my actual implementation (incorrect difficulty ranges, and allowing decimal parsing). This required me to carefully review and correct the tests to ensure they aligned with the real code.
---

