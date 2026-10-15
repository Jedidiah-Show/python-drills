def first_non_repeating(s, case_sensitive=True):
    # Write your code here
    if not s:
        return None
    s = s if case_sensitive else s.lower()
    char_list = list(filter(lambda x: s.count(x) == 1, s))
    return char_list[0] if char_list else None
