# O(n^2) time | O(n) space
def minReward(array):
	rewards = [1 for _ in array]
	for i in range(1, len(array)):
		j = i - 1
		if array[i] > array[j]:
			rewards[i] = rewards[j] + 1
		else:
			while j >= 0 and array[j] > array[j + 1]:
				rewards[j] = max(rewards[j], rewards[j + 1] + 1)
				j -= 1
	print(rewards)
	return sum(rewards)

array = [1,2,4,3,1,7,8,9,5]
print(minReward(array))