def is_isogram(phrase):
    letters=[]
    phrase=phrase.lower()
    for letter in phrase:
        if letter not in {'-' ,' '}:
            if letter in letters:
                return False
            letters.append(letter)
    return True
