# O(n) time | O(n) space
def minReward(array):
	rewards = [1 for _ in array]
	for i in range(1, len(array)):
		if array[i] > array[i - 1]:
			rewards[i] = rewards[i - 1] + 1
	for i in reversed(range(len(array) - 1)):
		if array[i] > array[i + 1]:
			rewards[i] = max(rewards[i], rewards[i + 1] + 1)
	print(rewards)
	return sum(rewards)

array = [1,2,4,3,1,7,8,9,5]
print(minReward(array))