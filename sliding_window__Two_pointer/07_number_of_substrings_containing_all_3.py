# 1358. Number of Substrings Containing All Three Characters

# Time Complexity: O(n)
# Space Complexity: O(1)
# Reason:
# Hashmap stores only 3 characters: a, b, c. constant space
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d = {'a':0,'b':0,'c':0}
        i=0
        j=0
        c=0
        n = len(s)
        while j<n:
            d[s[j]] +=1
            while j-i>=2 and d['a']>0 and d['b']>0 and d['c']>0:
                c+=n-j
                d[s[i]]-=1
                i+=1
            j+=1
        return c
            
