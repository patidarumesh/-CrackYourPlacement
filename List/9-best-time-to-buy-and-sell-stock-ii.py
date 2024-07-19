def maxProfit( prices) -> int:
    buy = float('inf')
    profit = 0
    for i in range(len(prices)-1):
        buy = min(buy, prices[i])
        if(prices[i+1] >buy):
            profit += prices[i+1] - buy
            buy = prices[i+1]
            i +=1
    
    return profit

prices = [7,1,5,3,6,4]

print(maxProfit(prices))
