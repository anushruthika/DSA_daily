# (considering changing s1 as s2) min deletion , min insertion 
# max operations: l1+l2
# min operations: min deletion: l1-lps min insertions: l2-lps 
# min operations : l1-lps +l2 - lps = l1+l2 - 2*lps
class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        l1,l2 = len(s1),len(s2)
        DP = [0]*(l2+1)
        for i in range(1,l1+1):
            newDP = [0]*(l2+1)
            for j in range(1,l2+1):
                if s1[i-1] == s2[j-1]:
                    newDP[j] = 1+DP[j-1]
                else:
                    newDP[j] = max(newDP[j-1],DP[j])
            DP = newDP
        return l1+l2-2*DP[l2]

