# https://www.geeksforgeeks.org/problems/number-of-islands/1

# Time: O(K * α(rows * cols)))

# - K = number of operators
# - For each operator:
#     - check 4 neighbors → O(1)
#     - union/find operations → nearly O(1) using path compression + union by rank
# - α(N) = inverse Ackermann function (extremely small)

# ⇒ Total: O(K * α(rows * cols))


# Space: O(rows * cols)

# - DSU parent array → O(rows * cols)
# - Rank array → O(rows * cols)
# - Visited grid → O(rows * cols)
# - Result array → O(K)

# ⇒ Total: O(rows * cols)
from typing import List

class Solution:
    
    def numOfIslands(self, rows: int, cols: int, operators: List[List[int]]) -> List[int]:
        dsu = self.dsu(rows * cols)
        visited = [[0]*cols for _ in range(rows)]
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        res = []
        count = 0
        for r,c in operators:
            node = r*cols+c
            if visited[r][c]:
                res.append(count)
                continue
            visited[r][c] = 1
            count+=1
            for dr,dc in directions:
                nr,nc = dr+r,dc+c
                if 0<=nr<rows and 0<=nc<cols and visited[nr][nc]:
                    new_node = nr*cols+nc
                    if dsu.union(node,new_node):
                        count-=1
            res.append(count) 
        return res
        
    class dsu:
        
        def __init__(self, n):
            self.parent = [i for i in range(n)]
            self.rank = [0] * n
        
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        
        def union(self, u, v):
            
            pu = self.find(u)
            pv = self.find(v)
            
            if pu == pv:
                return False
            
            if self.rank[pu] < self.rank[pv]:
                self.parent[pu] = pv

            elif self.rank[pv] < self.rank[pu]:
                self.parent[pv] = pu

            else:
                self.parent[pv] = pu
                self.rank[pu] += 1
            
            return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
