# 787. Cheapest Flights Within K Stops

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
