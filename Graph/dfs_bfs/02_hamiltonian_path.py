# https://www.geeksforgeeks.org/problems/hamiltonian-path2522/1

# A Hamiltonian Path is a path that visits every vertex exactly once.

# inside dfs check if count==n pass count as parameter
# Hamiltonian Path

# Time Complexity: O(V!)
# Space Complexity: O(V+E)

# time complexity is not O(V+E) and is O(V!) because we backtrack making visited as false. 
# Eg: V=3 then V! times to check all these possibilities

# graph:
# 1
# / \
# 2---3

# 1 → 2 → 3
# 1 → 3 → 2

# 2 → 1 → 3
# 2 → 3 → 1

# 3 → 1 → 2
# 3 → 2 → 1

class Solution:
    def check(self, n, m, edges):
        # Build graph
        adj = [[] for _ in range(n)]
        for u, v in edges:
            u -= 1
            v -= 1

            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n

        # Backtracking DFS
        def dfs(node, count):

            # All nodes visited
            if count == n:
                return True

            visited[node] = True

            for nei in adj[node]:

                if not visited[nei]:

                    if dfs(nei, count + 1):
                        return True

            # Backtrack
            visited[node] = False

            return False

        # Try starting from every node
        for i in range(n):

            visited = [False] * n

            if dfs(i, 1):
                return True

        return False
