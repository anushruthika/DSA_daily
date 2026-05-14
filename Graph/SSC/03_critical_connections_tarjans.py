 # Time Complexity: O(V + E)
 # Space Complexity: O(V)
class Solution:
    def criticalConnections(self, V: int, connections: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(V)]
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u) 
        disc = [-1]*V
        low = [-1]*V
        timer = [0]
        bridges = []
        def dfs(node,parent):
            timer[0] +=1
            low[node] = disc[node] = timer[0]
            for nei in adj[node]:
                if nei == parent:continue
                if disc[nei] == -1:
                    dfs(nei,node)
                    low[node] = min(low[node],low[nei])
                    if low[nei] > disc[node]:
                        bridges.append([node,nei])
                else:
                    low[node] = min(low[node],disc[nei])
            return bridges
        return dfs(0,-1)
