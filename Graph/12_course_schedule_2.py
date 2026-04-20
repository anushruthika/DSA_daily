# Time: O(V + E) => we visit each course once (V) and traverse each prerequisite edge once (E)
# Space: O(V + E) => adjacency list stores edges + visited/path arrays + recursion stack (worst case V)

# 210. Course Schedule II

# DFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for pre, course in prerequisites:
            adj[course].append(pre)
        visited = [False]*numCourses
        path = [False]*numCourses
        res=[]
        def isCycle(node):
            visited[node]=path[node]=True
            for val in adj[node]:
                if not visited[val]:
                    if isCycle(val):
                        return True
                elif path[val]:
                    return True
            res.append(node)
            path[node] = False
            return False
        
        for i in range(numCourses):
            if not visited[i]:
                if isCycle(i):
                    return []
        return res[::-1]

# BFS:= Khans algorithm
class Solution:
    def findOrder(self, V: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(V)]
        indegree=[0]*V
        for i,j in edges:
            adj[j].append(i)
            indegree[i]+=1
        visited = [False]*V
        stack = []
        res=[]
        for i in range(V):
            if indegree[i] == 0:
                stack.append(i)
        while stack:
            node = stack.pop()
            res.append(node)
            print(adj[node],node)
            for path_node in adj[node]:
                indegree[path_node]-=1
                if indegree[path_node] == 0:
                    stack.append(path_node)
        if len(res)!=V:
            return []
        return res
