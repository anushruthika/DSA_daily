# https://www.geeksforgeeks.org/problems/geeks-training/1

# | Approach                          |     Time Complexity | Space Complexity |
# | --------------------------------- | ------------------: | ---------------: |
# | **1. Plain Recursion**            | **O(m × (m−1)ⁿ⁻¹)** |         **O(n)** |
# | **2. Recursion + Memoization**    |        **O(n × m)** |     **O(n × m)** |
# | **3. Tabulation**                 |       **O(n × m²)** |     **O(n × m)** |
# | **4. Space-optimized Tabulation** |       **O(n × m²)** |         **O(m)** |


# eg: Input: mat[][]= [[1, 2, 5],
#               [3, 1, 1], 
#               [3, 3, 3]]
# Output: 11

# activities A, B, C
# mat =
# Day 0: [1, 2, 5]
# Day 1: [3, 1, 1]
# Day 2: [3, 3, 3]
#                   (Day 0)
#                  rec(0,-1)
#              /       |       \
#           A=1      B=2             C=5
#           /         |                 \
#         rec(1,A)  rec(1,B)            rec(1,C)
#         /    \      /    \            /    \
#      B=1    C=1   A=3   C=1           A=3   B=3
#       /        \    /       \          /       \
#   rec(2,B) rec(2,C) rec(2,A) rec(2,C) rec(2,A) rec(2,B)
#     / \       / \      / \       / \      / \      / \
#   A=3 C=3   A=3 B=3  B=3 C=3   A=3 B=3  B=3 C=3  A=3 C=3

#  TLE: 
# tot_days = n and tot_acti = m

# given tree: depth of n and breadth of m (1st day: m 2nd-end: m-1)
# TC:  O(m * (m-1)^(n-1))
# SC: O(n)

# class Solution:
#     def maximumPoints(self, mat):
#         tot_days = len(mat)
#         tot_acti = len(mat[0])
#         #  return max 
#         def func(day,last_acti):
#             if day == n:
#                 return 0
#             max_res = float('-inf')
#             for acti,points in enumerate(mat[day]):
#                 if acti != last_acti:
#                     max_res = max(max_res,func(day+1,acti)+points)
#             return max_res
#         return func(0,-1)

# TC:O(n*k) SC: O(n*k) states in DP 
# class Solution:
#     def maximumPoints(self, mat):
#         tot_days = len(mat)
#         tot_acti = len(mat[0])
#         DP = {}
#         #  return max 
#         def func(day,last_acti):
#             if day == n:
#                 return 0
#             max_res = float('-inf')
#             for acti,points in enumerate(mat[day]):
#                 if acti != last_acti:
#                     if (day+1,acti) not in DP:
#                         DP[(day+1,acti)] = func(day+1,acti)
#                     max_res = max(max_res,DP[(day+1,acti)]+points)
#             return max_res
#         return func(0,-1)
# Tabulation:
# mat =
# Day 0:  1  2  5
# Day 1:  3  1  1
# Day 2:  3  3  3

#              A   B   C
# Day 0        1   2   5
# Day 1        8   6   3
# Day 2        9  11  11

# class Solution:
#     def maximumPoints(self, mat):
#         n = len(mat)
#         m = len(mat[0])
#         if n == 1:
#             return max(mat[0])
#         DP = [[0] * m for _ in range(n)]
#         for i,val in enumerate(mat[0]):
#             DP[0][i] = val
        
#         for day in range(1,n):
#             for acti in range(m):
#                 for new_acti in range(m):
#                     if acti!= new_acti:
#                         new_score = DP[day-1][acti]+mat[day][new_acti]
#                         if DP[day][new_acti] < new_score:
#                             DP[day][new_acti] = new_score
#         return max(DP[n-1])

# Space complexity reduction no need to have full DP array. rather only previous day is needed.
# O(m)
class Solution:
    def maximumPoints(self, mat):
        n = len(mat)
        m = len(mat[0])
        if n == 1:
            return max(mat[0])
        DP = [0]*m
        for i,val in enumerate(mat[0]):
            DP[i] = val
        
        for day in range(1,n):
            new_DP = [0]*m
            for acti in range(m):
                for new_acti in range(m):
                    if acti!= new_acti:
                        new_score = DP[acti]+mat[day][new_acti]
                        if new_DP[new_acti] < new_score:
                            new_DP[new_acti] = new_score
            DP = new_DP
        return max(DP)                  

        
                
                
                
                
                
        
