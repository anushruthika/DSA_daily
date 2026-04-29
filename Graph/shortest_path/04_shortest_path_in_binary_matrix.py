# https://leetcode.com/problems/shortest-path-in-binary-matrix/submissions/1990716231/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        dir_ = [(0,1),(1,0),(1,1),(0,-1),(-1,0),(-1,-1),(1,-1),(-1,1)]
        queue = collections.deque([(0,0,1)])
        visited = set()
        visited.add((0,0))
        while queue:
            x,y,d = queue.popleft()
            if x == n-1 and y ==n-1:
                return d
            for i,j in dir_:
                nx,ny = i+x,j+y
                if 0<=nx<n and 0<=ny<n and (nx,ny) not in visited and grid[nx][ny]==0:
                    grid[nx][ny] = 1
                    visited.add((nx,ny))
                    queue.append((nx,ny,d+1))
        return -1
            
