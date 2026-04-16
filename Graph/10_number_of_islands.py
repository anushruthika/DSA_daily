# 200. Number of Islands

# Time: O(m * n) => each cell is visited at most once

# Space: O(m * n) => queue can hold all cells in worst case (one big island)

from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        lr = len(grid)
        lc = len(grid[0])
        def bfs(x,y):
            queue = deque([(x,y)])
            directions = [(0,1),(0,-1),(-1,0),(1,0)]
            while queue:
                r,c = queue.popleft()
                for dr,dc in directions:
                    nr,nc=r+dr,c+dc
                    if 0<=nr<lr and 0<=nc<lc:
                        if grid[nr][nc] =='1':
                            grid[nr][nc]='v'
                            queue.append((nr,nc))
        count=0
        for i in range(lr):
            for j in range(lc):
                if grid[i][j] == '1':
                    grid[i][j]='v'
                    bfs(i,j)
                    count+=1
        return count
      
# Time: O(m * n) => we traverse the entire grid once, and DFS visits each cell at most once

# Space: O(m * n) => recursion stack in worst case (when the whole grid is one big island)
#                    best case can be O(1) to O(min(m, n)) depending on island shape
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        lr = len(grid)
        lc = len(grid[0])
        def dfs(nr,nc):
            if not(0<=nr<lr and 0<=nc<lc) or grid[nr][nc]!='1':
                return
            grid[nr][nc] ='v'
            dfs(nr+1,nc)
            dfs(nr-1,nc)
            dfs(nr,nc+1)
            dfs(nr,nc-1)
        count=0
        for i in range(lr):
            for j in range(lc):
                if grid[i][j] == '1':
                    dfs(i,j)
                    count+=1
        return count
