# 1463. Cherry Pickup II

# | Approach                          | Time Complexity | Space Complexity | Reason                                                                                                        |
# | --------------------------------- | --------------: | ---------------: | ------------------------------------------------------------------------------------------------------------- |
# | **1. Recursion**                  |       **O(9ⁿ)** |         **O(n)** | At every row, Robot 1 has 3 choices and Robot 2 has 3 choices → `3 × 3 = 9` choices. Recursion depth is `n`.  |
# | **2. Memoization**                |   **O(n × m²)** |    **O(n × m²)** | States are `(row, c1, c2)`: `n × m × m` states. Each state tries 9 transitions, which is constant.            |
# | **3. 3D Tabulation**              |   **O(n × m²)** |    **O(n × m²)** | We calculate every `(row, c1, c2)` state once. The 3D DP stores all `n × m²` states.                          |
# | **4. Space-optimized Tabulation** |   **O(n × m²)** |        **O(m²)** | We only need the DP values of the **next row** to calculate the current row, so we keep two `m × m` matrices. |


# class Solution:
#     def cherryPickup(self, grid: List[List[int]]) -> int:

#         n = len(grid)
#         m = len(grid[0])
#         def rec(r, c1, c2):
#             if c1<0 or c2<0 or c1>=m or c2>=m:
#                 return float('-inf')
#             if r == n-1:
#                 if c1 == c2:
#                     return grid[r][c1]
#                 return grid[r][c1]+grid[r][c2]
#             best = float('-inf')
#             for c1_d in [-1,0,1]:
#                 for c2_d in [-1,0,1]:
#                     best = max(best,rec(r+1,c1+c1_d,c2+c2_d))
#             cur = 0
#             if c1 == c2:
#                 cur = grid[r][c1]
#             else:
#                 cur = grid[r][c1]+grid[r][c2]
#             return best+cur
#         return rec(0,0,m-1)

# class Solution:
#     def cherryPickup(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         m = len(grid[0])
#         DP = {}
#         def rec(r, c1, c2):
#             if (r,c1,c2) in DP:
#                 return DP[(r,c1,c2)]
#             if c1<0 or c2<0 or c1>=m or c2>=m:
#                 return float('-inf')
#             if r == n-1:
#                 if c1 == c2:
#                     return grid[r][c1]
#                 return grid[r][c1]+grid[r][c2]
#             best = float('-inf')
#             for c1_d in [-1,0,1]:
#                 for c2_d in [-1,0,1]:
#                     best = max(best,rec(r+1,c1+c1_d,c2+c2_d))
#             cur = 0
#             if c1 == c2:
#                 cur = grid[r][c1]
#             else:
#                 cur = grid[r][c1]+grid[r][c2]
#             DP[(r,c1,c2)] = best+cur
#             return DP[(r,c1,c2)]
#         return rec(0,0,m-1)

# Tabulation

# class Solution:
#     def cherryPickup(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         m = len(grid[0])
#         DP = [[[0] * m for _ in range(m)] for _ in range(n)]

#         #  fill last row
#         for c1 in range(m):
#             for c2 in range(m):
#                 if c1 == c2:
#                     DP[n-1][c1][c2] = grid[n-1][c1]
#                 else:
#                     DP[n-1][c1][c2] = grid[n-1][c1]+grid[n-1][c2]

#         for row in range(n-2,-1,-1):
#             for c1 in range(m):
#                 for c2 in range(m):
#                     cur = 0
#                     if c1 == c2:
#                         cur = grid[row][c1]
#                     else:
#                         cur = grid[row][c1]+grid[row][c2]
#                     best = float('-inf')
#                     for d1 in [-1,0,1]:
#                         for d2 in [-1,0,1]:
#                             nc1 = c1 + d1
#                             nc2 = c2 + d2
#                             if 0 <= nc1 < m and 0 <= nc2 < m:
#                                 best = max(best,DP[row+1][nc1][nc2])
#                     DP[row][c1][c2] = best+cur
#         # lets say robots starts at column rob1 rob2 the op: DP[0][rob1-1][rob2-1]
#         return DP[0][0][m-1]
                
# Space reduction:

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        DP = [[0] * m for _ in range(m)]

        #  fill last row
        for c1 in range(m):
            for c2 in range(m):
                if c1 == c2:
                    DP[c1][c2] = grid[n-1][c1]
                else:
                    DP[c1][c2] = grid[n-1][c1]+grid[n-1][c2]

        for row in range(n-2,-1,-1):
            # updating DP in place while also using DP as the values of the next row.
            new_DP = [[0] * m for _ in range(m)]
            for c1 in range(m):
                for c2 in range(m):
                    cur = 0
                    if c1 == c2:
                        cur = grid[row][c1]
                    else:
                        cur = grid[row][c1]+grid[row][c2]
                    best = float('-inf')
                    for d1 in [-1,0,1]:
                        for d2 in [-1,0,1]:
                            nc1 = c1 + d1
                            nc2 = c2 + d2
                            if 0 <= nc1 < m and 0 <= nc2 < m:
                                best = max(best,DP[nc1][nc2])
                    new_DP[c1][c2] = best+cur
            DP = new_DP
        # lets say robots starts at column rob1 rob2 the op: DP[0][rob1-1][rob2-1]
        return DP[0][m-1]
