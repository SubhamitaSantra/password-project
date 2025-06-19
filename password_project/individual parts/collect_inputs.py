# Collecting basic personal information

print("🔍 Enter the following details to generate a custom wordlist:")

name = input("Name: ")
nickname = input("Nickname: ")
birth_year = input("Birth year (e.g. 2003): ")
pet_name = input("Pet name: ")
fav_word = input("Favorite word: ")

# Store inputs in a list
user_inputs = [name, nickname, birth_year, pet_name, fav_word]

# Remove blanks and duplicates
cleaned_inputs = list(set([word.strip() for word in user_inputs if word.strip() != ""]))

# Display collected data
print("\n✅ Collected keywords:")
for word in cleaned_inputs:
    print(f"- {word}")