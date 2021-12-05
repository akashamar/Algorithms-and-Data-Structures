# O(n) time | O(n) space
def minReward(array):
	localMinsIdx = getLocalMinsIdx(array)
	rewards = [1 for _ in array]
	for localMinIdx in localMinsIdx:
		expandFromLocalMinIdx(localMinIdx, array, rewards)
	print(rewards)
	return sum(rewards)

def expandFromLocalMinIdx(localMinIdx, array, rewards):
	leftIdx = localMinIdx - 1
	while leftIdx >= 0 and array[leftIdx] > array[leftIdx + 1]:
		rewards[leftIdx] = max(rewards[leftIdx], rewards[leftIdx + 1] + 1)
		leftIdx -= 1
	rightIdx = localMinIdx + 1
	while rightIdx < len(array) and array[rightIdx] > array[rightIdx - 1]:
		rewards[rightIdx] = max(rewards[rightIdx], rewards[rightIdx - 1] + 1)
		rightIdx += 1

def getLocalMinsIdx(array):
	if len(array) == 1:
		return [0]
	localMinsIdx = []
	for i in range(len(array)):
		if i == 0 and array[i] < array[i + 1]:
			localMinsIdx.append(i)
		elif i == len(array) - 1 and array[i] < array[i - 1]:
			localMinsIdx.append(i)
		elif array[i] < array[i - 1] and array[i] < array[i + 1]:
			localMinsIdx.append(i)
	return localMinsIdx

array = [1,2,4,3,1,7,8,9,5]
print(minReward(array))