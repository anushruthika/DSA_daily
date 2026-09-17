# 121. Best Time to Buy and Sell Stock

# buy/sell only once within the window

# decreasing sells. maximum you can buy and sell on same day
# [7,6,5,4,3,2] ans = 0
# buy and sell on same day
# [1] ans = 0

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # min profit is zero. ,because buy and sell on same day
        ans_profit = 0
        mini = prices[0]
        n = len(prices)
        for i in range(1,n):
            if mini<prices[i]:
                ans_profit = max(prices[i]-mini,ans_profit)
            else:
                mini = prices[i]
        return ans_profit

            

