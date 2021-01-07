# O(n) time | O(1) space
def maxSubsetSum(array):
    if not len(array):
        return
    elif len(array) == 1:
        return array[1]
    first = array[0]
    second = max(array[0], array[1])
    for i in range(2, len(array)):
        current = max(second, first + array[i])
        first = second
        second = current
    return second
    
array = [2, 4, 8, 3, 9, 10]
print(maxSubsetSum(array))