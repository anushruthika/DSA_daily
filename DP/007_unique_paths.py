# 62. Unique Paths

# | Approach                          |             TC |           SC |
# | --------------------------------- | -------------: | -----------: |
# | **1. Plain recursion**            | **O(2^(m+n))** |   **O(m+n)** |
# | **2. Recursion returning count**  | **O(2^(m+n))** |   **O(m+n)** |
# | **3. Memoization**                |   **O(m × n)** | **O(m × n)** |
# | **4. Tabulation (2D DP)**         |   **O(m × n)** | **O(m × n)** |
# | **5. Space-optimized Tabulation** |   **O(m × n)** |     **O(n)** |

#  logic: paths(r,c) = paths(r-1,c) + paths(r,c-1)

# eg: grid =

# [ 0  0  0 ]
# [ 0  0  0 ]
# [ 0  0  0 ]

# recursion
                #               (0,0)
                #              /     \
                #             /       \
                #        (1,0)       (0,1)
                #        /   \       /   \
                #       /     \     /     \
                #  (2,0)    (1,1) (1,1)  (0,2)
                #    |       / \    / \      |
                #    |      /   \  /   \     |
                # (2,1)  (2,1) (1,2)(1,2) (1,2)
                #    |      |      |    |      |
                #    |      |      |    |      |
                # (2,2)  (2,2) (2,2)(2,2) (2,2)
                   ✓      ✓      ✓    ✓      ✓
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         count = [0]
#         def rec(r,c):
#             if r == m-1 and c ==n-1:
#                 count[0]+=1
#                 return
            # if r >= m or c >= n:
            #     return 0
#             rec(r+1,c)
#             rec(r,c+1)
#         rec(0,0)
#         return count[0]
# Recursion 2: return count
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         def rec(r,c):
#             if r == m-1 and c ==n-1:
#                 return 1
#             if r >= m or c >= n:
#                 return 0
#             return rec(r+1,c) + rec(r,c+1)
#         return rec(0,0)

# # memoization
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         # store number of paths to reach the index (r,c)
#         DP = {}
#         def rec(r,c):
#             if r == m-1 and c ==n-1:
#                 return 1
#             if r >= m or c >= n:
#                 return 0
#             if (r,c) in DP:
#                 return DP[(r,c)]
#             DP[(r,c)] =  rec(r+1,c) + rec(r,c+1)
#             return DP[(r,c)] 
#         return rec(0,0)

# # # Tabulation
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         # store number of paths to reach the index (r,c)
#         DP = [[0]*n for _ in range(m)]
#         # -1 states that position is unreachable at beggining
#         # 1 way to reach
#         DP[0][0] = 1
#         # First row → only one way: move right
#         for c in range(n):
#             DP[0][c] = 1
#         # First column → only one way: move down
#         for r in range(m):
#             DP[r][0] = 1
#         for r in range(1,m):
#             for c in range(1,n):
#                 DP[r][c] = DP[r-1][c]+DP[r][c-1]
#         return DP[m-1][n-1]
                
# # Space complexity
# logic:
# dp[c]   = previous row, above
# dp[c-1] = current row, left
# dp[c] = dp[c] + dp[c-1]
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        DP = [1] * n
        for r in range(1,m):
            for c in range(1,n):
                DP[c] = DP[c]+DP[c-1]
        return DP[-1]
