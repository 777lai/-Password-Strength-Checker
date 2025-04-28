import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_criteria = re.search(r'[\W_]', password) is not None  # \W matches any non-alphanumeric character

    score = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])

    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    # Feedback
    print(f"Password Strength: {strength}")
    print("Suggestions:")
    if not length_criteria:
        print("- Use at least 8 characters.")
    if not upper_criteria:
        print("- Add uppercase letters.")
    if not lower_criteria:
        print("- Add lowercase letters.")
    if not digit_criteria:
        print("- Include numbers.")
    if not special_criteria:
        print("- Include special characters (e.g. !, @, #, etc.)")

# Example
password_input = input("Enter a password to check its strength: ")
check_password_strength(password_input)
