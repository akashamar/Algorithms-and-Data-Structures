# O(n^3) time | O(n) space
def ThreeNumSum(arr, ts):
    arr.sort()
    triplets = []
    for i in range(len(arr)):
        first = arr[i]
        for j in range(len(arr)):
            if j != i :
                second = arr[j]
                for k in range(len(arr)):
                    if k != i and k != j:
                        third = arr[k]
                        sum = first+ second + third
                        if sum == ts:
                            if [third, first, second] in triplets or [third, second, first] in triplets or [second, third, first] in triplets or [second, first, third] in triplets or [first, third, second] in triplets:       # to avoide the duplicate of arrays
                                break
                            else:
                                triplets.append([first, second, third])
    return triplets
                
              
arr = [2, 4, 6, 8, 10]  
ts = 18   #target sum
print(ThreeNumSum(arr, ts))