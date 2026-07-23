# 787. Cheapest Flights Within K Stops


### Using dijkstra

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


# Time Complexity:
# O(E * k * log(E * k))
# Reason:
# - We treat (node, stops) as a state → total states ≈ O(n * k)
# - From each state, we explore outgoing edges → total transitions ≈ O(E * k)
# - Each transition may push into heap
# - Heap operations (push/pop) take O(log(number_of_states)) ≈ O(log(E * k))
# - So overall = O(E * k * log(E * k))

# Space Complexity:
# O(n * k + E)
# Reason:
# - best dictionary stores (node, stops) → O(n * k)
# - heap can grow up to O(E * k) in worst case
# - adjacency list stores graph → O(E)
# - Dominant terms → O(n*k + E)
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = [[] for _ in range(n)]
        for p,q,r in flights:
            adj_list[p].append((q,r))
        # cost/dist,stops,src
        pq=[(0,src,0)]
        # best[(node, stops)] = min cost
        best = {}
        while pq:
            dist,node,stops = heapq.heappop(pq)
            if node == dst:
                return dist
            if stops>k:
                continue
            if (node,stops) in best and best[(node,stops)]<=dist:
                continue
            best[(node,stops)]= dist
            for node_dest,nei_dist in adj_list[node]:
                    heapq.heappush(pq,(dist+nei_dist,node_dest,stops+1))
        return -1
