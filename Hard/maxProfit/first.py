# O(nk) time | O(nk) space 
def maxProfitWithKTransactions(prices, k):
    table = [[0 for i in range(len(prices))] for j in range(k+1) ]
    if not len(prices):
        return 0
    for row in range(1, k+1):
        maxProfitAtPrevRow = float('-inf')
        for col in range(1, len(prices)):
            maxProfitAtPrevRow = max(maxProfitAtPrevRow, table[row - 1][col - 1] - prices[col - 1])
            table[row][col] = max(table[row][col - 1], prices[col] + maxProfitAtPrevRow)
    return table[-1][-1]

prices = [5, 11, 3, 50, 40, 90]
print(maxProfitWithKTransactions(prices, 2))