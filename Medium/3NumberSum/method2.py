#O(n^2) time | O(n) space
def ThreeNumSum(arr, ts):
    arr.sort()
    triplets = []
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            currentSum = arr[i] + arr[left] + arr[right]
            if currentSum == ts:
                triplets.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
            elif currentSum > ts:
                right -= 1
            elif currentSum < ts:
                left += 1
    return triplets
                
              
arr = [2, 4, 6, 8, 10]
ts = 18   #target sum
print(ThreeNumSum(arr, ts))