
from collections import deque

class Solution:
    def shortestPath(self, V, edges, src):
        graph = [[] for _ in range(V)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)  # if undirected

        res_path_score = [-1] * V
        res_path_score[src] = 0

        queue = deque([src])

        while queue:
            node = queue.popleft()

            for nei in graph[node]:
                if res_path_score[nei] == -1:
                    res_path_score[nei] = res_path_score[node] + 1
                    queue.append(nei)

        return res_path_score
