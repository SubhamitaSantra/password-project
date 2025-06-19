from zxcvbn import zxcvbn

# Ask the user to enter a password
password = input("Enter a password to check its strength: ")

# Analyze password using zxcvbn
result = zxcvbn(password)

# Display results
print("\n🔐 Password Strength Analysis:")
print(f"Score (0-4): {result['score']}")
print(f"Estimated time to crack: {result['crack_times_display']['offline_fast_hashing_1e10_per_second']}")
print("Feedback:")
if result['feedback']['warning']:
    print(f"- Warning: {result['feedback']['warning']}")
if result['feedback']['suggestions']:
    for suggestion in result['feedback']['suggestions']:
        print(f"- Suggestion: {suggestion}")