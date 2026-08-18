# 64. Minimum Path Sum

# | Approach                       |           Time |      Space |
# | ------------------------------ | -------------: | ---------: |
# | **Recursion**                  | **O(2^(m+n))** | **O(m+n)** |
# | **Memoization**                |     **O(m×n)** | **O(m×n)** |
# | **Tabulation**                 |     **O(m×n)** | **O(m×n)** |
# | **Space-optimized Tabulation** |     **O(m×n)** |   **O(m)** |


class Solution:
    # # recursion
    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     n = len(grid)
    #     m = len(grid[0])
    #     def rec(r,c):
    #         if r>=n or c>=m:
    #             return float('inf')
    #         if r == n-1 and c == m-1:
    #             return grid[r][c]
    #         right = rec(r,c+1)+grid[r][c]
    #         down = rec(r+1,c)+grid[r][c]
    #         return min(right,down)
    #     return rec(0,0)
    # memoization
    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     n = len(grid)
    #     m = len(grid[0])
    #     # DP = [[-1]*m for _ in range(n)]
    #     DP = {}
    #     def rec(r,c):
    #         if (r,c) in DP:
    #             return DP[(r,c)]
    #         if r>=n or c>=m:
    #             return float('inf')
    #         if r == n-1 and c == m-1:
    #             return grid[r][c]
    #         right = rec(r,c+1)+grid[r][c]
    #         down = rec(r+1,c)+grid[r][c]
    #         DP[(r,c)] = min(right,down)
    #         return DP[(r,c)]
    #     return rec(0,0)
    # # Tabulation
    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     n = len(grid)
    #     m = len(grid[0])
    #     DP = [[0]*m for _ in range(n)]
    #     DP[0][0] = grid[0][0]
    #     for c in range(1,m):
    #         DP[0][c] = DP[0][c-1]+grid[0][c]
    #     for r in range(1,n):
    #         DP[r][0] = DP[r-1][0]+grid[r][0]
    #     for r in range(1,n):
    #         for c in range(1,m):
    #             DP[r][c]=min(DP[r-1][c],DP[r][c-1])+grid[r][c]
    #     return DP[n-1][m-1]
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        DP = [0]*m
        DP[0] = grid[0][0]
        for c in range(1,m):
            DP[c] = DP[c-1]+grid[0][c] 
        for r in range(1,n):
            for c in range(m):
                if c>0:
                    DP[c] = min(DP[c],DP[c-1])+grid[r][c]
                else:
                    DP[c] = DP[c]+grid[r][c]
        return DP[m-1]

    

