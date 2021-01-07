class MinHeap:
    def __init__(self, array):
        self.heap = self.BuildHeap(array)
        
    def BuildHeap(self, array):
        firstParentIdx = (len(array) - 2 + 1) // 2
        for currentIdx in reversed(range(firstParentIdx)):
            self.shiftDown(currentIdx, len(array) - 1, array)
        return array
        
    def shiftDown(self, currentIdx, endIdx, heap):
        childIdxOne = currentIdx * 2 + 1
        while childIdxOne <= endIdx:
            childIdxTwo = currentIdx * 2 + 2 if currentIdx * 2 + 1 <= endIdx else -1
            if childIdxTwo != -1 and heap[childIdxTwo] < heap[childIdxOne]:
                indexToSwap = childIdxTwo
            else:
                indexToSwap = childIdxOne
            if heap[indexToSwap] < heap[currentIdx]:
                self.swap(currentIdx, indexToSwap, heap)
                currentIdx = indexToSwap
                childIdxOne = currentIdx * 2 + 1
            else:
                break
            
    def shiftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(currentIdx, parentIdx, self.heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2
        
    def peek(self):
        return self.heap[0]
        
    def insert(self, value):
        self.heap.append(value)
        self.shiftUp(len(self.heap) - 1, self.heap)
        
    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.shiftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove
        
    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
        
    def printHeap(self):
        print(self.heap)
        
array = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
heap = MinHeap(array)
heap.remove()
heap.insert(1)
heap.printHeap()
print(heap.peek())
