def sort(nums):
    length = len(nums)
    if length <= 1:
        return nums
    else:
        pivot = nums.pop()
    
    items_grater = []
    items_lower = []
  
    for j in nums:
        if j < pivot:
            items_lower.append(j)
        else:
            items_grater.append(j)
         
    return sort(items_lower) + [pivot] + sort(items_grater)

nums = [82, 62, 28, 1, 6 , 9, 0 , 3, 5]
sort(nums)

print(sort(nums))