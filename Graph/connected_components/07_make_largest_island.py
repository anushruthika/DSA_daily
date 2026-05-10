# 827. Making A Large Island

# Time: O(n^2 * α(n^2))

# - Traverse grid to union neighboring 1s → O(n^2)
# - For every 0, check 4 neighbors → O(n^2)
# - DSU find/union operations are nearly O(1)
#   (α = inverse Ackermann function)

# ⇒ Total: O(n^2 * α(n^2))
# Usually written simply as O(n^2)

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dsu = self.DSU(n*m)
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    node = i*m+j
                    for dr,dc in directions:
                        nr,nc = dr+i,dc+j
                        if 0<=nr<n and 0<=nc<m and grid[nr][nc] ==1:
                            new_node = nr*m+nc
                            dsu.union(node,new_node)
        max_res = float('-inf')
        for i in range(n):
            for j in range(m):
                if grid[i][j] ==0:
                    node = i*m+j
                    set_ds = set()
                    res = 1
                    for dr,dc in directions:
                        nr,nc = dr+i,dc+j
                        if 0<=nr<n and 0<=nc<m and grid[nr][nc] ==1:
                            new_node = nr*m+nc
                            set_ds.add(dsu.find(new_node))
                    for val in set_ds:
                        res+=dsu.size[val]
                    if res>max_res:
                        max_res = res
        # Step 3: if grid already full of 1s
        for i in range(n * m):
            max_res = max(max_res, dsu.size[dsu.find(i)])
        return max_res
    
    class DSU:
        
        def __init__(self, n):
            self.parent = [i for i in range(n)]
            self.size = [1] * n
        
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        
        def union(self, u, v):
            
            pu = self.find(u)
            pv = self.find(v)
            
            if pu == pv:
                return
            
            if self.size[pu] < self.size[pv]:
                pu, pv = pv, pu
            
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
