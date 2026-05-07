# 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance

# Time: O(V * (V + E) log V)
# O(V) times outer loop : "for i in range(n):" ln runs 
# inside outer loop inner loop runs ( while pq )=> inside inner loop: for nei in adj[node]=>=>=> O(V+E) times
# therefore O(V*(V+E)) runs.
# internally O(logV) for push/pop in heap

# Space: O(V + E)

# Adjacency list: O(V + E)
# Distance array: O(V)
# Priority queue: O(E) in worst case

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        min_nodes = float('inf')
        res_node = -1
        for i in range(n):
            pq = [(0,i)]
            res = [float('inf')]*n
            res[i] = 0
            while pq:
                dist,node = heapq.heappop(pq)
                for nei,wt in adj[node]:
                    if res[nei] > res[node]+wt:
                        res[nei] = res[node]+wt 
                        heapq.heappush(pq,(res[nei],nei))
            count = 0
            for j in range(len(res)):
                if j!=i and res[j]<=distanceThreshold:
                    count+=1
            if count<=min_nodes:
                min_nodes = count
                res_node = i
        return res_node
