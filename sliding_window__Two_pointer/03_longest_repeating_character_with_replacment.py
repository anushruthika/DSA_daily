# 424. Longest Repeating Character Replacement

# Time Complexity: O(n)
# Space Complexity: O(1)

from collections import defaultdict

class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        i =0
        j=0
        # max_freq
        mf = 0
        # max width
        mw = 0
        while j<len(s):
            count[s[j]]+=1
            # width
            w = j-i+1
            mf = max(count[s[j]],mf)
            if w-mf>k:
                count[s[i]]-=1
                i+=1
                j+=1
                continue
            mw = max(w,mw)
            j+=1
        return mw
