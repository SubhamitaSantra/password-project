import tkinter as tk
from tkinter import ttk, messagebox
from zxcvbn import zxcvbn
import itertools

# Leetspeak substitutions
leetspeak = {
    'a': ['a', '@', '4'],
    'e': ['e', '3'],
    'i': ['i', '1', '!'],
    'o': ['o', '0'],
    's': ['s', '$', '5'],
    'l': ['l', '1']
}

# Function to check password strength
def check_strength():
    password = password_entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return
    result = zxcvbn(password)
    score = result['score']
    time = result['crack_times_display']['offline_fast_hashing_1e10_per_second']
    feedback = result['feedback']

    result_text = f"Score (0-4): {score}\nEstimated crack time: {time}\n"
    if feedback['warning']:
        result_text += f"\nWarning: {feedback['warning']}\n"
    for suggestion in feedback['suggestions']:
        result_text += f"Suggestion: {suggestion}\n"

    strength_result.delete(1.0, tk.END)
    strength_result.insert(tk.END, result_text)

# Function to generate wordlist
def generate_wordlist():
    name = name_entry.get().strip().lower()
    nickname = nickname_entry.get().strip().lower()
    year = year_entry.get().strip()
    pet = pet_entry.get().strip().lower()
    fav = fav_entry.get().strip().lower()

    inputs = [name, nickname, year, pet, fav]
    user_inputs = list(set([i for i in inputs if i != ""]))
    if not user_inputs:
        messagebox.showwarning("Input Error", "Please fill at least one field.")
        return

    def leet_variants(word):
        variations = ['']
        for char in word:
            if char in leetspeak:
                variations = [prefix + rep for prefix in variations for rep in leetspeak[char]]
            else:
                variations = [prefix + char for prefix in variations]
        return variations

    addons = ['', '123', '2024', '007', '!', '@']
    wordlist = set()

    for word in user_inputs:
        for variant in leet_variants(word):
            for addon in addons:
                wordlist.add(variant + addon)
                wordlist.add(addon + variant)

    for combo in itertools.permutations(user_inputs, 2):
        wordlist.add(combo[0] + combo[1])
        wordlist.add(combo[1] + combo[0])

    with open("custom_wordlist.txt", "w") as f:
        for word in sorted(wordlist):
            f.write(word + "\n")

    messagebox.showinfo("Success", f"Generated {len(wordlist)} passwords and saved to custom_wordlist.txt")

# Create GUI Window
root = tk.Tk()
root.title("Password Strength & Wordlist Tool")
root.geometry("500x600")

# Tabs
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Password Strength Checker')
tabControl.add(tab2, text='Custom Wordlist Generator')
tabControl.pack(expand=1, fill="both")

# Tab 1 - Password Strength Checker
tk.Label(tab1, text="Enter Password:").pack(pady=5)
password_entry = tk.Entry(tab1, width=40, show="*")
password_entry.pack(pady=5)
tk.Button(tab1, text="Check Strength", command=check_strength).pack(pady=10)
strength_result = tk.Text(tab1, height=10, width=55)
strength_result.pack(pady=5)

# Tab 2 - Wordlist Generator
tk.Label(tab2, text="Name:").pack()
name_entry = tk.Entry(tab2, width=40)
name_entry.pack()

tk.Label(tab2, text="Nickname:").pack()
nickname_entry = tk.Entry(tab2, width=40)
nickname_entry.pack()

tk.Label(tab2, text="Birth Year:").pack()
year_entry = tk.Entry(tab2, width=40)
year_entry.pack()

tk.Label(tab2, text="Pet Name:").pack()
pet_entry = tk.Entry(tab2, width=40)
pet_entry.pack()

tk.Label(tab2, text="Favorite Word:").pack()
fav_entry = tk.Entry(tab2, width=40)
fav_entry.pack()

tk.Button(tab2, text="Generate Wordlist", command=generate_wordlist).pack(pady=15)

root.mainloop()