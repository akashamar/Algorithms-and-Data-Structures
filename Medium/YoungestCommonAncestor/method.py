# O(d) time | O(1) space
# where d is the max depth of the two decendants
def findYoungestCommonAncestor(topAncestor, descendantOne, decendantTwo):
    depthOne = getDepthOfTheDescendant(descendantOne, topAncestor)
    depthTwo = getDepthOfTheDescendant(descendantTwo, topAncestor)
    if depthOne > depthTwo:
        return getTheLevelOfAncestor(descendantOne, descendantTwo, depthOne - depthTwo)
    else:
        return getTheLevelOfAncestor(descendantTwo, descendantOne, depthTwo - depthOne)
    
def getDepthOfTheDescendant(decendant, topAncestor):
    depth = 0
    while decendant =! topAncestor:
        decendant = decendant.ancestor
        depth += 1
    return depth
    
def getTheLevelOfAncestor(higherDecendant, lowerDecendant, depth):
    while depth != 0:
        higherDecendant = higherDecendant.ancestor
        depth -= 1
    while higherDecendant != lowerDecendant:
        higherDecendant = higherDecendant.ancestor
        lowerDecendant = lowerDecendant.ancestor
    return higherDecendant