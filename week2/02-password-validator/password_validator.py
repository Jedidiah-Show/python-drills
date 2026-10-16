import re
import string

def has_min_length(password) -> bool:
    # Write your code here
    return True if len(password) >= 8 else False

def has_uppercase(password) -> bool:
    # Write your code here
    return True if any(char.isupper() for char in password) else False

def has_lowercase(password) -> bool:
    # Write your code here
    return True if any(char.islower() for char in password) else False


def has_digit(password) -> bool:
    # Write your code here
     return True if any(char.isdigit() for char in password) else False


def has_special(password) -> bool:
    # Write your code here
    return True if any(char in string.punctuation for char in password) else False

lowercase = r"(?=.*[a-z])"
uppercase = r"(?=.*[A-Z])"
digit = r"(?=.*\d)"
special = r"(?=.*[@$!%*?&])"
min_length = r"([A-Za-z\d@$!%*?&]{8,})"

def is_valid_password(password) -> bool:
    # Write your code here
    if not password:
        return False

    pattern = fr"^{lowercase}{uppercase}{digit}{special}{min_length}"
    # pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

    return bool(re.match(pattern, password))

#     requirements = [has_min_length, has_uppercase, has_lowercase, has_digit, has_special]
#
#     return all(func(password) for func in requirements)


# bonus
def get_failed_requirements(password):
    # Write your code here
    requirements = [min_length, uppercase, lowercase, digit, special]

    return list(pattern for pattern in requirements if not bool(re.match(fr"{pattern}", password)))

