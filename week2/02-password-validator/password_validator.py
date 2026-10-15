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


def is_valid_password(password) -> bool:
    # Write your code here
    if not password:
        return False
    if has_uppercase(password) and has_lowercase(password) and has_min_length(password) and has_special(password) and has_digit(password):
        return True
    return False

# bonus
def get_failed_requirements(password):
    # Write your code here
    requirements = [has_min_length, has_uppercase, has_lowercase, has_digit, has_special]
    failed = []
    for func in requirements:
        if not func(password):
            failed += [f'{func.__name__[4:]}']
    return failed 
