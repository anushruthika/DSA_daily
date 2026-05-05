# 542. 01 Matrix

# Time: O(m * n) => each cell is processed at most once in BFS (each update happens once)
# Space: O(m * n) => queue can hold up to all cells in worst case

from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dir_ = [(1,0),(0,1),(-1,0),(0,-1)]
        lr = len(mat)
        lc = len(mat[0])
        queue = deque()
        # 1. append queue with 0 ind
        # 2. overwrite 1 with infinity
        for i in range(lr):
            for j in range(lc):
                if mat[i][j] == 0:
                    queue.append((i,j))
                elif mat[i][j] == 1:
                    mat[i][j] = float('inf')
        
        # 0 slowly cover 1 nearby and move deep
        while queue:
            r,c = queue.popleft()
            for dr,dc in dir_:
                nr,nc = r+dr,c+dc
                if 0<=nr<lr and 0<=nc<lc :
                    # correction of relaxation
                    if mat[nr][nc]>mat[r][c]+1:
                        mat[nr][nc] = mat[r][c]+1
                        queue.append((nr,nc))
        return mat

# this problem is naturally a multi-source BFS problem, so DFS will be less efficient (can revisit cells many times)
# BFS (your code):
# Processes layer by layer → guarantees shortest path immediately ✅
# Time: O(m × n)
# DFS (this version):
# May revisit cells multiple times ❌
# Worst-case time: O((m × n)²)
#####
# will hit TLE
#####
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        # Initialize: mark 1s as infinity
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    mat[i][j] = float('inf')
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        
        def dfs(r, c):
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    # If we can improve distance, update and continue DFS
                    if mat[nr][nc] > mat[r][c] + 1:
                        mat[nr][nc] = mat[r][c] + 1
                        dfs(nr, nc)
        
        # Start DFS from all 0 cells
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dfs(i, j)
        
        return mat
