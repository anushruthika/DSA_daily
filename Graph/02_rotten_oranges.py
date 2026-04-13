# 994. Rotting Oranges

# Time: O(m * n) => each cell is visited at most once
# Space: O(m * n) => queue can store all cells in worst case

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # get grid dimensions
        rl = len(grid)
        cl = len(grid[0])
        
        queue = deque()
        fresh = 0
        
        # Step 1: initialize BFS
        # add all rotten oranges to queue (multi-source BFS)
        # count number of fresh oranges
        for i in range(rl):
            for j in range(cl):
                if grid[i][j] == 2:
                    queue.append((i, j))   # starting points of infection
                elif grid[i][j] == 1:
                    fresh += 1             # count fresh oranges
        
        # directions for 4-directional movement
        directions = [(0,-1), (-1,0), (0,1), (1,0)]
        
        time = 0
        
        # Step 2: BFS traversal (level-order)
        # each level represents 1 minute
        while queue and fresh > 0:
            
            # process all oranges that rot in current minute
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                # spread rot to adjacent cells
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # check bounds + fresh orange
                    if 0 <= nr < rl and 0 <= nc < cl and grid[nr][nc] == 1:
                        grid[nr][nc] = 2     # make it rotten
                        fresh -= 1           # reduce fresh count
                        queue.append((nr, nc))  # add to queue for next minute
            
            # increment time after processing one full level
            time += 1
        
        # Step 3: check if all oranges are rotten
        # if fresh == 0 → return time
        # else → impossible case
        return time if fresh == 0 else -1
