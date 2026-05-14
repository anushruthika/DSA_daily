# https://www.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1

# Time Complexity: O(V + E)
# Space Complexity: O(V + E)

class Solution:

    def kosaraju(self, V, edges):

        # Step 1: Build graph
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
        
        # step 2: append stack with nodes 
        visited = [False] * V
        stack = []
        def dfs(node):
            visited[node] = True
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei)
            stack.append(node)
        for i in range(V):
            if not visited[i]:
                dfs(i)
        print(stack)
        # Step 3: Reverse graph
        rev_adj = [[] for _ in range(V)]
        for u, v in edges:
            rev_adj[v].append(u)
        
        # Step 4: DFS on reversed graph
        visited = [False] * V
        sccs = []
        def rev_dfs(node, curr_scc):
            visited[node] = True
            curr_scc.append(node)
            for nei in rev_adj[node]:
                if not visited[nei]:
                    rev_dfs(nei, curr_scc)
        # Process in reverse topo order
        while stack:
            node = stack.pop()
            if not visited[node]:
                curr_scc = []
                rev_dfs(node, curr_scc)
                sccs.append(curr_scc)

        # print("SCCs:", sccs)
        # print("Number of SCCs:", len(sccs))
        return len(sccs)
