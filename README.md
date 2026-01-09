# Hangman Game in Python 🎯

This is a simple Hangman game implemented using the Python programming language. It is a beginner-friendly project designed to help new programmers understand basic Python concepts such as loops, conditionals, strings, lists, and game logic.

---

## 📌 About the Game

The Hangman program randomly selects a secret word (a fruit name) from a predefined list. The player must guess the word letter by letter within a limited number of chances.

- Correct guesses reveal letters in the word
- Incorrect guesses reduce available chances
- The player wins by guessing all letters before chances run out

---

## 🧠 Game Logic Explained

1. A random word is selected using the `random` module
2. The word is hidden using underscores (`_`)
3. The player guesses one letter at a time
4. Each correct guess reveals the letter in the word
5. Total chances = length of the word + 2
6. The game ends when:
   - The word is fully guessed (Win)
   - All chances are used (Lose)

---

## 🛠️ Technologies Used

- Python 3
- Standard Libraries:
  - `random`
  - `collections.Counter`

---

## 🖼 Application Screenshot
![Application Screenshot]()

---

## 🤝 Contribution
Pull requests are welcome.  
If you'd like to improve this project, feel free to fork the repository and submit enhancements.
