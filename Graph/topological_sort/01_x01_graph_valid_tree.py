# gfg not working

# 1. Tree must have exactly n-1 edges
# V -1= len(edges)
# 2. No cycle within


class Solution:

    def isTree(self, n, m, edges):

        # Time Complexity : O(V + E)
        # Space Complexity: O(V)

        # Tree must have exactly n-1 edges
        if m != n - 1:
            return 0

        # Build adjacency list
        adj = [[] for _ in range(n)]

        for u, v in edges:

            # Self loop
            if u == v:
                return 0

            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n

        # DFS function
        def dfs(node, parent):

            visited[node] = True

            for nei in adj[node]:

                # Ignore parent edge
                if nei == parent:
                    continue

                # Cycle detected
                if visited[nei]:
                    return False

                if not visited[nei]:

                    if not dfs(nei, node):
                        return False

            return True

        # Check cycle
        if not dfs(0, -1):
            return 0

        # Check connectivity
        for i in range(n):

            if not visited[i]:
                return 0

        return 1
