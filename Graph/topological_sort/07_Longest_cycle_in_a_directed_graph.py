# https://www.geeksforgeeks.org/problems/length-of-longest-cycle-in-a-graph/1

# Time Complexity: O(V + E)
# Space Complexity: O(V)

class Solution:

    def longestCycle(self, V, edges):

        # Build adjacency list
        adj = [[] for _ in range(V)]

        for u, v in edges:
            adj[u].append(v)

        visited = [False] * V

        in_path = [False] * V

        depth = [0] * V

        longest = [-1]

        def dfs(node, d):

            visited[node] = True

            in_path[node] = True

            depth[node] = d

            for nei in adj[node]:

                # Tree edge
                if not visited[nei]:

                    dfs(nei, d + 1)

                # Back edge → cycle found
                elif in_path[nei]:

                    cycle_len = depth[node] - depth[nei] + 1

                    longest[0] = max(longest[0], cycle_len)

            # Remove from current DFS path
            in_path[node] = False

        for i in range(V):

            if not visited[i]:

                dfs(i, 0)

        return longest[0]
