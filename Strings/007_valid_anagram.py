# 242. Valid Anagram

# # Brute force
# # TC: O(nlogn) SC:O(n) extra auxilary space for sorting
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True if sorted(s) == sorted(t) else False

## optimal approach:
# TC: o(n)+O(n) = O(2n) = O(n) SC: O(n) dictionary
from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t)
        if n1 != n2:
            return False
        d = defaultdict(int)
        for i in s:
            d[i]+=1
        for i in t:
            if i not in d:
                return False
            elif d[i]==0:
                return False
            else:
                d[i]-=1
        return True
            
## Optimal Approach using Builtin
# TC: o(n)+O(n) = O(2n) = O(n) SC: O(n) dictionary
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# If s & t only have lower case or only specific set of tokens
# Time:O(n) Space: 26 integers O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        freq = [0] * 26

        for c in s:
            freq[ord(c) - ord('a')] += 1

        for c in t:
            freq[ord(c) - ord('a')] -= 1

        return all(x == 0 for x in freq)
