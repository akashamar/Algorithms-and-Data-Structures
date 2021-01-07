# O(w*n*log(n) + n*w*log(w)) time | O(wn) space
def groupAnagrams(words):
    sortedWords = [''.join(sorted(w)) for w in words]
    indices = [i for i in range(len(words))]
    indices.sort(key = lambda x: sortedWords[x])
    result = []
    currentAnagramGroup = []
    currentAnagram = sortedWords[indices[0]]
    for index in indices:
        word = words[index]
        sortedWord = sortedWords[index]
        if sortedWord == currentAnagram:
            currentAnagramGroup.append(word)
            continue
        result.append(currentAnagramGroup)
        currentAnagramGroup = [word]
        currentAnagram = sortedWord
    result.append(currentAnagramGroup)
    return result

words = ['yo', 'act', 'flop', 'tac', 'cat', 'oy', 'olfp']
print(groupAnagrams(words))