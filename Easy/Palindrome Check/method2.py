# O(n) time | O(n) space
def palindrome(string):
    reversedChar = []
    for i in reversed(range(len(string))) :
        reversedChar.append(string[i])
    return string == "".join(reversedChar)
    
#string = "abcdcba"
#print(palindrome(string))