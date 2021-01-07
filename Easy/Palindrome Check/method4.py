# O(n) time | O(1) space
def palindrome(string):
    leftIdx = 0
    rightIdx = len(string) - 1
    while leftIdx < rightIdx :
        if string[leftIdx] != string[rightIdx] :
            return False
        leftIdx += 1
        rightIdx -= 1
    return True
    
#string = "abcdcba"
#print(palindrome(string))
    