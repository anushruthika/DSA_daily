# 207. Course Schedule


####
# DFS
####
# Time: O(V + E) => each node and edge is visited once during DFS
# Space: O(V) => visited + path arrays + recursion stack (worst O(V), best O(log V) depending on graph depth)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]
        for pre,course in prerequisites:
            adj[course].append(pre)
        visited = [False]*numCourses
        path = [False]*numCourses
        def is_cycle_dfs(node):
            visited[node] = path[node] = True
            # each edge is visted once. 
            for next_node in adj[node]:
                if not visited[next_node]:
                    if is_cycle_dfs(next_node):
                        return True
                elif path[next_node]:
                    return True
            path[node] = False
            return False
        # each vertex visted
        for i in range(numCourses):
            if not visited[i]:
                if is_cycle_dfs(i):
                        return False
        return True
