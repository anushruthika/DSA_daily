# 785. Is Graph Bipartite?

# Time: O(V + E) => each node is visited once and each edge is checked once during DFS
# Space: O(V) => color dictionary + recursion stack (worst case depth = V)

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}

        def dfs(node,col):
            # print(color)
            color[node] = col
            for val in graph[node]:
                if val in color:
                    if color[val] == col:
                        return False
                    continue
                elif not dfs(val,1-col):
                    return False
            return True
        for x in range(len(graph)):
            if x not in color:
                if not dfs(x,0):
                    return False

        return True
