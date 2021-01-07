# O(n^2) time | O(1) space
def two_sum(nums, targetNum):
    for i in range(len(nums) - 1):
        firstNum = nums[i]
        for j in range(i+1, len(nums)):
            secondNum = nums[j]
            if firstNum + secondNum == targetNum:
                return [firstNum, secondNum]
                
    return[]
            

nums = [3,5,6,8,2,4]
targetNum = 7
print(two_sum(nums, targetNum))
