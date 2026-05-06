# https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1

# Time: O((V + E) log V)
# 1=> O(logV) => heap operation to push/pop one V. O(VlogV) to push V vertex.
# 2=> O(logV) => heap operation to push/pop one V. O(ElogV) to relax E edges
# therefore, O(VlogV)+O(ElogV) = O((V+E)logV)

# Space: O(V + E)
# Adjacency list stores all edges → O(E)
# - Distance array stores V nodes → O(V)
# - Heap can hold up to V elements → O(V)
# ⇒ Total: O(V + E)

from typing import List
from collections import deque
import heapq
class Solution:

    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        
        graph = [[] for _ in range(V)]
        for u,v,w in edges:
            graph[u].append((v,w))
        
        res = [float('inf')]*V
        res[0] = 0
        pq = [(0,0)]
        while pq:
            d,x = heapq.heappop(pq)
            if d > res[x]:
              continue
            for y,w in graph[x]:
                # Edge relaxation: Can I reach y cheaper through x?
                if res[y]>res[x]+w:
                    res[y] = res[x]+w
                    heapq.heappush(pq,(res[y],y))
        for i in range(len(res)):
            if res[i] == float('inf'):
                res[i] =-1
        return res
