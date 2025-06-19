print("🔐 Enter personal details to generate a custom password wordlist")

name = input("Your Name: ")
nickname = input("Nickname: ")
birth_year = input("Birth Year (e.g. 2003): ")
pet_name = input("Pet Name: ")
fav_word = input("Favorite Word: ")

# Store all inputs into a list
user_inputs = [name, nickname, birth_year, pet_name, fav_word]

# Clean list: remove empty entries and duplicates
user_inputs = list(set([item.strip().lower() for item in user_inputs if item.strip() != ""]))

import itertools

# Hacker-style letter replacements
leetspeak = {
    'a': ['a', '@', '4'],
    'e': ['e', '3'],
    'i': ['i', '1', '!'],
    'o': ['o', '0'],
    's': ['s', '$', '5'],
    'l': ['l', '1']
}

# Function to generate leetspeak variations
def generate_leetspeak(word):
    variations = ['']
    for char in word:
        if char in leetspeak:
            variations = [prefix + replacement for prefix in variations for replacement in leetspeak[char]]
        else:
            variations = [prefix + char for prefix in variations]
    return variations

# Add-ons to append or prepend to words
add_ons = ['', '123', '2024', '007', '!', '@']

# Final password list
wordlist = set()

# Create password patterns
for word in user_inputs:
    leet_versions = generate_leetspeak(word)
    for variant in leet_versions:
        for addon in add_ons:
            wordlist.add(variant + addon)
            wordlist.add(addon + variant)

# Combine multiple user words (like subha + tuffy)
for combo in itertools.permutations(user_inputs, 2):
    wordlist.add(combo[0] + combo[1])
    wordlist.add(combo[1] + combo[0])

# Save the final wordlist to a text file
with open("custom_wordlist.txt", "w") as file:
    for word in sorted(wordlist):
        file.write(word + "\n")

print("\n✅ Password wordlist saved as custom_wordlist.txt")
print(f"Total passwords generated: {len(wordlist)}")