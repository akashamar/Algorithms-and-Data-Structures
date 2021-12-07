# O(n^2) time | O(d) space
def sameBst(array1, array2):
	return traverseBst(array1, array2, 0, 0, float("-inf"), float("inf"))

def traverseBst(array1, array2, rootNodeIdx1, rootNodeIdx2, minVal, maxVal):
	if rootNodeIdx1 == -1 or rootNodeIdx2 == -1:
		return rootNodeIdx1 == rootNodeIdx2

	if array1[rootNodeIdx1] != array2[rootNodeIdx2]:
		return False

	leftRootNodeIdxOne = getLeftRootIdx(array1, rootNodeIdx1, minVal)
	leftRootNodeIdxTwo = getLeftRootIdx(array2, rootNodeIdx2, minVal)
	rightRootNodeIdxOne = getRightRootIdx(array1, rootNodeIdx1, maxVal)
	rightRootNodeIdxTwo = getRightRootIdx(array2, rootNodeIdx2, maxVal)

	currentNode = array1[rootNodeIdx1]
	leftAreSame = traverseBst(array1, array2, leftRootNodeIdxOne, leftRootNodeIdxTwo, minVal, currentNode)
	rightAreSame = traverseBst(array1, array2, rightRootNodeIdxOne, rightRootNodeIdxTwo, currentNode, maxVal)
	
	return leftAreSame and rightAreSame

def getLeftRootIdx(array, rootNodeIdx, minVal):
	for i in range(rootNodeIdx + 1, len(array)):
		if array[i] < array[rootNodeIdx] and array[i] >= minVal:
			return i
	return -1

def getRightRootIdx(array, rootNodeIdx, maxVal):
	for i in range(rootNodeIdx + 1, len(array)):
		if array[i] >= array[rootNodeIdx] and array[i] < maxVal:
			return i
	return -1

array1 = [10,15,8,12,94,81,5,2,11]
array2 = [10,8,5,15,2,12,11,94,81]
print(sameBst(array1, array2))