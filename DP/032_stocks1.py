# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans_profit = 0
        mini = prices[0]
        n = len(prices)
        for i in range(1,n):
            if mini<prices[i]:
                ans_profit = max(prices[i]-mini,ans_profit)
            else:
                mini = prices[i]
        return ans_profit

            

