# O(nk) time | O(n) space 
def maxProfitWithKTransactions(prices, k):
    if not len(prices):
        return 0
    oddProfits = [0 for i in range(len(prices))]
    evenProfits = [0 for i in range(len(prices))]
    for row in range(1, k+1):
        if row % 2 == 1:
            currentProfit = oddProfits
            previousProfit = evenProfits
        else:
            currentProfit = evenProfits
            previousProfit = oddProfits
        maxProfitAtPrevRow = float('-inf')
        for col in range(1, len(prices)):
            maxProfitAtPrevRow = max(maxProfitAtPrevRow, previousProfit[col - 1] - prices[col - 1])
            currentProfit[col] = max(currentProfit[col - 1], prices[col] + maxProfitAtPrevRow)
    return currentProfit[-1]


prices = [5, 11, 3, 50, 40, 90]
print(maxProfitWithKTransactions(prices, 2))