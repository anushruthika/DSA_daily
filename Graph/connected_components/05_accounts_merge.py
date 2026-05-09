# 721. Accounts Merge

# Time: O(E * α(N) + E log E)

# - E = total number of emails
# - N = number of accounts

# - Traversing all emails + union/find operations → O(E * α(N))
#   (α(N) is nearly constant)

# - Sorting merged emails:
#   In worst case all emails belong to one account → O(E log E)

# ⇒ Total: O(E * α(N) + E log E)


# Space: O(N + E)

# - Parent + rank arrays → O(N)
# - uniq_emails hashmap → O(E)
# - merged hashmap → O(E)
# - result stores all emails → O(E)

# ⇒ Total: O(N + E)

from collections import defaultdict

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
    def accountsMerge(self, accounts):
        n = len(accounts)
        dsu = DisjointSet(n)

        uniq_emails = defaultdict(list)
        for i,l in enumerate(accounts):
            for acc in l[1:]:
                if acc not in uniq_emails:
                    uniq_emails[acc] = i
                else:
                    dsu.union(uniq_emails[acc],i)
        merged = defaultdict(list)

        for email,node in uniq_emails.items():
            merged[dsu.find(node)].append(email)
        res = []
        for name,emails in merged.items():
            res.append([accounts[name][0]]+sorted(emails))
        return res
