# https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1

# Time Complexity:
# O(V^2 + E)
# - Each time we pick min(set_) → O(V) (linear scan over set)
# - This happens up to V times → O(V^2)
# - For each node, we relax its edges → total O(E)
# Overall: O(V^2 + E)

# Space Complexity:
# O(V + E)
# - Adjacency list → O(E)
# - Distance array → O(V)
# - Set can hold up to O(V) elements

# Time: O(V^2 + E)
# Space: O(V + E)
import heapq
from typing import List
class Solution:
    def shortestPath(self, V: int, E: int,edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(V)]
        for u,v,w in edges:
            adj[u].append((v,w))
        set_ds = set([(0,0)])
        res = [float('inf')]*V
        res[0] = 0
        
        while set_ds:
            dist,node = min(set_ds)
            set_ds.remove((dist,node))
            if dist>res[node]:
                continue
            for nei,wt in adj[node]:
                if res[nei]>res[node]+wt:
                    res[nei] = res[node]+wt
                    set_ds.add((res[nei],nei))
        for i in range(len(res)):
            if res[i] == float('inf'):
                res[i] =-1
        return res
