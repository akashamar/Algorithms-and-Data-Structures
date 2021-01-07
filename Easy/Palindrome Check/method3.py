# O(n) time | O(n) space
def isPalindrome(string, i = 0):
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and isPalindrome(string, i + 1)
    
#string = "abcdcba"
#print(isPalindrome(string))