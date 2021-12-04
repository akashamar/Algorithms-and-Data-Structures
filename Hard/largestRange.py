# O(n) time | O(n) space
def largestRange(array):
	largestRange = []
	hashTable = {}
	for num in array:
		if num not in hashTable:
			hashTable[num] = True
		if hashTable[num]:
			newRange = [num]
			leftNum = num - 1
			while leftNum in hashTable:
				newRange.insert(0, leftNum)
				hashTable[leftNum] = False
				leftNum -= 1
			rightNum = num + 1
			while rightNum in hashTable:
				newRange.append(rightNum)
				hashTable[rightNum] = False
				rightNum += 1
			if len(newRange) > len(largestRange):
				largestRange = newRange
	return [largestRange[0],largestRange[-1]]


array = [1,11,3,0,15,5,2,4,10,7,12,6]
print(largestRange(array))