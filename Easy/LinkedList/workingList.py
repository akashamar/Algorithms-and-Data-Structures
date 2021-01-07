class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def setHead(self, node):
        newNode = Node(node)
        if self.head is None:
            self.head = newNode
            self.head.next = None
            self.head.prev = None
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
            self.head.prev = None
            
    def setTail(self, node):
        newNode = Node(node)
        if self.head is None:
            self.setHead(node)
        elif self.tail is None:
            self.tail = newNode
            self.tail.next = None
            if self.head.next is None:
                self.tail.prev = self.head
                self.head.next = self.tail
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            self.tail.next = None
        
    def insertAfter(self, prev_node, node):
        self.remove(node)
        newNode = Node(node)
        current = self.head
        while current is not None:
            if current.data == prev_node.data:
                newPrevNode = current
                if newPrevNode.next is None:
                    self.setTail(node)
                else:
                    newNode.prev = newPrevNode
                    newNode.next = newPrevNode.next
                    newPrevNode.next.prev = newNode
                    newPrevNode.next = newNode
                break
            else:
                if current.next is None:
                    print('Given Node is Not Found in Linked_List')
                    break
                else:
                    current = current.next
            
    def insertBefore(self, aft_node, node):
        self.remove(node)
        newNode = Node(node)
        current = self.head
        while current is not None:
            if current.data == aft_node.data:
                newBefNode = current
                if newBefNode.prev is None:
                    self.setHead(node)
                else:
                    newNode.next = newBefNode
                    newNode.prev = newBefNode.prev
                    newBefNode.prev.next = newNode
                    newBefNode.prev = newNode
                break
            else:
                if current.next is None:
                    print('Given Node is Not Found in Linked_List')
                    break
                else:
                    current = current.next
            
    def insertAtPosition(self, position, nodeToInsert):
        self.remove(nodeToInsert)
        newNode = Node(nodeToInsert)
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)
            
    def remove(self, node):
        current = self.head
        while current is not None:
            if current.data == node:
                remNode = current
                if remNode.prev is None:
                    self.head = remNode.next
                    remNode.next.prev = None
                    remNode.next = None
                elif remNode.next is None:
                    self.tail = remNode.prev
                    remNode.prev.next = None
                    remNode.prev = None
                else:
                    remNode.prev.next = remNode.next
                    remNode.next.prev = remNode.prev
                    remNode.next = None
                    remNode.prev = None
                break
            else:
                if current.next is None:
                    print('Given Node is Not Found in Linked_List')
                    break
                else:
                    current = current.next
                    
    def search(self, node):
        current = self.head
        while node is not None:
            if current.data == node.data:
                print('Node found Successful')
                break
            else:
                if current.next is None:
                    print('Given Node is Not Found in Linked_List')
                    break
                else:
                    current = current.next
                    
    def printList(self):
        current = self.head
        print('head',self.head.data)
        print('tail',self.tail.data)
        while current is not None:
            print(current.data)
            current = current.next
            

root = LinkedList()
root.setHead(6)
root.setTail(7)
root.setTail(8)
root.setTail(9)
root.setTail(10)
root.setHead(5)
root.setHead(4)
root.setHead(3)
root.setHead(2)
root.setHead(1)
root.insertBefore(Node(4), 20)
root.insertAfter(Node(5), 3)
root.remove(Node(5))
root.insertAtPosition(6, 30)
root.search(Node(5))
root.printList()