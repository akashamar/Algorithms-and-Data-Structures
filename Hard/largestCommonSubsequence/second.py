# O(nm*in(n,m)) time = space
def largestCommonSubsequence(str1, str2):
    lcs = [[[] for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + [str1[i - 1]]
            else:
                lcs[i][j] = max(lcs[i][j - 1], lcs[i -1][j], key = len)
    print(lcs[-1][-1])
    
str1 = 'ZXVVYZW'
str2 = 'XKYKZPW'
largestCommonSubsequence(str1, str2)