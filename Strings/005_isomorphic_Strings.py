# 205. Isomorphic Strings

# TC: O(n)
# SC: O(n)
# consider edge case:
# s = "badc" t = "baba" reason to create vals

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #  track mapping of key & values
        d = {}
        # track values
        vals = set()
        i = 0
        # j = 0
        n1 = len(s)
        n2 = len(t)
        if n1!=n2:
            return False
        while i<n1:
            # no need i<n1 and j<n2: as n1 n2 are same
            if s[i] not in d:
                if t[i] in vals:
                    return False
                d[s[i]] = t[i]
                vals.add(t[i])
            # s[i] is in d thus no need to check here as the oppposite condition was captured above
            elif d[s[i]]!=t[i]:
                return False
            i+=1
        return True

            

            
        
