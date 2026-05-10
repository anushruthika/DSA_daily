class DisjointSet:
    
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    # Find parent with path compression
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # Union by rank
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False   # already connected

        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv

        elif self.rank[pv] < self.rank[pu]:
            self.parent[pv] = pu

        else:
            self.parent[pv] = pu
            self.rank[pu] += 1

        return True
        
ds = DisjointSet(5)

ds.union(0, 1)
ds.union(1, 2)

print(ds.find(2))   




class DSU:
    
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    # Find with path compression
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # Union by size
    def union(self, u, v):

        pu = self.find(u)
        pv = self.find(v)

        # already connected
        if pu == pv:
            return False

        # attach smaller component to larger component
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu

        self.parent[pv] = pu
        self.size[pu] += self.size[pv]

        return True
