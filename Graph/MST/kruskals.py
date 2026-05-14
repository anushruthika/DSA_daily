# Time Complexity: O(E log E)
# Space Complexity: O(V)

from typing import List


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
            return False

        if self.rank[pu] < self.rank[pv]:

            self.parent[pu] = pv

        elif self.rank[pv] < self.rank[pu]:

            self.parent[pv] = pu

        else:

            self.parent[pv] = pu

            self.rank[pu] += 1

        return True


class Solution:

    def kruskalsMST(self, V: int, edges: List[List[int]]) -> int:

        # Sort edges based on weight
        edges.sort(key=lambda x: x[2])

        ds = DisjointSet(V)

        mst_weight = 0
        mst_list = []
        for u, v, w in edges:

            # If edge does not form cycle
            if ds.union(u, v):
                mst_list.append([u,v])
                mst_weight += w

        return mst_weight
