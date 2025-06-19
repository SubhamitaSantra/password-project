import math

def calculate_entropy(password):
    charset = 0
    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(c in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~" for c in password):
        charset += 32  # rough estimate for special characters

    entropy = math.log2(charset ** len(password))
    return round(entropy, 2)

# Take user input
password = input("Enter a password: ")
entropy = calculate_entropy(password)

print(f"\n🔐 Password Entropy: {entropy} bits")
if entropy < 40:
    print("⚠️ Very weak password.")
elif entropy < 60:
    print("⚠️ Weak password. Try to add more variety or length.")
elif entropy < 80:
    print("✅ Good password.")
else:
    print("🔒 Strong password.")