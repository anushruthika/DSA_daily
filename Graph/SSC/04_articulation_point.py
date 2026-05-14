# https://www.geeksforgeeks.org/problems/articulation-point-1/1
# Time Complexity : O(V + E)
# Space Complexity: O(V)
class Solution:
    def articulationPoints(self, V, adj):
        disc = [-1]*V
        low = [-1]*V
        timer = [0]
        ap = set()
        def dfs(node,parent):
            timer[0]+=1
            disc[node] = low[node] = timer[0]
            children = 0
            
            for nei in adj[node]:
                if disc[nei] ==-1:
                    children+=1
                    dfs(nei,node)
                    low[node] = min(low[node],low[nei])
                    if parent == -1 and children>1:
                        ap.add(node)
                    if parent!=-1 and disc[node]<=low[nei]:
                        ap.add(node)
                elif nei!=parent:
                    low[node] = min(low[node],disc[nei])
        for node in range(V):
            if disc[node] ==-1:
                dfs(node,-1)
        return [-1] if len(ap)==0 else sorted(ap)
        
