# https://www.geeksforgeeks.org/problems/strongly-connected-component-tarjanss-algo-1587115621/1

# Time Complexity  : O(V + E) => Every node visited once O(v) , Every edge traversed once O(E)
# Space Complexity : O(V) disc ,low , inSt => stores of size V

# Understanding
# If a subtree cant reach the ancestor node except through its parent edge. then the parentedge is a bridge
# removing that bridge divides the graph into two different components
# strongly connected nodes
# disc => time of insertion, 
# low => lowest time of insertion (helps us track a back edge) if backe edge exists the node is not a root.

# time: O(V+E)
# space: O(v)
class Solution:

    # Function to find all Strongly Connected Components using Tarjan's Algorithm
    def tarjans(self, V, adj):

        disc = [-1]*V
        low = [-1]*V
        instack = [False]*V
        stack = []
        allssc=[]
        timer = [0]
        def dfs(node):
            timer[0]+=1
            low[node]=disc[node]=timer[0]
            instack[node] = True
            stack.append(node)
            for nei in adj[node]:
                if disc[nei] == -1:
                    dfs(nei)
                    low[node] = min(low[node],low[nei])
                elif instack[nei]:
                    low[node] = min(low[node],disc[nei])
                    
            if low[node] == disc[node]:
                ssc = []
                while True:
                    x = stack.pop()
                    instack[x] = False
                    ssc.append(x)
                    if x == node:
                        break
                ssc.sort()
                allssc.append(ssc)
        for i in range(V):
            if disc[i] == -1:
                dfs(i)
    
        return sorted(allssc)

# | Step    | Action             | Stack           | disc                  | low                   | inStack         |
# | ------- | ------------------ | --------------- | --------------------- | --------------------- | --------------- |
# | Initial | Start              | `[]`            | `[-1,-1,-1,-1,-1,-1]` | `[-1,-1,-1,-1,-1,-1]` | `[F,F,F,F,F,F]` |
# | 1       | DFS(0)             | `[0]`           | `[1,-1,-1,-1,-1,-1]`  | `[1,-1,-1,-1,-1,-1]`  | `[T,F,F,F,F,F]` |
# | 2       | DFS(1)             | `[0,1]`         | `[1,2,-1,-1,-1,-1]`   | `[1,2,-1,-1,-1,-1]`   | `[T,T,F,F,F,F]` |
# | 3       | DFS(2)             | `[0,1,2]`       | `[1,2,3,-1,-1,-1]`    | `[1,2,3,-1,-1,-1]`    | `[T,T,T,F,F,F]` |
# | 4       | Back edge `2 → 0`  | `[0,1,2]`       | `[1,2,3,-1,-1,-1]`    | `[1,2,1,-1,-1,-1]`    | `[T,T,T,F,F,F]` |
# | 5       | DFS(3) from node 2 | `[0,1,2,3]`     | `[1,2,3,4,-1,-1]`     | `[1,2,1,4,-1,-1]`     | `[T,T,T,T,F,F]` |
# | 6       | DFS(4)             | `[0,1,2,3,4]`   | `[1,2,3,4,5,-1]`      | `[1,2,1,4,5,-1]`      | `[T,T,T,T,T,F]` |
# | 7       | Back edge `4 → 3`  | `[0,1,2,3,4]`   | `[1,2,3,4,5,-1]`      | `[1,2,1,4,4,-1]`      | `[T,T,T,T,T,F]` |
# | 8       | DFS(5)             | `[0,1,2,3,4,5]` | `[1,2,3,4,5,6]`       | `[1,2,1,4,4,6]`       | `[T,T,T,T,T,T]` |
# | 9       | SCC found at 5     | `[0,1,2,3,4]`   | `[1,2,3,4,5,6]`       | `[1,2,1,4,4,6]`       | `[T,T,T,T,T,F]` |
# | 10      | Return to DFS(4)   | `[0,1,2,3,4]`   | `[1,2,3,4,5,6]`       | `[1,2,1,4,4,6]`       | `[T,T,T,T,T,F]` |
# | 11      | Return to DFS(3)   | `[0,1,2,3,4]`   | `[1,2,3,4,5,6]`       | `[1,2,1,4,4,6]`       | `[T,T,T,T,T,F]` |
# | 12      | SCC found at 3     | `[0,1,2]`       | `[1,2,3,4,5,6]`       | `[1,2,1,4,4,6]`       | `[T,T,T,F,F,F]` |
# | 13      | Return to DFS(2)   | `[0,1,2]`       | `[1,2,3,4,5,6]`       | `[1,2,1,4,4,6]`       | `[T,T,T,F,F,F]` |
# | 14      | Return to DFS(1)   | `[0,1,2]`       | `[1,2,3,4,5,6]`       | `[1,1,1,4,4,6]`       | `[T,T,T,F,F,F]` |
# | 15      | Return to DFS(0)   | `[0,1,2]`       | `[1,2,3,4,5,6]`       | `[1,1,1,4,4,6]`       | `[T,T,T,F,F,F]` |
# | 16      | SCC found at 0     | `[]`            | `[1,2,3,4,5,6]`       | `[1,1,1,4,4,6]`       | `[F,F,F,F,F,F]` |

