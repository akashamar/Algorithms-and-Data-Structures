# O(n) time | O(1) space
def kadanes(arr):
    currentMax = 0
    maxSumResult = 0
    for i in range(len(arr)):
        currentMax = max((currentMax + arr[i]), (arr[i]))
        maxSumResult = max(maxSumResult, currentMax)
    return maxSumResult
    
arr = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
print(kadanes(arr))