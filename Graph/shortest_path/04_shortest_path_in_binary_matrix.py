# https://leetcode.com/problems/shortest-path-in-binary-matrix/submissions/1990716231/

# Use Dijkstra's algorithm when graph edges have different (weighted) costs, to always find the minimum-distance path.

# here, BFS (queue / deque) efficient
# -------------------------------
# 2️⃣ BFS (queue / deque)
# -------------------------------

# Time: O(n^2)
# - Each cell visited at most once → O(n^2)
# - Each has constant 8 neighbors
# ⇒ O(n^2)

# Space: O(n^2)
# - Queue can hold up to n^2 cells
# - Visited set stores up to n^2 cells
# ⇒ O(n^2)

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

# -------------------------------
# 1️⃣ Dijkstra (heap / priority queue)
# -------------------------------

# Time: O(n^2 log n)
# - Total nodes = n^2
# - Each cell can be pushed into heap → O(n^2) pushes
# - Each push/pop takes log(n^2) = log n
# ⇒ Total: O(n^2 log n)

# Space: O(n^2)
# - Heap can store up to n^2 cells
# - Grid used as visited
# ⇒ O(n^2)
import heapq
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0]!=0 or grid[n-1][n-1]!=0:
            return -1
        directions = [(0,1),(1,0),(0,-1),(-1,0),(1,-1),(1,1),(-1,1),(-1,-1)]
        pq = [(1,0,0)]
        while pq:
            d,r,c = heapq.heappop(pq)
            if r ==n-1 and c == n-1:
                return d
            for dr,dc in directions:
                nr,nc = dr+r,dc+c
                if 0<=nr<n and 0<=nc<n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    heapq.heappush(pq,(d+1,nr,nc))
        return -1
