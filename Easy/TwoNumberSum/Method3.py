# O(nLog(n)) time | O(1) space
def two_sum(nums, targetNum):
    nums.sort()
    left = 0
    right = len(nums) - 1
    while left < right:
        currentSum = nums[left] + nums[right]
        if currentSum == targetNum:
            return [nums[left], nums[right]]
        elif currentSum < targetNum:
            left += 1
        elif currentSum > targetNum:
            right -= 1
    return []

nums = [3,5,6,8,2,4]

targetNum = 7

print(two_sum(nums, targetNum))
