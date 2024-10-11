import re

def password_strength_checker(password):
    length_check = len(password) >= 8
    uppercase_check = re.search(r'[A-Z]', password) is not None
    lowercase_check = re.search(r'[a-z]', password) is not None
    digit_check = re.search(r'\d', password) is not None
    special_char_check = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    strength_score = sum([length_check, uppercase_check, lowercase_check, digit_check, special_char_check])
    if strength_score == 5:
        return "Strong password"
    elif strength_score >= 3:
        return "Moderate password"
    else:
        return "Weak password"
password = input("Enter a password to check its strength: ")
result = password_strength_checker(password)
print(result)
