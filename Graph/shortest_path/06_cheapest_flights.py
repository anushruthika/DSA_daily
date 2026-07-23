# 787. Cheapest Flights Within K Stops

# IN dijktsra: Once a node is popped with the minimum distance, its shortest distance is finalized . (understanding same node being reached with larger distance no considered due to relaxation step.)
#  but here. Once a node poped cant finalize:
# example: 
# (5, A, 4 stops)
# (8, A, 2 stops) 
# lets take maximum 5 stops to reach destination and # (5, A, 4 stops) unable to reach destination in 5 stops
# thus consider # (8, A, 2 stops) 

# Why is the complexity O(V^(k+1))?

# Suppose every node is connected to every other node.

# Level 0 (source):          1 node
# Level 1 (1 edge):          V nodes
# Level 2 (2 edges):         V² nodes
# Level 3 (3 edges):         V³ nodes
# ...
# Level (k+1):               V^(k+1) nodes

# Since we allow at most (k+1) edges, the algorithm may explore every possible path up to depth (k+1).

# Total states:
# 1 + V + V² + ... + V^(k+1)
# ≈ O(V^(k+1))      (last term dominates)

# Each state is pushed and popped from the heap once.

# Heap operation = O(log(V^(k+1)))

# Total Time:
# O(V^(k+1) × log(V^(k+1)))

###########################
# Time complexity
# ≈ O(V^(k+1) logV)
#######################
# SPACE COMPLEXITY

# Adjacency List : O(V + E)

# Priority Queue:
# Stores (price, node, stops) states.
# Since the algorithm does not prune duplicate states,
# it may store O(V^(k+1)) states in the worst case.

# Total Space:
# O(V + E + V^(k+1))
# = O(V^(k+1))

import heapq
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        # building adj
        # Time: O(E)
        # Space: O(V + E)
        adj = [[] for _ in range(n)]
        for u, v, w in flights:
            adj[u].append((v, w))
        
        pq = [(0,src,0)]
        while pq:
            price_node,node,stops = heapq.heappop(pq)
            if stops>k+1:
                continue
            if node == dst:
                return price_node
            for neighbour,price_nei in adj[node]:
                heapq.heappush(pq,(price_nei+price_node,neighbour,stops+1))
        return -1



# Time: O(E * k * log (V * k)) ### V: nodes E: edges K: stops 
# 1. while pq: designed to run for V*K times, due to relaxation the while pq reduces to E*K 
# 2. log(V*K) heap stores(dist,node(V),stop(K)) and is unique for (V*K) at max can store upto V*K 
# and push and pop operation in heap is log(V*E)

# Space: O(V * k + E)
# - Adjacency list → O(E)
# - 'best' dictionary stores up to V * k states
# - Heap can also hold up to V * k entries
# ⇒ Total: O(V * k + E)

import heapq

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        adj = [[] for _ in range(n)]
        for u, v, w in flights:
            adj[u].append((v, w))
        
        pq = [(0, src, 0)]  # (cost, node, stops)
        
        # store best cost for (node, stops)
        best = {}
        
        while pq:
            cost, node, stops = heapq.heappop(pq)
            
            if node == dst:
                return cost
            
            if stops > k:
                continue
            
            for nei, wt in adj[node]:
                new_cost = cost + wt
                
                # only prune if strictly worse for same (node, stops)
                if (nei, stops) not in best or best[(nei, stops)] > new_cost:
                    best[(nei, stops)] = new_cost
                    heapq.heappush(pq, (new_cost, nei, stops + 1))
        
        return -1
