# https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1

# Time: O((V + E) log V)
# Space: O(V + E)

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
                if res[y]>res[x]+w:
                    res[y] = res[x]+w
                    heapq.heappush(pq,(res[y],y))
        for i in range(len(res)):
            if res[i] == float('inf'):
                res[i] =-1
        return res
