# 🔐 Day 5: PyPassword Generator

Welcome to Day 5 of my **#100DaysOfCodePython** challenge!  
Today, I built a **random password generator** that creates secure and unpredictable passwords based on user input — perfect for boosting your cybersecurity habits. 🛡️✨

---

## 💻 Project Description

The **PyPassword Generator** asks the user how many:
- **Letters** (both uppercase and lowercase),
- **Symbols** (like `!`, `#`, `%`, etc.),
- **Numbers** (`0-9`)

...they want in their password. It then:
- Randomly selects characters from each category,
- Shuffles the final list to ensure true randomness,
- Joins and prints a secure password string.

---

## 🧠 What I Learned

- 🎲 How to use `random.choice()` and `random.shuffle()` effectively.
- 🔁 Looping with `range()` to collect multiple characters based on user input.
- 💡 Storing items in lists and later converting them into a string.
- 🧪 Importance of mixing elements (letters, symbols, numbers) for secure password creation.
- 👀 Improved my understanding of list manipulation and user input handling in Python.

---

## 🧪 Sample Run

```text
Welcome to the PyPassword Generator!
How many letters would you like in your password?
> 5
How many symbols would you like?
> 2
How many numbers would you like?
> 3

Your password is: 8$ATp3#e1
