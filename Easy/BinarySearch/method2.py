# O(log(n)) time | O(1) space
# space complexity is better than previous method
def BinarySearch(array, target) :
    return BinarySearchHelper(array, target, 0, len(array) -1)
    
def BinarySearchHelper(array, target, left, right) :
    while left <= right :
        middle = (left + right) // 2
        potentialMatch = array[middle]
        if target == potentialMatch :
            return middle
        elif target < potentialMatch :
            right = middle - 1
        else :
            left = middle + 1
    return 'NOT FOUND'
    

#array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#print(BinarySearch(array, 3))