# O(n) time | O(n) space
def two_sum(nums, targetNum):
    table = {}
    for num in nums:
        if targetNum - num in table:
            return [targetNum - num, num]
        else:
            table[num] = True
    return []

nums = [3,5,6,8,2,4]

targetNum = 7

print(two_sum(nums, targetNum))
