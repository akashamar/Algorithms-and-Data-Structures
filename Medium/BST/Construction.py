class BST:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        
    # Average: O(log(n)) times | O(1) space
    # Worst: O(n) times | O(1) space
    def insert(self, value):
        currentNode = self
        while True:
            if currentNode.value:
                if value < currentNode.value:
                    if currentNode.left is None:
                        currentNode.left = BST(value)
                        break
                    else:
                        currentNode = currentNode.left
                else:
                    if currentNode.right is None:
                        currentNode.right = BST(value)
                        break
                    else:
                        currentNode = currentNode.right
            else:
                currentNode.value = value
                
    # Average: O(log(n)) times | O(1) space
    # Worst: O(n) times | O(1) space
    def search(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False
        
    # Average: O(log(n)) times | O(1) space
    # Worst: O(n) times | O(1) space         
    def remove(self, value, parentNode = None):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinVal()
                    currentNode.right.remove(currentNode.value, currentNode)
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        currentNode.value = None
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.right if currentNode.right is not None else currentNode.left
                break
        return self
        
    def getMinVal(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value
                
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.value)
        if self.right:
            self.right.printTree()
            
root = BST(10)
root.insert(4)
root.insert(2)
root.insert(9)
root.insert(12)
root.insert(3)
root.insert(1)
root.insert(13)
print(root.search(12))
root.remove(3)
root.remove(10)

root.printTree()