# intution: max insertions- len(string) 

# min insertions = len(string)-lps

class Solution:
    def minInsertions(self, s: str) -> int:
        s2 = s[::-1]
        l = len(s)
        DP = [0]*(l+1)
        for i in range(1,l+1):
            newDP = [0]*(l+1)
            for j in range(1,l+1):
                if s[i-1] == s2[j-1]:
                    newDP[j] = 1+DP[j-1]
                else:
                    newDP[j] = max(newDP[j-1],DP[j])
            DP = newDP
        return l-DP[l]
