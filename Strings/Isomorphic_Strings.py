class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n=len(s)
        if n != len(t):
            return False
        d={}
        for i in range(n):
            x = t[i] in d.values()
            if s[i] not in d:
                if not(x):
                    d[s[i]]=t[i]
                else:
                    return False
            elif d[s[i]]!=t[i]:
                return False
        return True

        
