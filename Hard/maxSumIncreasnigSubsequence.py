# O(n^2) time | O(n) space
def maxSumIncreasnigSubsequence(array):
	sums = array[:]
	sequences = [None for _ in array]
	highestSumIdx = 0
	for i in range(len(array)):
		for j in range(0, i):
			if array[j] < array[i] and sums[j] + array[i] >= sums[i]:
				sums[i] = sums[j] + array[i]
				sequences[i] = j
		if sums[i] >= sums[highestSumIdx]:
			highestSumIdx = i

	subSequence = []
	idx = highestSumIdx
	while idx is not None:
		subSequence.insert(0, array[idx])
		idx = sequences[idx]
	print(sums[highestSumIdx], subSequence)

array = [8, 12, 2, 3, 15, 5, 7]
maxSumIncreasnigSubsequence(array)