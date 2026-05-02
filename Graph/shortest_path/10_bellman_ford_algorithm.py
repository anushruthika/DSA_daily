# https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1

# shortest paths from a single source vertex to all other vertices in a weighted graph.
# can have negative edges
# slower than dijkstra Time O((V+E) log V) bellman: O(V × E)
# graph can be both directed and undirected. 

# After doing V−1 relaxations, all shortest paths are finalized.
# If in the next (V-th) check any distance still improves → negative cycle exists.

# Time: O(V * E)
# Relax all E edges for (V - 1) iterations → O(V * E)
# + one extra O(E) pass for cycle check (ignored in final)

# Space: O(V)
# Distance array stores V values

class Solution:
    def bellmanFord(self, V, edges, src):
        dist = [10**8]*V
        dist[src] = 0
        for i in range(V-1):
            for u,v,w in edges:
                # Relaxation : reset dist[v] with short paths
                if dist[u]!=10**8 and dist[u]+w<dist[v]:
                    dist[v] = dist[u]+w
        for u,v,w in edges:
            if dist[u]!=10**8 and dist[u]+w<dist[v]:
                return [-1]
        return dist
