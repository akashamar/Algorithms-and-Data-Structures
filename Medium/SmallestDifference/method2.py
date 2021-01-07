# O(nLog(n) + mLog(m)) time | O(1) space
def SmallestDifference(array1, array2):
    array1.sort()
    array2.sort()
    difference = float('inf')
    currentDiff = float('inf')
    Nums = []
    leftIdx = 0
    rightIdx = 0
    while leftIdx < len(array1) and rightIdx < len(array2):
        left = array1[leftIdx]
        right = array2[rightIdx]
        if left < right:
            currentDiff = right - left
            leftIdx += 1
        elif right < left:
            currentDiff = left - right
            rightIdx += 1
        else:
            return [left, right]
        if difference > currentDiff:
            difference = currentDiff
            Nums = [left, right]
    return Nums


array1 = [0, -3, 9, 8, 2, 6]
array2 = [4, 5, 3, 5, 1]
print(SmallestDifference(array1, array2))