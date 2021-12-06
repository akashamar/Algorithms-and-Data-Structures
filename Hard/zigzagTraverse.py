# O(n) time | O(n) space
def zigzagTraverse(array):
	height = len(array) - 1
	width = len(array[0]) - 1
	result = []
	row, col = 0, 0
	goingDown = True
	while not isOutOfBound(row, col, height, width):
		result.append(array[row][col])
		if goingDown:
			if col == 0 or row == height:
				goingDown = False
				if row == height:
					col += 1
				else:
					row += 1
			else:
				row += 1
				col -= 1
		else:
			if row == 0 or col == width:
				goingDown = True
				if col == width:
					row += 1
				else:
					col += 1
			else:
				row -= 1
				col += 1
	return result

def isOutOfBound(row, col, height, width):
	return row < 0 or row > height or col < 0 or col > width 

array = [
	[1,3,4,10,11],
	[2,5,9,12,19],
	[6,8,13,18,20],
	[7,14,17,21,24],
	[15,16,22,23,25]
]
print(zigzagTraverse(array))