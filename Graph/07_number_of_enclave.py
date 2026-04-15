# 1020. Number of Enclaves

# Time: O(m * n) => full grid traversal (marking boundary + inner cells) + BFS traversal (each cell visited at most once) + final pass to count
# Space: O(m * n) => queue in worst case (all cells can be added), no extra space since grid is modified in-place

####
# Multi-source BFS
####
from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        queue = deque([])
        lr = len(grid)
        lc = len(grid[0])
        for i in range(lr):
            for j in range(lc):
                if grid[i][j] == 1:
                    if i == 0 or i==lr-1 or j==0 or j==lc-1:
                        queue.append((i,j))
                    # marking all 1's inside boundary as 2
                    else:
                        grid[i][j] = 2

        while queue:
            r,c = queue.popleft()
            for dr,dc in directions:
                nr,nc = r+dr , c+dc
                if 0<=nr<lr and 0<=nc<lc:
                    if grid[nr][nc] == 2:
                        grid[nr][nc] = 1
                        queue.append((nr,nc))
        count = 0

####
# DFS
####
# Time: O(m * n) => full grid traversal (mark all 1s as 2 + collect boundary cells) 
#                     + DFS flood fill (each cell visited at most once) 
#                     + final pass to count remaining 2s

# Space: O(m * n) => recursion stack in worst case (grid fully connected),
#                    list 'l' storing boundary cells can also take O(m * n)

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        lr = len(grid)
        lc = len(grid[0])
        l=[]
        for i in range(lr):
            for j in range(lc):
                if grid[i][j] == 1:
                    if i == 0 or i==lr-1 or j==0 or j==lc-1:
                        l.append((i,j))
                    # marking all 1's => whole matrix => as 2
                    # else:
                    grid[i][j] = 2
        def flood_fill(nr,nc):
            if not(0<=nr<lr and 0<=nc<lc) or grid[nr][nc] != 2:
                return
            print(grid[nr][nc])
            grid[nr][nc] = 1
            flood_fill(nr+1,nc)
            flood_fill(nr-1,nc)
            flood_fill(nr,nc-1)
            flood_fill(nr,nc+1)

        for r,c in l:
            flood_fill(r,c)
        print(grid)
        count = 0
        for i in range(lr):
            for j in range(lc):
                if grid[i][j] == 2:
                    count+=1
        return count
        for i in range(lr):
            for j in range(lc):
                if grid[i][j] == 2:
                    count+=1
        return count
