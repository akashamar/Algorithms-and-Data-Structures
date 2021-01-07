# O(n) time | O(d) space
# n = total number of elements eg.{5} if [1,2,[7,6],4,[0,4]]
# d = no of depth of the array
def productSum(array, multiplier = 1):
    sum = 0
    for element in array :
        if type(element) is list :
            return productSum(element, multiplier + 1)
        else :
            sum += element
    return sum * multiplier
    
#array = [5, 1, [7, -1], 3, [6, [-13, 8], 4]]
#print(productSum(array))