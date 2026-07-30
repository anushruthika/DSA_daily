## Time complexity: O(n**2) 
#  Space compexity: O(V + E) adj list n nodes and each node can be connected at max n-1 other nodes.

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        adj = [[] for i in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        # base cond fall back 
        # eg: n = 0 edges = [[]] op = [], 
        # eg: n = 1 edges = [[]] op = [0]
        min_ = float('inf') 
        ans = []            
        for node in range(n):
            max_depth = [0]
            visited = set()
            def dfs(node,parent,d):
                visited.add(node)
                max_depth[0] = max(max_depth[0],d)
                for nei in adj[node]:
                    if nei not in visited:
                        dfs(nei,node,d+1)
            dfs(node,-1,0)
            if min_>max_depth[0]:
                min_ = max_depth[0]
                ans = [node]
            elif min_ == max_depth[0]:
                ans.append(node)
        return ans

# Repeatedly remove all leaf nodes (degree = 1) until only 1 or 2 nodes remain—those remaining nodes are the roots of the Minimum Height Trees.
# Peel the tree from the outside inward until only the center(s) remain.

# time : O(n)
# space: O(V + E)
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        adj = [[] for i in range(n)]
        degree = [0] * n
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1
        # base cond fall back 
        # eg: n = 0 edges = [[]] op = [], 
        # eg: n = 1 edges = [[]] op = [0]
        # Add all initial leaves
        q = deque()
        for i in range(n):
            if degree[i] == 1:
                q.append(i)

        remaining = n

        while remaining > 2:

            size = len(q)
            remaining -= size

            for _ in range(size):

                leaf = q.popleft()

                for nei in adj[leaf]:
                    degree[nei] -= 1

                    if degree[nei] == 1:
                        q.append(nei)

        return list(q) if q else [0]

