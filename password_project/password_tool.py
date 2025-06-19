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

def check_password_strength():
    password = input("\n🔑 Enter the password you want to check: ")
    result = zxcvbn(password)

    print("\n🔐 Password Strength Report:")
    print(f"- Score (0 = weak, 4 = strong): {result['score']}")
    print(f"- Estimated crack time: {result['crack_times_display']['offline_fast_hashing_1e10_per_second']}")
    
    print("- Feedback:")
    if result['feedback']['warning']:
        print(f"  ⚠️ Warning: {result['feedback']['warning']}")
    if result['feedback']['suggestions']:
        for suggestion in result['feedback']['suggestions']:
            print(f"  💡 Suggestion: {suggestion}")
    print()

def generate_custom_wordlist():
    print("\n📝 Enter personal details to generate a custom wordlist:")
    name = input("Name: ")
    nickname = input("Nickname: ")
    birth_year = input("Birth Year: ")
    pet_name = input("Pet Name: ")
    fav_word = input("Favorite Word: ")

    user_inputs = [name, nickname, birth_year, pet_name, fav_word]
    user_inputs = list(set([w.strip().lower() for w in user_inputs if w.strip() != ""]))

    add_ons = ['', '123', '2024', '007', '!', '@']
    wordlist = set()

    def generate_leetspeak(word):
        variations = ['']
        for char in word:
            if char in leetspeak:
                variations = [prefix + rep for prefix in variations for rep in leetspeak[char]]
            else:
                variations = [prefix + char for prefix in variations]
        return variations

    for word in user_inputs:
        leet_versions = generate_leetspeak(word)
        for variant in leet_versions:
            for addon in add_ons:
                wordlist.add(variant + addon)
                wordlist.add(addon + variant)

    for combo in itertools.permutations(user_inputs, 2):
        wordlist.add(combo[0] + combo[1])
        wordlist.add(combo[1] + combo[0])

    with open("custom_wordlist.txt", "w") as f:
        for word in sorted(wordlist):
            f.write(word + "\n")

    print(f"\n✅ Wordlist saved as 'custom_wordlist.txt'. Total passwords: {len(wordlist)}\n")

def main():
    while True:
        print("📌 Password Tool Menu:")
        print("1. Check password strength")
        print("2. Generate custom password wordlist")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            check_password_strength()
        elif choice == '2':
            generate_custom_wordlist()
        elif choice == '3':
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.")

# Run the main menu
main()