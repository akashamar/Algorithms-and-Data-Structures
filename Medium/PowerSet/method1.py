# O(n*2^n) time | O(n*2^n) space
def powerSet(array):
    subsets = [[]]
    for ele in array:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset + [ele])
    return subsets
    
array = [1, 2, 3]
print(powerSet(array))