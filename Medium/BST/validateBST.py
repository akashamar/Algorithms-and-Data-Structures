# O(n) times | O(d) space 
# where d is the depth of the tree
def validateBST(tree):
    return validateBST_helper(tree, float('-inf'), float('inf'))
    
def validateBST_helper(tree, min, max):
    if tree is None:
        return True
    if tree.value < min or tree.value >= max:
        return False
    validateLeft = validateBST_helper(tree.left, min, tree.value)
    validateRight = validateBST_helper(tree.right, tree.value, max)
    return validateLeft and validateRight

