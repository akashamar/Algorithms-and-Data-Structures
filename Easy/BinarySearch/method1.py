# O(log(n)) time || O(log(n)) space
# n = the no of elements in array
def BinarySearch(array, target) :
    return BinarySearchHelper(array, target, 0, len(array) -1)
    
def BinarySearchHelper(array, target, left, right) :
    if left > right :
        return 'NOT FOUND'
    middle = (left + right) // 2
    potentialMatch = array[middle]
    if target == potentialMatch :
        return middle
    elif target < potentialMatch :
        return BinarySearchHelper(array, target, left, middle -1)
    else:
        return BinarySearchHelper(array, target, middle +1, right)
        
        
#array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#print(BinarySearch(array, 10))