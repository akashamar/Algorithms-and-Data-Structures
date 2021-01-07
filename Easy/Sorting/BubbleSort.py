def sort(nums) :
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1] :
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

nums = [84, 42, 53, 74, 82, 18, 19, 30, 93]
sort(nums)

print(nums)
