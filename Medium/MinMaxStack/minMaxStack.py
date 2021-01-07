class minMaxStack:
    def __init__(self):
        self.minMaxStack = []
        self.stack = []
        
    # O(1) time | O(1) space
    def peek(self):
        return self.stack[len(self.stack) - 1]
        
    # O(1) time | O(1) space
    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()
        
    # O(1) time | O(1) space  
    def push(self, number):
        newMinMax = {'min' : number, 'max' : number}
        if len(self.minMaxStack):
            lasMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
            newMinMax['min'] = min(lasMinMax['min'], number)
            newMinMax['max'] = max(lasMinMax['max'], number)
        self.minMaxStack.append(newMinMax)
        self.stack.append(number)
        
    # O(1) time | O(1) space
    def getMin(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]['min']
        
    # O(1) time | O(1) space
    def getMax(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]['max']
        
        
stack = minMaxStack()
stack.push(2)
stack.push(4)
stack.push(10)
stack.push(3)
stack.push(8)
stack.pop()
print(stack.getMin())
print(stack.getMax())
print(stack.peek())