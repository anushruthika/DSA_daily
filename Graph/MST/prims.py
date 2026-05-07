# https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1
# Time: O(E log V)
# - Building adjacency list → O(E)
# - Each edge may be pushed into heap once → O(E operations)
# - Each heap push/pop takes => log V
# ⇒ Total: O(E log V)

# Space: O(V + E)
# - Adjacency list → O(E)
# - Visited array → O(V)
# - MST array → O(V)
# - Heap can store up to O(E) edges
# ⇒ Total: O(V + E)

import heapq
class Solution:
    def spanningTree(self, V, edges):
        adj = [[] for _ in range(V)]
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
        visited = [False]*V
        mst = []
        mst_sum = 0
        pq = [(0,0,-1)]
        visited[0] = True
        while pq:
            dist,node,parent = heapq.heappop(pq)
            if not visited[node]:
                visited[node] = True
                mst.append((node,parent))
                mst_sum+=dist
            for nei,wt in adj[node]:
                if not visited[nei]:
                    heapq.heappush(pq,(wt,nei,node))
        return mst_sum
