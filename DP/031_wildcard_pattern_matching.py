# 44. Wildcard Matching

# class Solution(object):
#     def isMatch(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: bool
#         """
#         n = len(s)
#         m = len(p)
#         DP = [[-1]*m for _ in range(n)]
#         def rec(i,j):
#             if i<0 and j<0:
#                 return True
#             if j<0 and i>=0:
#                 return False
#             if j>=0 and i<0:
#                 for x in range(j+1):
#                     if p[x]!='*':
#                         return False
#                 return True
#             if DP[i][j]!=-1:
#                 return DP[i][j]
#             if s[i] == p[j] or p[j]=='?':
#                 DP[i][j] = rec(i-1,j-1)
#                 return DP[i][j]
#             if p[j] == '*':
#                 DP[i][j] = rec(i,j-1) or rec(i-1,j) or rec(i-1,j-1)
#                 return DP[i][j]
#             DP[i][j] = False
#             return DP[i][j]
#         return rec(n-1,m-1) 

# class Solution(object):
#     def isMatch(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: bool
#         """
#         n = len(s)
#         m = len(p)
#         DP = [[False]*(m+1) for _ in range(n+1)]
#         DP[0][0] = True
#         for r in range(1,n+1):
#             DP[r][0] = False
#         flag = True
#         for c in range(1,m+1):
#             if flag and p[c-1] == '*':
#                 DP[0][c] = True
#             else:
#                 flag = False
#                 DP[0][c] = False
#         for r in range(1,n+1):
#             for c in range(1,m+1):
#                 if s[r-1] == p[c-1] or p[c-1] == '?':
#                     DP[r][c] = DP[r-1][c-1]
#                 elif p[c-1] == '*':
#                     DP[r][c] = DP[r-1][c] or DP[r][c-1] or DP[r-1][c-1]
#                 else:
#                     DP[r][c] = False
#         return DP[n][m]

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n = len(s)
        m = len(p)
        DP = [False]*(m+1)
        DP[0] = True
        flag = True
        for c in range(1,m+1):
            if flag and p[c-1] == '*':
                DP[c] = True
            else:
                flag = False
                DP[c] = False
        for r in range(1,n+1):
            newDP = [False]*(m+1)
            for c in range(1,m+1):
                if s[r-1] == p[c-1] or p[c-1] == '?':
                    newDP[c] = DP[c-1]
                elif p[c-1] == '*':
                    newDP[c] = DP[c] or newDP[c-1] or DP[c-1]
                else:
                    newDP[c] = False
            DP = newDP
        return DP[m]
        
