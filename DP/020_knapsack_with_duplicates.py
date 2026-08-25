# https://www.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1

# 0/1 Knapsack means: for every item, you have exactly two choices: take & not take: without duplicates


# | Approach             | Time Complexity | Space Complexity |
# | -------------------- | --------------: | ---------------: |
# | **1. Recursion**     |  **O(2^(N+C))** |       **O(N+C)** |
# | **2. Memoization**   |    **O(N × C)** |     **O(N × C)** |
# | **3. 2D Tabulation** |    **O(N × C)** |     **O(N × C)** |
# | **4. 1D Tabulation** |    **O(N × C)** |         **O(C)** |


# class Solution:
#     def knapSack(self, val, wt, capacity):
#         # code here
#         def rec(index,weight):
#             if index == 0:
#                 if wt[index]<=weight:
#                     return (weight//wt[index])*val[index]
#                 return 0
#             not_take = rec(index-1,weight)
#             take = 0
#             if weight>=wt[index]:
#                 take = val[index]+rec(index,weight-wt[index])
#             return max(take,not_take)
#         return rec(len(val)-1,capacity)
# class Solution:
#     def knapSack(self, val, wt, capacity):
#         n = len(val)
#         DP = [[-1]*(capacity+1) for _ in range(n)]
#         def rec(index,weight):
#             if DP[index][weight]!=-1:
#                 return DP[index][weight]
#             if index == 0:
#                 if wt[index]<=weight:
#                     return (weight//wt[index])*val[index]
#                 return 0
#             not_take = rec(index-1,weight)
#             take = 0
#             if weight>=wt[index]:
#                 take = val[index]+rec(index,weight-wt[index])
#             DP[index][weight] = max(take,not_take)
#             return DP[index][weight]
#         return rec(n-1,capacity)

# class Solution:
#     def knapSack(self, val, wt, capacity):
#         n = len(val)
#         DP = [[-1]*(capacity+1) for _ in range(n)]
#         for index in range(n):
#             DP[index][0] = 0
#         for weight in range(1,capacity+1):
#             DP[0][weight] = (weight//wt[0]) * val[0]
#         for index in range(1,n):
#             for weight in range(1,capacity+1):
#                 not_take = DP[index-1][weight]
#                 take = 0
#                 if weight>=wt[index]:
#                     take = val[index]+DP[index][weight-wt[index]]
#                 DP[index][weight] = max(not_take,take)
#         return DP[n-1][capacity]
        
class Solution:
    def knapSack(self, val, wt, capacity):
        n = len(val)
        DP = [-1]*(capacity+1)
        DP[0] = 0
        for weight in range(1,capacity+1):
            DP[weight] = (weight//wt[0]) * val[0]
        for index in range(1,n):
            for weight in range(1,capacity+1):
                not_take = DP[weight]
                take = 0
                if weight>=wt[index]:
                    take = val[index]+DP[weight-wt[index]]
                DP[weight] = max(not_take,take)
        return DP[capacity]
                
                
