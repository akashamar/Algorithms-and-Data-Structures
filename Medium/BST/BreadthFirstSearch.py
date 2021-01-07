# O(v + e) time | O(v) space
# v => vertises(Node) and e => edges(/,\)
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name
        
    def addChild(self, name):
        self.children.append(Node(name))
        
    def breadthFirstSearch(self, arr=[]):
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            arr.append(current.name)
            for child in current.children:
                queue.append(child)
        return arr