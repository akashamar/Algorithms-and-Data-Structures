# O(n^2) times | O(1) space
def SmallestDifference(array1, array2):
    SD = None           #smallestDifference
    nums = None
    for num1 in array1:
        for num2 in array2:
            difference = abs(num1 - num2)
            if SD is None:
                SD = difference
            elif difference < SD:
                SD = difference
                nums = [num1, num2]
    return nums, SD


array1 = [0, -3, 9, 8, 6]
array2 = [4, -5, 3, 5, 1, 9]
print(SmallestDifference(array1, array2))