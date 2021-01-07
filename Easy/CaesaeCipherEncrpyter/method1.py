# O(n) time | O(n) space
def cipher(string, key):
    newLetters = []
    newKey = key % 26
    for letter in string :
        newLetters.append(getNewLetter(letter, newKey))
    return "".join(newLetters)
    
def getNewLetter(letter, key):
    newLetterCode = ord(letter) + key
    return chr(newLetterCode) if newLetterCode <= 122 else chr(26 + newLetterCode % 122)
    

#string = "abc"
#print(cipher(string, 2))