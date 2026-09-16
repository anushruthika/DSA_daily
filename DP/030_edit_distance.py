# 72. Edit Distance

class Solution(object):
    # def minDistance(self, word1, word2):
    #     """
    #     :type word1: str
    #     :type word2: str
    #     :rtype: int
    #     """
    #     n = len(word1)
    #     m = len(word2)
    #     def rec(i,j):
    #         if j<0:
    #             return i+1
    #         if i<0:
    #             return j+1
    #         if word1[i] == word2[j]:
    #             return rec(i-1,j-1)
    #         return min(1+rec(i-1,j-1),1+rec(i,j-1),1+rec(i-1,j))
    #     return rec(n-1,m-1)
    # def minDistance(self, word1, word2):
    #     """
    #     :type word1: str
    #     :type word2: str
    #     :rtype: int
    #     """
    #     n = len(word1)
    #     m = len(word2)
    #     DP = [[-1]*m for _ in range(n)]
    #     def rec(i,j):
    #         if j<0:
    #             return i+1
    #         if i<0:
    #             return j+1
    #         if DP[i][j]!=-1:
    #             return DP[i][j]
    #         if word1[i] == word2[j]:
    #             DP[i][j] = rec(i-1,j-1)
    #             return DP[i][j]
    #         DP[i][j]=min(1+rec(i-1,j-1),1+rec(i,j-1),1+rec(i-1,j))
    #         return DP[i][j]
    #     return rec(n-1,m-1)
    # def minDistance(self, word1, word2):
    #     """
    #     :type word1: str
    #     :type word2: str
    #     :rtype: int
    #     """
    #     n = len(word1)
    #     m = len(word2)
    #     DP = [[-1]*(m+1) for _ in range(n+1)]
    #     DP[0][0] = 0
    #     for r in range(1,n+1):
    #         DP[r][0] = r
    #     for c in range(1,m+1):
    #         DP[0][c] = c
    #     for r in range(1,n+1):
    #         for c in range(1,m+1):
    #             if word1[r-1]==word2[c-1]:
    #                 DP[r][c] = DP[r-1][c-1]
    #             else:
    #                 DP[r][c]=1+min(DP[r-1][c-1],DP[r][c-1],DP[r-1][c])
    #     return DP[n][m]
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)
        DP = [0]*(m+1)
        DP[0] = 0
        for c in range(1,m+1):
            DP[c] = c
        for r in range(1,n+1):
            newDP = [0]*(m+1)
            newDP[0] = r
            for c in range(1,m+1):
                if word1[r-1]==word2[c-1]:
                    newDP[c] = DP[c-1]
                else:
                    newDP[c]=1+min(DP[c-1],newDP[c-1],DP[c])
            DP = newDP
        return DP[m]
