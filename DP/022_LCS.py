class Solution:
    # 2^n x 2^m
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     def rec(ind1,ind2):
    #         if ind1<0 or ind2<0:
    #             return 0
    #         if text1[ind1] == text2[ind2]:
    #             return 1+rec(ind1-1,ind2-1)
    #         return max(rec(ind1-1,ind2),rec(ind1,ind2-1))
    #     return rec(len(text1)-1,len(text2)-1)
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     n,m = len(text1),len(text2)
    #     DP = [[-1]*m for _ in range(n)]
    #     def rec(ind1,ind2):
    #         if ind1<0 or ind2<0:
    #             return 0
    #         if DP[ind1][ind2]!=-1:
    #             return DP[ind1][ind2]
    #         if text1[ind1] == text2[ind2]:
    #             DP[ind1][ind2] = 1+rec(ind1-1,ind2-1)
    #             return DP[ind1][ind2]
    #         DP[ind1][ind2] = max(rec(ind1-1,ind2),rec(ind1,ind2-1))
    #         return DP[ind1][ind2]
    #     return rec(n-1,m-1)
    # Tabulation
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     n,m = len(text1),len(text2)
    #     DP = [[0]*(m+1) for _ in range(n+1)]
    #     for r in range(n+1):
    #         DP[r][0] = 0
    #     for c in range(m+1):
    #         DP[0][c] = 0
    #     for r in range(1,n+1):
    #         for c in range(1,m+1):
    #             if text1[r-1] == text2[c-1]:
    #                 DP[r][c] = 1+DP[r-1][c-1]
    #             else:
    #                 DP[r][c] = max(DP[r-1][c],DP[r][c-1])
    #     return DP[n][m]
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     n,m = len(text1),len(text2)
    #     DP = [0]*(m+1)
    #     for r in range(1,n+1):
    #         new_DP = [0]*(m+1)
    #         for c in range(1,m+1):
    #             if text1[r-1] == text2[c-1]:
    #                 new_DP[c] = 1+DP[c-1]
    #             else:
    #                 new_DP[c] = max(DP[c],new_DP[c-1])
    #         DP = new_DP
    #     return DP[m]

