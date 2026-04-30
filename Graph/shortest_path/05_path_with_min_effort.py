# 1631. Path With Minimum Effort
# # Time Complexity:
# O(n * m * log(n * m))
# Reason:
# - There are n*m cells → total nodes (V)
# - Each cell explores up to 4 neighbors → constant work
# - Each time we relax an edge, we push into heap
# - Heap push/pop takes O(log(n*m))
# - So overall = O(V log V) = O(n*m log(n*m))

# Space Complexity:
# O(n * m)
# Reason:
# - res matrix stores minimum effort for each cell → O(n*m)
# - heap can contain up to O(n*m) elements in worst case
# - No additional major space used
import heapq
class Solution:
    def minimumEffortPath(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        res= [[float('inf')]*m for _ in range(n)]
        res[0][0]=0
        heap = [(0,0,0)]
        while heap:
            cur_sum,x,y = heapq.heappop(heap)
            if x == n-1 and y == m-1:
                return cur_sum
            for dx,dy in directions:
                nx,ny = dx+x,dy+y
                if 0<=nx<n and 0<=ny<m:
                    new_sum = max(cur_sum, abs(grid[nx][ny] - grid[x][y]))
                    if new_sum<res[nx][ny]:
                        res[nx][ny] = new_sum
                        heapq.heappush(heap,(new_sum,nx,ny))
        return -1          
      

#############
# Minumm path sum
#############
# Time Complexity:
# O(n * m * log(n * m))
# Reason:
# - There are n*m cells (nodes in the grid)
# - Each cell can be pushed into the heap
# - For each push/pop operation → heap takes O(log(n*m))
# - Each cell explores at most 4 neighbors (constant work)
# - So total = O(V log V) = O(n*m log(n*m))

# Space Complexity:
# O(n * m)
# Reason:
# - res matrix stores distance for each cell → O(n*m)
# - heap can store up to O(n*m) elements in worst case
# - No extra significant space used
import heapq
class Solution:
    def minimumEffortPath(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        res= [[float('inf')]*m for _ in range(n)]
        res[0][0]=grid[0][0]
        heap = [(grid[0][0],0,0)]
        while heap:
            cur_sum,x,y = heapq.heappop(heap)
            if x == n-1 and y == m-1:
                return cur_sum
            for dx,dy in directions:
                nx,ny = dx+x,dy+y
                if 0<=nx<n and 0<=ny<m:
                    new_sum = cur_sum+grid[nx][ny]
                    print(cur_sum,res[x][y],new_sum,nx,ny)
                    if new_sum<res[nx][ny]:
                        res[nx][ny] = new_sum
                        heapq.heappush(heap,(new_sum,nx,ny))
        return -1          
