## Time complexity: O(n**2) 
#  Space compexity: O(n**2) adj list n nodes and each node can be connected at max n-1 other nodes.

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

  
