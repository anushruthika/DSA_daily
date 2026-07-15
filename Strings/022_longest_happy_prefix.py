# The largest prefix which is also suffix is given by "l".

# s = "level"
# lps: [0,0,0,0,1]
# ans: 1
# s = "ababab"
# lps: [0,0,1,2,3,4]
# ans: 4

class Solution:
    def buildLPS(self, pattern):
        n = len(pattern)
        lps = [0] * n

        length = 0
        i = 1

        while i < n:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps
    def longestPrefix(self, s: str) -> str:
        return s[:self.buildLPS(s)[-1]]

