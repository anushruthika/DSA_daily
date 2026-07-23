# DSU : disjoint set : union by rank and size
# - dynamic graph ( when graph grows dynamically)
# - DSU is a data structure that efficiently keeps track of connected components by supporting fast union (merge) and find (identify the set representative) operations.
# - DSU operations (find and union) run in nearly constant time, specifically O(α(n)), where α is the inverse Ackermann function. inverse Ackermann function grows extremely slowly.

# # - Union by RANK
# # (1-based idexinig to explain example but code uses 0-based indexing)
# eg: (1,2) (2,3) (4,5) (6,7) (5,6) (3,7)
# # two arrays: 
# 1. parent: [1,2,3,4,5,6,7]
# 2. rank: [0,0,0,0,0,0,0]
# # union(u,v):
# rules; 
# 1. find ultimate parent of u & v which is pu,pv
# 2. find rank of pu & pv
# 3. connect smaller rank to larger rank , incase of equality we can connect any one to anyone


# | Edge                                                   | `find(u)` (`pu`) | `find(v)` (`pv`) | Rank(`pu`) | Rank(`pv`) | Action                                                       | Parent Array          | Rank Array        |
# | ------------------------------------------------------ | ---------------: | ---------------: | ---------: | ---------: | ------------------------------------------------------------ | --------------------- | ----------------- |
# | **Initial**                                            |                - |                - |          - |          - | Initialize                                                   | `[1,2,3,4,5,6,7]`     | `[0,0,0,0,0,0,0]` |
# | **(1,2)**                                              |                1 |                2 |          0 |          0 | Equal rank → make **1** parent of **2**, increment rank of 1 | `[1,1,3,4,5,6,7]`     | `[1,0,0,0,0,0,0]` |
# | **(2,3)**                                              |                1 |                3 |          1 |          0 | Rank(1)>Rank(3) → make **1** parent of **3**                 | `[1,1,1,4,5,6,7]`     | `[1,0,0,0,0,0,0]` |
# | **(4,5)**                                              |                4 |                5 |          0 |          0 | Equal rank → make **4** parent of **5**, increment rank of 4 | `[1,1,1,4,4,6,7]`     | `[1,0,0,1,0,0,0]` |
# | **(6,7)**                                              |                6 |                7 |          0 |          0 | Equal rank → make **6** parent of **7**, increment rank of 6 | `[1,1,1,4,4,6,6]`     | `[1,0,0,1,0,1,0]` |
# | **(5,6)**                                              |                4 |                6 |          1 |          1 | Equal rank → make **4** parent of **6**, increment rank of 4 | `[1,1,1,4,4,4,6]`     | `[1,0,0,2,0,1,0]` |
# | **(3,7)**                                              |                1 |      4 *(7→6→4)* |          1 |          2 | Rank(4)>Rank(1) → make **4** parent of **1**                 | `[4,1,1,4,4,4,6]`     | `[1,0,0,2,0,1,0]` |
# | **Path Compression** (`find(2)`, `find(3)`, `find(7)`) |                4 |                4 |          - |          - | Update every visited node to point directly to the root (4)  | **`[4,4,4,4,4,4,4]`** | `[1,0,0,2,0,1,0]` |



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
