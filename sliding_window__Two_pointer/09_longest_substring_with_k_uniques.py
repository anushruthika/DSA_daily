# Time Complexity: O(n)
# Space Complexity: O(k)

import collections
class Solution:
    def longestKSubstr(self, s, k):
        d=collections.defaultdict(int)
        i=0
        j=0
        n = len(s)
        long_count = -1
        while j<n:
            d[s[j]]+=1
            while len(d)>k:
                d[s[i]]-=1
                if d[s[i]] == 0:
                    del d[s[i]]
                i+=1
            if len(d) == k:
                long_count = max(long_count,j-i+1)
            j+=1
        return long_count
