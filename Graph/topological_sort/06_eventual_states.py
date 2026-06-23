# similar to course schdeule 2. but if it consists loop dont return immediately.

# | Solution          | Time             | Space    |
# | ----------------- | ---------------- | -------- |
# | Topological sort+ sort(stack) | O(V + E + VlogV) | O(V)     |
# | Reverse graph DFS | O(V + E)         | O(V + E) |

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        
        stack = []
        path = [False] * V
        visited = [False] * V
        
        def dfs(node):
            visited[node] = path[node] = True
            
            for nei in graph[node]:
                if not visited[nei]:
                    if not dfs(nei):
                        return False
                elif path[nei]:
                    return False
            
            path[node] = False
            stack.append(node)   
            return True
        
        for i in range(V):
            if not visited[i]:
                dfs(i)
        
        return sorted(stack)   # sort because order doesn't matter

# inv matrix
from typing import List
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        
        # build reverse graph
        inv_adj = [[] for _ in range(V)]
        for u in range(V):
            for v in graph[u]:
                inv_adj[v].append(u)
        
        visited = [False] * V
        path = [False] * V
        safe = [False] * V   # track safe nodes
        
        def dfs(node):
            visited[node] = path[node] = True
            
            for nei in graph[node]:   # 🔥 IMPORTANT: use original graph here
                if not visited[nei]:
                    if not dfs(nei):
                        return False
                elif path[nei]:
                    return False
            
            path[node] = False
            safe[node] = True   # mark safe
            return True
        
        for i in range(V):
            if not visited[i]:
                dfs(i)
        
        return [i for i in range(V) if safe[i]]

  class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        res = []
        visited = set()
        memo = [0] * n

        def dfs(i):
            if memo[i] == 1 or len(graph[i]) == 0:
                return True
            elif memo[i] == -1 or i in visited:
                return False
            
            visited.add(i)
            
            for neighbour in graph[i]:
                if not dfs(neighbour):
                    memo[i] = -1
                    return False

            memo[i] = 1
            return True
        
        for i in range(n):
            if dfs(i):
                res.append(i)
        
        return res
