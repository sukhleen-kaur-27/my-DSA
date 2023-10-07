def bestTimeToBuyAndSellStock(prices: [int]) -> int:
    # Write your code here.
    max_profit = 0
    for i in range(len(prices)-1, -1,-1):
        for j in range(i-1, -1,-1):
            profit = prices[i]-prices[j]
            max_profit = max(max_profit, profit)
    return max_profit