# O(n) times | O(n) space
def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array
    
def preOrderTraverse(tree, array):
    if tree is not None:
        array.append(tree.value)
        inOrderTraverse(tree.left, array)
        inOrderTraverse(tree.right, array)
    return array
    
def postOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        inOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array