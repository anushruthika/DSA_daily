# https://www.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1

class Solution:

    # def kosaraju(self, V, edges):
    def count_SSC(self, V, edges):
        adj = [[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)

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
    
        return len(allssc)
