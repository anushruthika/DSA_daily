class Solution:
    # length of shortest common supersequence
    # def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
    #     l1,l2 = len(s1),len(s2)
    #     DP = [0]*(l2+1)
    #     for i in range(1,l1+1):
    #         newDP = [0]*(l2+1)
    #         for j in range(1,l2+1):
    #             if s1[i-1] == s2[j-1]:
    #                 newDP[j] = 1+DP[j-1]
    #             else:
    #                 newDP[j] = max(newDP[j-1],DP[j])
    #         DP = newDP
    #     return l1+l2-DP[l2]
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        l1,l2 = len(s1),len(s2)
        DP = [[0]*(l2+1) for _ in range(l1+1)]
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if s1[i-1] == s2[j-1]:
                    DP[i][j] = 1+DP[i-1][j-1]
                else:
                    DP[i][j] = max(DP[i][j-1],DP[i-1][j])
        length = l1+l2 - DP[l1][l2]
        i = l1
        j = l2
        ans = ""
        while i>0 and j>0:
            if s1[i-1] == s2[j-1]:
                ans+=s1[i-1]
                i-=1
                j-=1
            else:
                if DP[i-1][j]>=DP[i][j-1]:
                    ans+=s1[i-1]
                    i-=1
                else:
                    ans+=s2[j-1]
                    j-=1
        while i > 0:
            ans += s1[i-1]
            i -= 1

        while j > 0:
            ans += s2[j-1]
            j -= 1
        return ans[::-1]


