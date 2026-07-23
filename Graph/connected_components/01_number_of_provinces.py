# 547. Number of Provinces

# | Approach | Time      | Space    |
# | -------- | --------- | -------- |
# | DFS      | **O(n²)** | **O(n)** |
# | BFS      | **O(n²)** | **O(n)** |
# | DSU      | **O(n²)** | **O(n)** |

# Time: O(n^2) => adjacency matrix traversal
# Space: O(n) => visited + queue
# 💡 Can we do better than O(n²)?

# 👉 No, because:

# Input is an n × n matrix
# You must check all entries

# 👉 So O(n²) is optimal

#######
# DFS
#######

from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        
        def dfs(ind):
            for j in range(len(isConnected)):
                if isConnected[ind][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)
        provinces = 0
        for i in range(len(isConnected)):
            if i not in visited:
                visited.add(i)
                dfs(i)
                provinces+=1
        return provinces


#######
# BFS
#######

from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        def bfs(ind):
            queue = deque([ind])
            while queue:
                x = queue.popleft()
                visited.add(x)
                for i,val in enumerate(isConnected[x]):
                    if val==1 and i not in visited:
                        queue.append(i)
        
        provinces = 0
        for i in range(len(isConnected)):
            if i not in visited:
                bfs(i)
                provinces+=1
        return provinces

#######
# DSU
######

from collections import deque
class Solution:
    class DSU:
        def __init__(self,n:int):
            self.parent =[i for i in range(n)]
            self.rank = [0]*n
        def find(self,x):
            if self.parent[x]!=x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        def union(self,u,v):
            pu = self.find(u)
            pv = self.find(v)
            # already connected
            if pu == pv:
                return False
            # new connection
            if self.rank[pu]>self.rank[pv]:
                self.parent[pv] = self.parent[pu]
            elif self.rank[pv]>self.rank[pu]:
                self.parent[pu] = self.parent[pv]
            else:
                self.parent[pv] = self.parent[pu]
                self.rank[pu]+=1
            return True
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        n = len(isConnected)
        dsu = self.DSU(n)
        # n*n matrix
        for i in range(n):
            # for j in range(n):
            #     if i!=j and isConnected[i][j] == 1:
            for j in range(i+1,n):
                if isConnected[i][j] == 1:
                    if dsu.union(i,j):
                        count+=1
        return n-count


            
        

            
        
