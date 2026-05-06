# https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1

# Time: O(V * E)
# push/pop in queue is O(1)
# - Each edge can be relaxed multiple (V)times=> V*E (but in dijskstra logV times therefore E*logV)
# - In total, up to V relaxations per edge → O(V * E)

# Space: O(V + E)
# - Adjacency list stores edges → O(E)
# - Distance array → O(V)
# - Queue → up to O(V)

# If weights exist → use Dijkstra (priority queue) O((V + E) log V)  ✅ guaranteed

from typing import List
from collections import deque

class Solution:

    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        
        graph = [[] for _ in range(V)]
        for u,v,w in edges:
            graph[u].append((v,w))
        queue = deque([0])
        res = [float('inf')]*V
        res[0] = 0
        while queue:
            x = queue.popleft()
            for y,w in graph[x]:
                if res[y]>res[x]+w:
                    res[y] = res[x]+w
                    queue.append(y)
        for i in range(len(res)):
            if res[i] == float('inf'):
                res[i] =-1
        return res
