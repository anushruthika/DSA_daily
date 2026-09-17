# 123. Best Time to Buy and Sell Stock III

class Solution:
    # def maxProfit(self, prices: list[int]) -> int:
    #     # transNo : 
    #     # k = 2 transNo = 2*k = 4 means,
    #     # k%2 == 0 -> buy else sell
    #     k = 2
    #     n = len(prices)
    #     def rec(ind,transNo):
    #         if ind == n or transNo==2*k:
    #             return 0
    #         if transNo%2 == 0:
    #             return max(-prices[ind]+rec(ind+1,transNo+1),rec(ind+1,transNo))
    #         else:
    #             return max(prices[ind]+rec(ind+1,transNo+1),rec(ind+1,transNo))
    #     return rec(0,0)
    # def maxProfit(self, prices: list[int]) -> int:
    #     # transNo : 
    #     # k = 2 transNo = 2*k = 4 means,
    #     # k%2 == 0 -> buy else sell
    #     k = 2
    #     n = len(prices)
    #     DP = [[-1]*(2*k) for _ in range(n)]
    #     def rec(ind,transNo):
    #         if ind == n or transNo==2*k:
    #             return 0
    #         if DP[ind][transNo] !=-1:
    #             return DP[ind][transNo]
    #         if transNo%2 == 0:
    #             DP[ind][transNo] = max(-prices[ind]+rec(ind+1,transNo+1),rec(ind+1,transNo))
    #             return DP[ind][transNo]
    #         else:
    #             DP[ind][transNo]= max(prices[ind]+rec(ind+1,transNo+1),rec(ind+1,transNo))
    #             return DP[ind][transNo]
    #     return rec(0,0)
    # def maxProfit(self, prices: list[int]) -> int:
    #     # transNo : 
    #     # k = 2 transNo = 2*k = 4 means,
    #     # k%2 == 0 -> buy else sell
    #     k = 2
    #     n = len(prices)
    #     DP = [[0]*(2*k+1) for _ in range(n+1)]
    #     for ind in range(n-1,-1,-1):
    #         for transNo in range(2*k):
    #             # buy
    #             if transNo%2 == 0:
    #                 DP[ind][transNo] = max(-prices[ind]+DP[ind+1][transNo+1],DP[ind+1][transNo])
    #             else:
    #                 DP[ind][transNo] = max(prices[ind]+DP[ind+1][transNo+1],DP[ind+1][transNo])
    #     max_ = 0
    #     # max can be while doing only 1 sell so need to loop
    #     # eg: k = 2 max(DP[0][0],DP[0][2],DP[0][4])
    #     for i in range(0,2*k,2):
    #         max_ = max(max_,DP[0][i])
    #     return max_

    # Space optimized
    def maxProfit(self, prices: list[int]) -> int:
        # transNo : 
        # k = 2 transNo = 2*k = 4 means,
        # k%2 == 0 -> buy else sell
        k = 2
        n = len(prices)
        DP = [0]*(2*k+1)
        for ind in range(n-1,-1,-1):
            newDP = [0]*(2*k+1)
            for transNo in range(2*k):
                # buy
                if transNo%2 == 0:
                    newDP[transNo] = max(-prices[ind]+DP[transNo+1],DP[transNo])
                else:
                    newDP[transNo] = max(prices[ind]+DP[transNo+1],DP[transNo])
            DP = newDP
        max_ = 0
        for i in range(0,2*k,2):
            max_ = max(max_,DP[i])
        return max_
