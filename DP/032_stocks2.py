# 122. Best Time to Buy and Sell Stock II

# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         n = len(prices)
#         def rec(ind,buybool):
#             if ind==n:
#                 return 0
#             if buybool:
#                 return max(rec(ind+1,True),-prices[ind]+rec(ind+1,False))
#             if not buybool:
#                 return max(rec(ind+1,False),prices[ind]+rec(ind+1,True))
#         return rec(0,True)

# Memoization
# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         n = len(prices)
#         DP = [[-1]*2 for _ in range(n)]
#         def rec(ind,buybool):
#             if ind==n:
#                 return 0
#             if DP[ind][buybool] !=-1:
#                 return DP[ind][buybool]
#             if buybool:
#                 DP[ind][buybool] = max(rec(ind+1,1),-prices[ind]+rec(ind+1,0))
#                 return DP[ind][buybool]
#             if not buybool:
#                 DP[ind][buybool] = max(rec(ind+1,0),prices[ind]+rec(ind+1,1))
#                 return DP[ind][buybool]
#         return rec(0,1)

# # tabulation
# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         n = len(prices)
#         DP = [[0]*2 for _ in range(n+1)]
#         for i in range(n-1,-1,-1):
#             # for j in range(2):
#             # instead
#             # buy
#             DP[i][1] = max(DP[i+1][1],-prices[i]+DP[i+1][0])     
#             # sell
#             DP[i][0] = max(DP[i+1][0],prices[i]+DP[i+1][1])
#         return DP[0][1]
# space optimized
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        DP = [0]*2
        for i in range(n-1,-1,-1):
            newDP = [0]*2
            newDP[1] = max(DP[1],-prices[i]+DP[0])     
            # sell
            newDP[0] = max(DP[0],prices[i]+DP[1])
            DP = newDP
        return DP[1]
        
