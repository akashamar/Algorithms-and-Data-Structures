def subArraySort(array):
	minOutOFOrder = float("inf")
	maxOutOfOrder = float("-inf")
	for i in range(len(array)):
		num = array[i]
		if isOutOfOrder(i, num, array):
			minOutOFOrder = min(minOutOFOrder, num)
			maxOutOfOrder = max(maxOutOfOrder, num)
	if minOutOFOrder == float("inf"):
		return [1, -1]
	subarrayLeftIdx = 0
	while minOutOFOrder >= array[subarrayLeftIdx]:
		subarrayLeftIdx += 1
	subarrayRightIdx = len(array) - 1
	while maxOutOfOrder <= array[subarrayRightIdx]:
		subarrayRightIdx -= 1
	return [subarrayLeftIdx, subarrayRightIdx]

def isOutOfOrder(i, num, array):
	if i == 0:
		return num > array[i + 1]
	if i == len(array) - 1:
		return num < array[i -1]
	return num < array[i - 1] or num > array[i + 1]

array = [1,2,3,8,9,6,12,11,13,14]
print(subArraySort(array))