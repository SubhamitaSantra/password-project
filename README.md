# 🔐 Password Strength Analyzer & Custom Wordlist Generator

This is a beginner-friendly cybersecurity tool built in Python to help users:

✅ Analyze the strength of passwords using real-world cracking logic  
✅ Generate personalized password wordlists using user information and hacker-style variations  
✅ Use a CLI or a GUI interface for easy access  
✅ Export custom wordlists for ethical hacking or security testing

---

## Features

- **Password Strength Checker**  
  Uses [zxcvbn](https://github.com/dropbox/zxcvbn) to rate password strength, suggest improvements, and estimate crack times.

- **Custom Wordlist Generator**  
  Takes user inputs like name, nickname, birth year, pet name, etc. and generates intelligent variations using:
  - Leetspeak replacements (like `@` for `a`, `0` for `o`)
  - Common suffixes (`123`, `@`, `007`)
  - Smart permutations
  - Saves the final list in `.txt` format

- **CLI + GUI Interface**  
  Offers a command-line tool for fast usage and a Tkinter GUI for ease of use with textboxes and buttons.

---

## Technologies Used

- Python 3  
- `zxcvbn` – for password analysis  
- `Tkinter` – for GUI  
- `itertools` – for wordlist combinations  
- Standard I/O and file handling  

---
