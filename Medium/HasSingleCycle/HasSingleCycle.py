#O(n) time | O(1) space
def HasSingleCycle(arr):
    noVisitedIdx = 0
    currentIdx = 0
    while noVisitedIdx < len(arr):
        if noVisitedIdx > 0 and currentIdx == 0:
            return False
        noVisitedIdx += 1
        currentIdx = FindNextIdx(currentIdx, arr)
    return currentIdx == 0
    
def FindNextIdx(idx, arr):
    jump = arr[idx]
    nextIdx = (jump + idx) % len(arr)
    return nextIdx if nextIdx >= 0 else nextIdx + len(arr)
    
arr = [2, 3, 1, -4, -4, 2]
print(HasSingleCycle(arr))