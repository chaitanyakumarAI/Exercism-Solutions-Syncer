def is_pangram(sentence):
    sentence=sentence.lower()
    alphabets=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    for letter in alphabets:
        if letter not in sentence:
            return False
    return True
