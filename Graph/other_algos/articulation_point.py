# https://www.geeksforgeeks.org/problems/articulation-point-1/1

# Time Complexity  : O(V + E)
# Space Complexity : O(V)
class Solution:

    # Function to find articulation points in the graph
    def articulationPoints(self, V, adj):

        # Time Complexity : O(V + E)
        # Space Complexity: O(V)

        disc = [-1] * V
        low = [-1] * V

        visited = [False] * V

        ap = [False] * V

        timer = [0]

        # DFS function
        def dfs(u, parent):

            visited[u] = True

            timer[0] += 1

            disc[u] = low[u] = timer[0]

            children = 0

            # Traverse neighbors
            for v in adj[u]:

                # Tree Edge
                if not visited[v]:

                    children += 1

                    dfs(v, u)

                    # Update low value
                    low[u] = min(low[u], low[v])

                    # Case 1:
                    # Root node with more than one child
                    if parent == -1 and children > 1:
                        ap[u] = True

                    # Case 2:
                    # Non-root node
                    if parent != -1 and low[v] >= disc[u]:
                        ap[u] = True

                # Back Edge
                elif v != parent:

                    low[u] = min(low[u], disc[v])

        # Run DFS for all nodes
        for i in range(V):

            if not visited[i]:

                dfs(i, -1)

        # Collect articulation points
        ans = []

        for i in range(V):

            if ap[i]:
                ans.append(i)

        # If no articulation point exists
        if not ans:
            return [-1]

        return ans
