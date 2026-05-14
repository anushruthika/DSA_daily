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
