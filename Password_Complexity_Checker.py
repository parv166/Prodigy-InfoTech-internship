import string

def password_strength(password):
    print("Checking password strength...")  # Debugging line
    score = 0
    
    length_score = len(password)
    print(f"Password length: {length_score}")  # Debugging line
    if length_score >= 8:
        score += 1
    if length_score >= 12:
        score += 1
    if length_score >= 16:
        score += 1

    if any(c.islower() for c in password):
        score += 1
    
    if any(c.isupper() for c in password):
        score += 1
    
    if any(c.isdigit() for c in password):
        score += 1
    
    if any(c in string.punctuation for c in password):
        score += 1

    print(f"Score: {score} out of 7")  # Debugging line

    if score < 3:
        print("Weak password. Consider making your password longer and including more character types.")
    elif score < 5:
        print("Good password. Consider using a mix of different character types for better strength.")
    else:
        print("Strong password! You've created a secure password.")

password = input("Enter your password: ")
password_strength(password)
