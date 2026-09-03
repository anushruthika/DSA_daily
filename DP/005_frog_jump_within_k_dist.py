# https://www.naukri.com/code360/problems/minimal-cost_8180930
# formula: 
# DP[index] = jump:1->k given=> jump<index min( DP[index-jump] + abs(heights[index-jump] - heights[index]) )


from typing import *
# | Approach                |        TC |       SC |
# | ----------------------- | --------: | -------: |
# | Plain recursion         | **O(k?)** | **O(n)** |
# | Recursion + Memoization | **O(nk)** | **O(n)** |
# | Bottom-up DP            | **O(nk)** | **O(n)** |
# | Space-optimized DP      | **O(nk)** | **O(k)** |

# recursion
# O(k^(n)):
# n~10**4 and k~100 100**10**4 >>>>>> 10**9 therefore TLE

# eg:
# n = 4
# k = 2
# heights = [10, 40, 30, 10]
#                          rec(3)
#                        /        \
#                   jump 1       jump 2
#                     /             \
#                  rec(2)          rec(1)
#                 /     \          /    \
#            jump 1   jump 2   jump 1  (jump 2)
#               /        \        /       \
#            rec(1)     rec(0)  rec(0)   invalid
#              / \         |       |
#             /   \        0       0
#         rec(0) rec(-1)
#            |      |
#            0      0
#  TAbulation
#  minimum  40-10 = 30 DP[0] = 0 DP[1] = 30
# minimum DP[2] = minimum (DP[0]+arr[2]-arr[0] or DP[1]+arr[2]-arr[1])
# 
# Recursion Logic 1
# def minimizeCost(n : int, k : int, heights : List[int]) -> int:
#     def rec(index):
#         if index<=0:
#             return 0
#         list_values = []
#         for jump in range(1,min(k, index) + 1):
#             list_values.append(rec(index-jump)+abs(heights[index]-heights[index-jump]))
#         return min(list_values)
#     return rec(n-1)

# recursion logic 2
# def minimizeCost(n : int, k : int, heights : List[int]) -> int:
#     def rec(index):
#         if index<=0:
#             return 0
#         min_tracker = float('inf')
#         for jump in range(1,min(k, index) + 1):
#             val = rec(index-jump)+abs(heights[index]-heights[index-jump])
#             if min_tracker>val:
#                 min_tracker = val
#         return min_tracker
#     return rec(n-1)

# TC: O(n*k)
# SC: O(n) - DP array recursion stack
# def minimizeCost(n : int, k : int, heights : List[int]) -> int:
#     DP = [-1]*n
#     def rec(index):
#         if index<=0:
#             return 0
#         min_tracker = float('inf')
#         for jump in range(1,min(k, index) + 1):
#             if DP[index-jump] == -1:
#                 DP[index-jump] = rec(index-jump)
#             val = DP[index-jump] +abs(heights[index]-heights[index-jump])
#             if min_tracker>val:
#                 min_tracker = val
#         DP[index] = min_tracker
#         return min_tracker
#     return rec(n-1)

# Tabulation
# minimum  40-10 = 30 DP[0] = 0 DP[1] = 30
# minimum DP[2] = minimum (DP[0]+arr[2]-arr[0] or DP[1]+arr[2]-arr[1])
# def minimizeCost(n : int, k : int, heights : List[int]) -> int:
#     if n <=1:
#         return 0
#     DP = [float('inf')]*n
#     DP[0] = 0
#     DP[1] = abs(heights[0]-heights[1])
#     if n == 2:
#         return DP[1]
#     for index in range(2,n): 
#         for jump in range(1,k+1):
#             compute = DP[index-jump]+abs(heights[index]-heights[index-jump])
#             if DP[index]>compute:
#                 DP[index] = compute
#     return DP[n-1]



# Space optimized : 
def minimizeCost(n: int, k: int, heights: List[int]) -> int:
    if n <= 1:
        return 0

    dp = [float('inf')] * k
    dp[0] = 0

    for i in range(1, n):
        curr = float('inf')

        for j in range(max(0, i - k), i):
            curr = min(
                curr,
                dp[j % k] + abs(heights[i] - heights[j])
            )

        dp[i % k] = curr

    return dp[(n - 1) % k]


