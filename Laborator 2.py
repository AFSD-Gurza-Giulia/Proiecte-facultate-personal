import hashlib
import string


def get_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()


target_hash = "0e000d61c1735636f56154f30046be93b3d71f1abbac3cd9e3f80093fdb357ad"

uppercase_letters = list(string.ascii_uppercase)  # A-Z
lowercase_letters = list(string.ascii_lowercase)  # a-z
digits = list(string.digits)  # 0-9
special_chars = ['!', '@', '#', '$']

recursive_calls = 0


def backtrack(password="", uppercase_count=0, lowercase_count=0, digit_count=0, special_count=0):
    global recursive_calls
    recursive_calls += 1

    if len(password) == 6:
        if uppercase_count == 1 and lowercase_count == 3 and digit_count == 1 and special_count == 1:
            password_hash = get_hash(password)
            if password_hash == target_hash:
                print(f"Parola găsită: {password}")
                print(f"Număr apeluri recursive: {recursive_calls}")
                return True
        return False


    if uppercase_count < 1:
        for char in uppercase_letters:
            password_candidate = password + char
            if backtrack(password_candidate, uppercase_count + 1, lowercase_count, digit_count, special_count):
                return True

    if lowercase_count < 3:
        for char in lowercase_letters:
            password_candidate = password + char
            if backtrack(password_candidate, uppercase_count, lowercase_count + 1, digit_count, special_count):
                return True

    if digit_count < 1:
        for char in digits:
            password_candidate = password + char
            if backtrack(password_candidate, uppercase_count, lowercase_count, digit_count + 1, special_count):
                return True

    if special_count < 1:
        for char in special_chars:
            password_candidate = password + char
            if backtrack(password_candidate, uppercase_count, lowercase_count, digit_count, special_count + 1):
                return True

    return False


backtrack()