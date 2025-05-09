class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        if len(s)!=len(t):
            return False
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1 
        for i in t:
            if i not in d:
                return False
            elif d[i]==0:
                return False
            else:
                d[i]-=1
        return True
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
