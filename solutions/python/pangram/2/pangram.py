def is_pangram(sentence):
    sentence=sentence.lower()
    alphabets=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    return all(letter in sentence for letter in alphabets)
