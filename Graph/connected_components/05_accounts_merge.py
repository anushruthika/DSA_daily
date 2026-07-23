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

from collections import defaultdict
class Solution:
    class DSU:
        def __init__(self,n):
            self.parent = [i for i in range(n)]
            self.rank = [0]*n
        def find(self,x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        def union(self,u,v):
            pu = self.find(u)
            pv = self.find(v)
            if pu == pv:
                return False
            if self.rank[pu]>self.rank[pv]:
                self.parent[pv] = self.parent[pu]
            elif self.rank[pv] >self.rank[pu]:
                self.parent[pu] = self.parent[pv]
            else:
                self.parent[pv] = self.parent[pu]
                self.rank[pu]+=1
            return True
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        dsu = self.DSU(n)
        unique_emails = defaultdict(int)

        # E     : lets take=> n*m(emails in one account)= E (total number of emails)
        # O(n*m(emails in one account)*α(N)) 

        # O(E*α(N))
        # {"johnsmith@mail.com": 0,"john_newyork@mail.com":0,"john00@mail.com":1,"mary@mail.com":2,"johnnybravo@mail.com":3 }
        for i,account in enumerate(accounts):
            for email in account[1:]:
                if email not in unique_emails:
                    unique_emails[email] = i
                else:
                    dsu.union(unique_emails[email],i)

        merged_list = defaultdict(list)
        # {0:["johnsmith@mail.com","john_newyork@mail.com"],
        # 1: ["john00@mail.com"], 2:["mary@mail.com"], 3:["johnnybravo@mail.com"]}
        
        # O(E*α(N))
        for email,node in unique_emails.items():                     # <- O(E) : runs E times 
            merged_list[dsu.find(node)].append(email)                # <- O(α(N)) : complexity of dsu.find(node)

        # O(ElogE all the emails partioned go through sorting)
        res = []
        for node,email_list in merged_list.items():
            res.append([accounts[node][0]]+sorted(email_list))
        return res
        # TC: O(E*α(N) + ElogE)
        # SC: space for DSU -> O(n) -> parent,rank array
        # O(E)-> unique_emails O(E) -> merged_list o(E) -> res
        # ans: O(n+E)
