# O(2 ^ n) time | O(n) space
def getNthFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return getNthFib(n - 1) + getNthFib(n - 2)
    
#print(getNthFib(8))