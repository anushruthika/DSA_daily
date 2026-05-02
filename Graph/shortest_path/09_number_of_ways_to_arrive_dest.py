# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/
# Time: O((V + E) log V)
#   Reason:
#   - Building adjacency list takes O(E)
#   - Each edge relaxation can push into heap → up to O(E) pushes
#   - Each heap operation (push/pop) costs O(log V)

# Worst-case Time: O(E log V)
#   Reason:
#   - In dense graphs, E dominates V, so total operations scale with edges

# Space: O(V + E)
#   Reason:
#   - Adjacency list stores all edges → O(E)
#   - Distance array + ways array → O(V)
#   - Heap can grow up to O(E) in worst case
import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        adj = [[] for _ in range(n)]
        
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        res = [float('inf')] * n
        ways = [0]*n
        res[0] = 0
        ways[0] = 1
        pq = [(0,0)]  # (distance, node)
        
        while pq:
            dist, node = heapq.heappop(pq)
            
            if dist > res[node]:
                continue
            
            for nei, weight in adj[node]:
                new_dist = dist + weight
                
                if new_dist < res[nei]:
                    res[nei] = new_dist
                    ways[nei] = ways[node]
                    heapq.heappush(pq, (new_dist, nei))
                elif new_dist == res[nei]:
                    ways[nei] = (ways[nei]+ways[node]) % MOD
        return ways[n-1]
        
