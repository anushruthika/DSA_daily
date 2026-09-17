# 309. Best Time to Buy and Sell Stock with Cooldown

# recursion
# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         n = len(prices)
#         def rec(ind,buy):
#             if ind >= n:
#                 return 0
#             if buy:
#                 return max(-prices[ind]+rec(ind+1,False),rec(ind+1,True))
#             else:
#                 return max(prices[ind]+rec(ind+2,True),rec(ind+1,False))
#         return rec(0,True)

# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         n = len(prices)
#         DP = [[-1]*2 for _ in range(n)]
#         def rec(ind,buy):
#             if ind >= n:
#                 return 0
#             if DP[ind][buy]!=-1:
#                 return DP[ind][buy]
#             if buy:
#                 DP[ind][buy] = max(-prices[ind]+rec(ind+1,0),rec(ind+1,1))
#                 return DP[ind][buy]
#             else:
#                 DP[ind][buy] = max(prices[ind]+rec(ind+2,1),rec(ind+1,0))
#                 return DP[ind][buy]
#         return rec(0,True)
            
# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         n = len(prices)
#         DP = [[0]*2 for _ in range(n+2)]
#         for ind in range(n-1,-1,-1):
#             DP[ind][1] = max(DP[ind+1][1],-prices[ind]+DP[ind+1][0])
#             DP[ind][0] = max(DP[ind+1][0],prices[ind]+DP[ind+2][1])
#         return DP[0][1]
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        DP = [[0]*2 for i in range(2)]
        
        for ind in range(n-1,-1,-1):
            newDP = [0]*2
            newDP[1] = max(DP[0][1],-prices[ind]+DP[0][0])
            newDP[0] = max(DP[0][0],prices[ind]+DP[1][1])
            DP[1] = DP[0]
            DP[0] = newDP
        return DP[0][1]
            
