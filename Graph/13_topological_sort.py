# https://www.geeksforgeeks.org/problems/topological-sort/1

# Time: O(V + E) => building adjacency list takes O(E), and DFS visits each node and edge once
# Space: O(V + E) => adjacency list stores all edges + visited array + recursion stack (worst case O(V))

class Solution:
    def topoSort(self, V, edges):
        adj = [[] for _ in range(V)]
        for i,j in edges:
            adj[i].append(j)
        # print(adj)
        visited = [False]*V
        stack = []
        def dfs(node):
            visited[node]=True
            for path in adj[node]:
                if not visited[path]:
                    dfs(path)
            stack.append(node)
        for i in range(V):
            if not visited[i]:
                dfs(i)
                # print(visited,stack)
        # print(stack[::-1])
        return stack[::-1]
