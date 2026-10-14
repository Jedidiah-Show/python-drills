def clean(word):
    if not word:
        return
    if word[0].isalpha() and word[-1].isalpha():
        return word
    if word and not word[0].isalpha():
        word = word[1:]
    if not word:
        return
    if word and not word[-1].isalpha():
        word = word[:-1]
    return clean(word)

def longest_word(sentence):
    if not sentence:
        return sentence
    sentence = sentence.split()
    count, longest = 0, ""
    for word in sentence:
        word = clean(word)
        if not word:
            continue
        if len(word) > count:
            longest, count = word, len(word)
    return longest

# bonus
def longest_words(sentence):
    if not sentence:
        return []

    sentence, word_dict, count = sentence.split(), {}, 0
    for word in sentence:
        word = word.strip()
        word = clean(word)
        if not word:
            continue
        word_dict[word] = word_dict.get(word, 0) + len(word)
        if len(word) > count:
            count = len(word)
    longest = [word for word, length in word_dict.items() if length == count]
    return longest
