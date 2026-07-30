# 3608. Minimum Time for K Connected Components

class Solution:
    class DSU:
        def __init__(self,n:int):
            self.parent = [i for i in range(n)]
            self.rank = [0]*n
        def find(self,x):
            if self.parent[x]!=x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        def union(self,u,v):
            pu = self.find(u)
            pv = self.find(v)
            if pu == pv:
                return False
            if self.rank[pu]>self.rank[pv]:
                self.parent[pv] = pu
            elif self.rank[pv]>self.rank[pu]:
                self.parent[pu] = pv
            else:
                self.parent[pv] = pu
                self.rank[pu]+=1
            return True
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        edges.sort(key = lambda x:x[2],reverse=True)
        # number of components: disconnected.
        components = n
        dsu = self.DSU(n)
        for u,v,w in edges:
            if dsu.union(u,v):
                components-=1
            if components<k:
                return w
        return 0
