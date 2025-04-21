import re

def check_password_strength(password):
    strength_score = 0
    remarks = ""

    # Criteria checks
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Assign score based on criteria met
    if length_criteria:
        strength_score += 1
    if uppercase_criteria:
        strength_score += 1
    if lowercase_criteria:
        strength_score += 1
    if digit_criteria:
        strength_score += 1
    if special_char_criteria:
        strength_score += 1

    # Strength classification
    if strength_score == 5:
        remarks = "🟢 Strong Password (Great!)"
    elif 3 <= strength_score < 5:
        remarks = "🟡 Medium Strength (Consider improving)"
    else:
        remarks = "🔴 Weak Password (Not secure!)"

    return {"password": password, "score": strength_score, "remarks": remarks}

# Example Test
if __name__ == "__main__":
    test_password = input("Enter a password to test: ")
    result = check_password_strength(test_password)
    print(f"Password: {result['password']}\nStrength: {result['score']}/5\nRemarks: {result['remarks']}")
