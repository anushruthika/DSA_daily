# 714. Best Time to Buy and Sell Stock with Transaction Fee

class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        n = len(prices)
        DP = [0]*2
        for i in range(n-1,-1,-1):
            newDP = [0]*2
            newDP[1] = max(DP[1],-prices[i]-fee+DP[0])     
            newDP[0] = max(DP[0],prices[i]+DP[1])
            DP = newDP
        return DP[1]
