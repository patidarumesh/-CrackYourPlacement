def maxProfit( prices):
        size = len(prices)
        buy_stock = prices[0]
        profit = 0
        for i in range(size-1):
            if prices[i+1]>buy_stock:
                profit = max(profit, prices[i+1]-buy_stock)
            else:
                buy_stock = prices[i+1]
        return profit

list = [5,3,56,7,8,6,5]
print(maxProfit(list))
