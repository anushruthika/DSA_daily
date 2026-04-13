# 547. Number of Provinces

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

            
        
