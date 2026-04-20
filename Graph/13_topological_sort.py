# https://www.geeksforgeeks.org/problems/topological-sort/1
# topological sorting => can be done only in DAG


# DFS

# Time: O(V + E) => building adjacency list takes O(E), and DFS visits each node and edge once
# Space: O(V + E) => adjacency list stores all edges + visited array + recursion stack (worst case O(V))
class Solution:
    def topoSort(self, V, edges):
        adj = [[] for _ in range(V)]
        for i,j in edges:
            adj[i].append(j)
        # print(adj)
        visited = [False]*V
        stack = []
        def dfs(node):
            visited[node]=True
            for path in adj[node]:
                if not visited[path]:
                    dfs(path)
            stack.append(node)
        for i in range(V):
            if not visited[i]:
                dfs(i)
                # print(visited,stack)
        # print(stack[::-1])
        return stack[::-1]

# BFS = Khans algorithm - indegree instead of visited 
# https://www.youtube.com/watch?v=73sneFXuTEg

# Time: O(V + E) => building adjacency list takes O(E), and each node + edge is processed once in Kahn’s algorithm

# Space: O(V + E) => adjacency list stores edges + indegree array + stack + result list
class Solution:
    def topoSort(self, V, edges):
        adj = [[] for _ in range(V)]
        indegree=[0]*V
        for i,j in edges:
            adj[i].append(j)
            indegree[j]+=1
        
        # print(adj,indegree)
        stack=[]
        res=[]
        for i in range(V):
            if indegree[i] == 0:
                stack.append(i)
        while stack:
            node = stack.pop()
            res.append(node)
            for path in adj[node]:
                indegree[path]-=1
                if indegree[path] == 0:
                    stack.append(path)
        return res

