# O(n) time | O(1) space
def MoveToEnd(array, element):
    firstIdx = 0
    secondIdx = len(array) - 1
    while firstIdx < secondIdx:
        left = array[firstIdx]
        right = array[secondIdx]
        if right == element:
            secondIdx -= 1
        elif left == element:
            temp = array[firstIdx]
            array[firstIdx] = array[secondIdx]
            array[secondIdx] = temp
        else:
            firstIdx += 1
    return array
    
array = [1, 5, 2, 4, 2, 6, 2, 9, 2]
print(MoveToEnd(array, 2))