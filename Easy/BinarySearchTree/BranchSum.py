class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        
# O(n) time | O(n) space
def branchSums(root):
    sums = []
    claculateBranchSums(root, 0, sums)
    return sums
    
def claculateBranchSums(node, runningSum, sums):
    if node is None:
        return
        
    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return
        
    claculateBranchSums(node.left, newRunningSum, sums)
    claculateBranchSums(node.right, newRunningSum, sums)
    