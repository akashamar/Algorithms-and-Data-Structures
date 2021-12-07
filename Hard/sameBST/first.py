# O(n^2) time | O(n^2) space
def sameBst(array1, array2):
	isSameBst = traverseBst(array1, array2)
	return isSameBst

def traverseBst(array1, array2):
	if len(array1) == 0 and len(array2) == 0:
		return True
	if array1[0] == array2[0] and len(array1) == len(array2):
		rootNode = array1[0]
		array1LeftBranch, array1RightBranch = [], []
		array2LeftBranch, array2RightBranch = [], []
		for i in range(1, len(array1)):
			if array1[i] < rootNode:
				array1LeftBranch.append(array1[i])
			else:
				array1RightBranch.append(array1[i])
			if array2[i] < rootNode:
				array2LeftBranch.append(array2[i])
			else:
				array2RightBranch.append(array2[i])
		return traverseBst(array1RightBranch, array2RightBranch) and traverseBst(array1LeftBranch, array2LeftBranch)
	else:
		return False

array1 = [10,15,8,12,94,81,5,2,11]
array2 = [10,8,5,15,2,12,11,94,81]
print(sameBst(array1, array2))