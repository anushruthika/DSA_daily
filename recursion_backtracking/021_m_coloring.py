# https://www.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1

class Solution:
    def graphColoring(self, v, edges, m):
        adj = [[] for _ in range(v)]
        for u,nei in edges:
            adj[u].append(nei)
            adj[nei].append(u)
        res=[-1]*v
        def dfs(node):
            if node == v:
                return True
            colors = set()
            for nei in adj[node]:
                colors.add(res[nei])
            for i in range(1,m+1):
                if i not in colors:
                    res[node] = i
                    if not dfs(node+1):
                        res[node] = -1
                    else:
                        return True
            return False
        
        return dfs(0)


# 1042. Flower Planting With No Adjacent

class Solution:
    def gardenNoAdj(self, n: int, paths: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(n)]
        for u,v in paths:
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
        res = [-1]*n
        def dfs(node):
            if node == n:
                return True
            colors = set()
            for nei in adj[node]:
                colors.add(res[nei])
            for i in range(1,4+1):
                if i not in colors:
                    res[node] = i
                    if not dfs(node+1):
                        res[node] = -1
                    else:
                        return True
        dfs(0)
        return res
            
