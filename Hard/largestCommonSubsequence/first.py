def largestCommonSubsequence(str1, str2):
    subsequenceArray = []
    for k in range(0, len(str1)):
        sequence = []
        lastIdx = 0
        for i in range(k, len(str1)):
            j = lastIdx
            if len(sequence) == 0 and i > k:
                break
            while j < len(str2):
                if str1[i] == str2[j]:
                    lastIdx = j + 1
                    sequence.append(str2[j])
                    break
                j += 1
        if len(sequence):
            subsequenceArray.append(sequence)
    longestArray = []
    for arr in subsequenceArray:
        if len(arr) > len(longestArray):
            longestArray = arr
    print(longestArray)
    
str1 = 'ZXVVYZW'
str2 = 'XKYKZPW'
largestCommonSubsequence(str1, str2)