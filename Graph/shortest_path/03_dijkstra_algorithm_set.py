# https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1

# Time: O(V^2 + E)
# Space: O(V + E)
from typing import List
class Solution:

    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        
        graph = [[] for _ in range(V)]
        for u,v,w in edges:
            graph[u].append((v,w))
        
        res = [float('inf')]*V
        res[0] = 0
        set_ds=set()
        set_ds.add((0,0))
        while set_ds:
            d,x = min(set_ds)
            set_ds.remove((d,x))
            for y,w in graph[x]:
                if res[y]>res[x]+w:
                    # 🔥 remove old pair if exists
                    if res[y] != float('inf'):
                        set_ds.discard((res[y], y))
                    res[y] = res[x]+w
                    set_ds.add((res[y],y))
        for i in range(len(res)):
            if res[i] == float('inf'):
                res[i] =-1
        return res
