# O(n^2*n!) time | O(n*n!) space
def getPermutations(array):
    permutations = []
    permutationHelper(array, [], permutations)
    return permutations
    
def permutationHelper(array, currentPermutations, permutations):
    if not len(array) and len(currentPermutations):
        permutations.append(currentPermutations)
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i + 1:]
            newPermutation = currentPermutations + [array[i]]
            permutationHelper(newArray, newPermutation, permutations)
            
array = [1, 2, 3]
print(getPermutations(array))