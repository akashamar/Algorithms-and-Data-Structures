# O(n) time | O(n) space
def maxSubsetSum(array):
    if not len(array):
        return
    elif len(array) == 1:
        return array[1]
    maxSums = array[:]
    maxSums[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        maxSums[i] = max(maxSums[i -1], maxSums[i - 2] + array[i])
    return maxSums[-1]
    
array = [2, 4, 8, 3, 9, 10]
print(maxSubsetSum(array))