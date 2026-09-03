# https://www.geeksforgeeks.org/problems/geek-jump/1 


# | Approach        | Time      | Space                                 |
# | --------------- | --------- | ------------------------------------- |
# | Recursion       | **O(2ⁿ)** | **O(n)**                              |
# | Memoization     | **O(n)**  | **O(n)** (DP array + recursion stack) |
# | Tabulation      | **O(n)**  | **O(n)**                              |
# | Space Optimized | **O(n)**  | **O(1)**                              |


# DP[n] = min( DP[n-1]+abs(height[n],height[n-1]) , DP[n-2]+abs(height[n],height[n-2])  )

# edge case :
# heights = [10] op = 0
# heights = [] op = invalid case

# Recursion

# class Solution:
#     def minCost(self, height: list[int]) -> int:
#         if len(height) == 0:
#             return -1 
#         def fib(ind):
#             if ind == 0:
#                 return 0
#             left = fib(ind-1)+abs(height[ind]-height[ind-1])
#             if ind==1:
#                 return left
#             right = fib(ind-2)+abs(height[ind]-height[ind-2])
#             return min(right,left)
#         return fib(len(height)-1)
        
# Memoization
# Index :    0    1    2    3
# Height:   20   30   40   20
# DP    :    0   10   20   20

# class Solution:
#     def minCost(self, height: list[int]) -> int:
#         n = len(height)
#         DP = [-1]*n
#         if len(height) == 0:
#             return -1 
#         def fib(ind):
#             if ind == 0:
#                 return 0
#             sub_left = DP[ind-1]
#             if DP[ind-1]==-1:
#                 sub_left = fib(ind-1)
#             left = sub_left+abs(height[ind]-height[ind-1])
#             if ind==1:
#                 return left
#             sub_right = DP[ind-2]
#             if DP[ind-2]==-1:
#                 sub_right = fib(ind-2)
#             right = sub_right+abs(height[ind]-height[ind-2])
#             DP[ind] = min(right,left)
#             return DP[ind]
#         return fib(n-1)

#  Tabularization
# class Solution:
#     def minCost(self, height: list[int]) -> int:
#         n = len(height)
#         DP = [-1]*n
#         DP[0] = 0
#         if len(height) == 0:
#             return -1 
#         for i in range(1,n):
#             left = DP[i-1]+abs(height[i-1]-height[i])
#             right = float('inf')
#             if i>1:
#                 right = DP[i-2]+abs(height[i-2]-height[i])
#             DP[i] = min(left,right)
#         return DP[n-1]
        
#  space complexity
class Solution:
    def minCost(self, height: list[int]) -> int:
        n = len(height)
        if len(height) == 0:
            return -1 
        if len(height) == 1:
            return 0
        prev1 = 0
        prev2 = abs(height[1]-height[0])
        
        for i in range(2,n):
            left = prev2+abs(height[i-1]-height[i])
            right = prev1+abs(height[i-2]-height[i])
            cur = min(left,right)
            prev1 = prev2
            prev2 = cur
        return prev2
            
