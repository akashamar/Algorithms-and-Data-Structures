# o(n) time | O(n) space
def cipher(string, key):
    newLetters = []
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    newKey = key % 26
    for letter in string :
        newLetters.append(getNewLetter(letter, newKey, alphabet))
    return "".join(newLetters)
    
def getNewLetter(letter, key, alphabet):
    newLetterIdx = alphabet.index(letter) + key
    return alphabet[newLetterIdx] if newLetterIdx <= 25 else alphabet[-1 + newLetterIdx % 25]
    

#string = "abc"
#print(cipher(string, 2))