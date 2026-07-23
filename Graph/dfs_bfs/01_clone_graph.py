# 133. Clone Graph

# TC : O(V+E):
# Every node is visited once → O(V)
# Every edge is traversed once → O(E)
# SC : O(V)
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        # Stores the copied values & acts like a visited array too
        copied = {}
        def dfs(node):
            # check if already visited
            if node in copied:
                return copied[node]
            copied[node] = Node(node.val,[])
            for nei in node.neighbors:
                #### DONT FORGET PERFORM DFS(NEI) explore NEIGHBOURS
                copied[node].neighbors.append(dfs(nei))
            return copied[node]
        return dfs(node)
