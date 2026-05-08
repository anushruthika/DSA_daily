# 947. Most Stones Removed with Same Row or Column

# Time: O(n^2)
# - Compare every pair of stones to build graph

# Space: O(n^2)
# - Adjacency list can store up to O(n^2) edges
# - Visited array + recursion stack → O(n)

class Solution:
    def removeStones(self, stones):
        
        n = len(stones)

        # build graph
        adj = [[] for _ in range(n)]

        for i in range(n):
            x1, y1 = stones[i]

            for j in range(i + 1, n):
                x2, y2 = stones[j]

                if x1 == x2 or y1 == y2:
                    adj[i].append(j)
                    adj[j].append(i)

        print(adj)
        visited = [False] * n

        def dfs(node):
            visited[node] = True

            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei)

        components = 0

        for i in range(n):
            if not visited[i]:
                components += 1
                dfs(i)

        return n - components


  #######
      # DISJOINT SET
#######


class DisjointSet:
    
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return

        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv

        elif self.rank[pv] < self.rank[pu]:
            self.parent[pv] = pu

        else:
            self.parent[pv] = pu
            self.rank[pu] += 1


class Solution:
    def removeStones(self, stones):
        
        n = len(stones)

        ds = DisjointSet(n)

        # connect stones sharing same row or column
        for i in range(n):
            for j in range(i + 1, n):

                x1, y1 = stones[i]
                x2, y2 = stones[j]

                if x1 == x2 or y1 == y2:
                    ds.union(i, j)

        # count connected components
        components = 0

        for i in range(n):
            if ds.find(i) == i:
                components += 1

        return n - components

        return n - components
