# https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1




# time complexity: 
        # 1. build adj : O(V+E)
        # 2. 
        #  == > while+for loop to traverse each edge and reach nei:  O(E)
        #  == > internal push pop into pq:  log(E)
        # ==> O(ElogE) 
# but for simlicity to represent TC in 2 variables such as E & V we use O(ElogV)
# understanding for :
                # Directed fully connected graph:
                # E = V(V − 1)
                # Undirected fully connected graph:
                # E = V(V − 1) / 2
                
                # In Big-O notation:
                # Directed:
                # V(V − 1) = O(V²)
                # Undirected:
                # V(V − 1) / 2 = O(V²)
# in general usecase: V**2>> E
# considering: for heap push pop as : O(logE) = O(logV**2) = O(2logV) = O(logV) in Big-O
# thus Time complexity is O(ElogV)

# why not O(V**2logV)? because it would be very wrong to assume E=V**2 as in average case we can generalize a graph to have V**2 edges
thus,

####################### TIME COMPLEXITY
# average case: O(ElogV)+O(V+E) =  O(E logV) as O(ElogV) >> O(V+E)
# worst case: O(V**2logV) 
####################### SPACE COMPLEXITY
# adj list: O(V+E)
# heap: O(E) as max all edges
# dist array: O(V)
# total : O(V+E)
#######################################

from typing import List
from collections import deque
import heapq
class Solution:

    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        # build adj list : O(V+E)                
        graph = [[] for _ in range(V)]         # <- O(V)
        for u,v,w in edges:                    # <- O(E)
            graph[u].append((v,w))
        
        res = [float('inf')]*V
        res[0] = 0
        pq = [(0,0)]
        
        while pq:                        # <- O(E): Each pushed edge is eventually popped, so loop runs at max O(E) times.
            d,x = heapq.heappop(pq)      # heap pop O(logE) (as heap can have max size of E)
            if d > res[x]:
              continue
            for y,w in graph[x]:
                # Edge relaxation: Can I reach y cheaper through x?
                if res[y]>res[x]+w:
                    res[y] = res[x]+w
                    heapq.heappush(pq,(res[y],y))        # heap push O(logE) (as heap can have max size of E)
        for i in range(len(res)):
            if res[i] == float('inf'):
                res[i] =-1
        return res
