# O(n^2) time | O(n) space
def palindrome(string):
    reversedString = ""
    for i in reversed(range(len(string))) :
        reversedString += string[i]
    return string == reversedString
    
#string = "abcdcba"
#print(palindrome(string))