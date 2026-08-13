# 63. Unique Paths II

# | Approach                             | Time Complexity | Space Complexity |
# | ------------------------------------ | --------------: | ---------------: |
# | **1. Plain Recursion**               |  **O(2^(m+n))** |       **O(m+n)** |
# | **2. Memoization**                   |    **O(m × n)** |     **O(m × n)** |
# | **3. Tabulation — `-1` logic**       |    **O(m × n)** |     **O(m × n)** |
# | **4. Tabulation — simple `0` logic** |    **O(m × n)** |     **O(m × n)** |
# | **5. Space-optimized Tabulation**    |    **O(m × n)** |         **O(n)** |

# edge cases: 
# grid = [[0]] ways = 1
# grid = [[1]] ways = 0 i.e: grid[m-1][n-1] = 1 grid[0][0] = 1

# class Solution:
#     def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
#         m = len(grid)
#         n = len(grid[0])
#         if grid[m-1][n-1] == 1 or grid[0][0] == 1:
#             return 0
#         def rec(r,c):
#             if r == m-1 and c == n-1:
#                 return 1
#             if r >= m or c >= n or grid[r][c] == 1:
#                 return 0
#             return rec(r+1,c) + rec(r,c+1)
#         return rec(0,0)

#  DP
# class Solution:
#     def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
#         m = len(grid)
#         n = len(grid[0])
#         if grid[m-1][n-1] == 1 or grid[0][0] == 1:
#             return 0
#         DP = {} # store states r,c
#         def rec(r,c):
#             if r == m-1 and c == n-1:
#                 return 1
#             if r >= m or c >= n or grid[r][c] == 1:
#                 return 0
#             if (r+1,c) not in DP:
#                 DP[(r+1,c)] = rec(r+1,c)
#             if (r,c+1) not in DP:
#                 DP[(r,c+1)] = rec(r,c+1)
#             DP[(r,c)] = DP[(r+1,c)]+DP[(r,c+1)]
#             return DP[(r,c)]
#         return rec(0,0)

#  Tabulation
# class Solution:
#     def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
#         m = len(grid)
#         n = len(grid[0])
#         if grid[m-1][n-1] == 1 or grid[0][0] == 1:
#             return 0
#         DP = [[0]*n for i in range(m)]
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] ==1:
#                     DP[i][j] =-1
#                 # This means every non-obstacle cell in the first row/column gets 1, even if there was an obstacle before it.
#                 # elif i == 0 or j == 0:
#                 #     DP[i][j] = 1
#         flag = 1
#         for i in range(m):
#             if grid[i][0] == 1:
#                 flag = 0
#                 break
#             if flag:
#                 DP[i][0] = 1
#             else:
#                 DP[i][0] = -1
#         flag = 1
#         for i in range(n):
#             if grid[0][i] == 1:
#                 flag = 0
#                 break
#             if flag:
#                 DP[0][i] = 1
#             else:
#                 DP[0][i] = -1
            
#         for i in range(1,m):
#             for j in range(1,n):
#                 if DP[i][j] == -1:
#                     continue
#                 if DP[i-1][j] == -1 and DP[i][j-1]==-1:
#                     DP[i][j] = -1
#                 elif DP[i-1][j] == -1:
#                     DP[i][j] = DP[i][j-1]
#                 elif DP[i][j-1] == -1:
#                     DP[i][j] = DP[i-1][j]
#                 else:
#                     DP[i][j] = DP[i-1][j] +DP[i][j-1]
#         if DP[m-1][n-1] == -1:
#             return 0
#         return DP[m-1][n-1]

# Tabulation different logic
# class Solution:
#     def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
#         m = len(grid)
#         n = len(grid[0])

#         if grid[0][0] == 1:
#             return 0

#         DP = [[0] * n for _ in range(m)]
#         DP[0][0] = 1

#         for i in range(m):
#             for j in range(n):

#                 if grid[i][j] == 1:
#                     DP[i][j] = 0
#                     continue

#                 if i > 0:
#                     DP[i][j] += DP[i-1][j]

#                 if j > 0:
#                     DP[i][j] += DP[i][j-1]

#         return DP[m-1][n-1]

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        if grid[0][0] == 1:
            return 0

        DP = [0]*n
        DP[0] = 1

        for i in range(m):
            for j in range(n):

                if grid[i][j] == 1:
                    DP[j] = 0
                    continue
                if j > 0:
                    DP[j] += DP[j-1]

        return DP[n-1]

