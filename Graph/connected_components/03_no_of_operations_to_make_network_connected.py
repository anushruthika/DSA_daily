# 1319. Number of Operations to Make Network Connected

# Time: O(V + E)
# - Building adjacency list → O(E)
# - DFS visits each node once → O(V)
# - Each edge is traversed at most twice (undirected graph) → O(E)

# Space: O(V + E)
# - Adjacency list stores all edges → O(E)
# - Visited array → O(V)
# - DFS recursion stack can go up to O(V)
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
