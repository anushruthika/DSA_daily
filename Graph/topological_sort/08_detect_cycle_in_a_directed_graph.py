# https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1

# Time Complexity: O(V + E)
# - Building the adjacency list takes O(E).
# - DFS visits each vertex once and explores each edge once.

# Space Complexity: O(V + E)
# - O(V + E) for the adjacency list.
# - O(V) for visited and recursion path arrays.
# - O(V) recursion stack in the worst case.

class Solution:
    def isCyclic(self, V, edges):
        path = [False]*V
        visited = [False]*V
        adj = [[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
        def dfs(node):
            path[node] = visited[node] = True
            for nei in adj[node]:
                if visited[nei] != True:
                    if dfs(nei):
                        return True
                elif path[nei] == True:
                    return True
            path[node] = False
            return False
        for i in range(V):
            if not visited[i]:
                if dfs(i):
                    return True
        return False
                    
        
