# 205. Isomorphic Strings

# TC: O(n)
# SC: O(n)

# d = {'e':'a', 'g':'d'}
# edge case: 
# s = 'badc' t = 'efft'
# d = {b:e, a:f, d:f, c:t}
# Thus need a set or d.values() to track the mapping of t->s
from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        len_string1 = len(s)
        len_string2 = len(t)
        # edge case: strings are not of same size
        if len_string1 != len_string2:
            return False
        d = defaultdict(str)
        # s = set()
        for i in range(len_string1):
            if (s[i] in d and d[s[i]]!=t[i]) or (s[i] not in d and t[i] in d.values()):
                return False
            # if s[i] in d and d[s[i]]==t[i]:
            #     pass
            if s[i] not in d and t[i] not in d.values():
                d[s[i]] = t[i]
        return True


            

            
        
