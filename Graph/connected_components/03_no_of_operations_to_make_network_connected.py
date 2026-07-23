# 1319. Number of Operations to Make Network Connected

# Time: O(V + E)
# - Building adjacency list → O(E)
# - DFS visits each node once → O(V)
# - Each edge is traversed at most twice (undirected graph) → O(E)

# Space: O(V + E)
# - Adjacency list stores all edges → O(E)
# - Visited array → O(V)
# - DFS recursion stack can go up to O(V)

# | Approach                 | Time Complexity        | Space Complexity | Reason                                                                                                                                                                            |
# | ------------------------ | ---------------------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
# | **DFS (Adjacency List)** | **O(V + E)**           | **O(V + E)**     | Build adjacency list in **O(E)**, DFS visits each vertex once and each edge once. 
                                                                            # Space includes adjacency list **O(V+E)**, visited array **O(V)**, and recursion stack **O(V)**. |
# | **DSU (Union-Find)**     | **O(E · α(V)) ≈ O(E)** | **O(V)**         | Process each edge once. Each `union/find` is **O(α(V))** (nearly constant) due to path compression and 
                                                                            # union by rank. Space is only `parent` and `rank` arrays.                   |

class Solution:
    def makeConnected(self, V, edges):

        # rule to connect all nodes V need V-1 edges to connect.
        # eg: 3 nodes - require 2 edges to connect.

        # return -1 if number of existing connections is less than number of vertex -1
        if len(edges) < V - 1:
            return -1

        adj = [[] for _ in range(V)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * V

        def dfs(node):
            visited[node] = True
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei)

        components = 0

        for i in range(V):
            if not visited[i]:
                components += 1
                dfs(i)

        # same rule.. to connect 'C' unconnected Components, atleast C-1 edges are required.
        return components - 1


class Solution:
    class DSU:
        def __init__(self,n):
            self.parent = [i for i in range(n)]
            self.rank = [0]*n
        def find(self,x):
            if self.parent[x]!=x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        def union(self,u,v):
            pu = self.find(u)
            pv = self.find(v)
            if pu == pv:
                return False
            if self.rank[pu]>self.rank[pv]:
                self.parent[pv] = self.parent[pu]
            elif self.rank[pv]>self.rank[pu]:
                self.parent[pu] = self.parent[pv]
            else:
                self.parent[pv] = self.parent[pu]
                self.rank[pu]+=1
            return True

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        # for n computers we need n-1 edges
        edge_count = len(connections)
        if n-1>edge_count:
            return -1
        dsu = self.DSU(n)
        count = 0
        for u,v in connections:
            if dsu.union(u,v):
                count+=1
        return n-count-1
