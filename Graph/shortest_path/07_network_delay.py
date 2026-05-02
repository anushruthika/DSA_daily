# 743. Network Delay Time

# Time: O((V + E) log V)
#   Reason:
#   - Each node can be pushed into the heap multiple times, but effectively
#     each edge relaxation leads to at most one useful push → O(E) pushes.
#   - Each push/pop from heap costs O(log V).
#   - So total = O(E log V) ≈ O((V + E) log V)

# Worst-case Time: O(E log V)
#   Reason:
#   - In dense graphs, E can be much larger than V, so this dominates.

# Space: O(V + E)
#   Reason:
#   - Adjacency list stores all edges → O(E)
#   - Distance array stores V nodes → O(V)
#   - Heap can grow up to O(E) in worst case
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        
        for u, v, w in times:
            adj[u-1].append((v-1, w))
        
        res = [float('inf')] * n
        res[k-1] = 0
        
        pq = [(0, k-1)]  # (distance, node)
        
        while pq:
            dist, node = heapq.heappop(pq)
            
            if dist > res[node]:
                continue
            
            for nei, weight in adj[node]:
                new_dist = dist + weight
                
                if new_dist < res[nei]:
                    res[nei] = new_dist
                    heapq.heappush(pq, (new_dist, nei))
        
        ans = max(res)
        return ans if ans != float('inf') else -1
