class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data
		
	def insert(self, data):
		if self.data:
			if data < self.data:
				if self.left is None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			elif data > self.data:
				if self.right is None:
					self.right = Node(data)
				else:
					self.right.insert(data)
		else:
			self.data = data

    # O(n) time | O(log(n)) space
	def maxPathSum(self):
		_, maxSum = self.findMaxSum()
		return maxSum

	def findMaxSum(self):
		if self.left == None:
			LBS, LS = 0, 0
		else:
			LBS, LS = self.left.findMaxSum()
		if self.right == None:
			RBS, RS = 0, 0
		else:
			RBS, RS = self.right.findMaxSum()
		MCSB = max(LBS, RBS)
		MSB = max(MCSB + self.data, self.data)
		MST = max(MSB, LBS + self.data + RBS)
		RMPS = max(LS, RS, MST)
		return (MSB, RMPS)
		
	def printTree(self):
		if self.left:
			self.left.printTree()
		print(self.data),
		if self.right:
			self.right.printTree()
            
            
root = Node(10)
root.insert(4)
root.insert(2)
root.insert(9)
root.insert(12)
root.insert(3)
root.insert(1)
root.insert(13)

# root.printTree()
print(root.maxPathSum())