class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s1 = s
        s2 = s[::-1]
        return lcs(s1,s2)


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s1 = s
        s2 = s[::-1]
        l = len(s)
        DP = [0]*(l+1)

        for i in range(1,l+1):
            newDP = [0]*(l+1)
            for j in range(1,l+1):
                if s1[i-1] == s2[j-1]:
                    newDP[j] = 1+DP[j-1]
                else:
                    newDP[j] = max(DP[j],newDP[j-1])
            DP = newDP
        return DP[l]
        
        
        
        
