# 696. Count Binary Substrings

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        s = s.replace('10','1 0')
        s= s.replace('01','0 1')
        l = s.split()
        i = 0
        j = 1
        count = 0
        while j<len(l):
            count+=min(len(l[i]),len(l[j]))
            i+=1
            j+=1
        return count
