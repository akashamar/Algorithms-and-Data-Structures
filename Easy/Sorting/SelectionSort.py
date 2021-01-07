def sort(nums):
    for i in range(len(nums)):
        minPos = i
        for j in range(i, len(nums)):
            if nums[j] < nums[minPos]:
                minPos = j
                
        temp = nums[i]
        nums[i] = nums[minPos]
        nums[minPos] = temp
        
    

nums = [62, 41, 93, 19, 71, 2, 1, 8, 88, 9]
sort(nums)

print(nums)