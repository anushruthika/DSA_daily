# 76. Minimum Window Substring
# TC: O(n) SC: O(k)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = {}
        for i in t:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        i=0
        j=0
        n = len(s)
        m = len(t)
        l = float('inf')
        res=""
        matched = 0
        # required should not be n (because we may have duplicates so count may increase)
        required = len(d)
        while j<n:
            if s[j] in d:
                d[s[j]]-=1
                if d[s[j]] ==0:
                    matched+=1
            while matched==required:
                if l>len(s[i:j+1]):
                    l = len(s[i:j+1])
                    res=s[i:j+1]
                if s[i] in d:
                    if d[s[i]] == 0:
                        matched-=1
                    d[s[i]]+=1
                    
                i+=1
            j+=1
        return res


# TC: O(n*k) SC : O(k)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = {}
        for i in t:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        i=0
        j=0
        n = len(s)
        m = len(t)
        l = float('inf')
        res=""
        while j<n:
            if s[j] in d:
                d[s[j]]-=1
            while all(value <= 0 for value in d.values()):
                
                if l>len(s[i:j+1]):
                    l = len(s[i:j+1])
                    # print(s[i:j+1])
                    res=s[i:j+1]
                if s[i] in d:
                    d[s[i]]+=1
                i+=1
            j+=1
        return res

