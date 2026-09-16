# 115. Distinct Subsequences

# aab ->ab

# tabulation 
#   a  b  
# a 1  0  
# a 1  1
# b 0  2
# count of number of distinct subsequences

# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:
#         def rec(i,j):
#             if j<0:
#                 return 1
#             if i<0:
#                 return 0
#             if s[i] == t[j]:
#                 return rec(i-1,j)+rec(i-1,j-1)
#             return rec(i-1,j)
#         return rec(len(s)-1,len(t)-1)
# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:
#         m = len(t)
#         n = len(s)
#         DP = [[-1]*m for _ in range(n) ]
#         def rec(i,j):
#             if j<0:
#                 return 1
#             if i<0:
#                 return 0
#             if DP[i][j]!=-1:
#                 return DP[i][j]
#             if s[i] == t[j]:
#                 DP[i][j] = rec(i-1,j)+rec(i-1,j-1)
#                 return DP[i][j]
#             DP[i][j] = rec(i-1,j)
#             return DP[i][j]
#         return rec(n-1,m-1)

# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:
#         m = len(t)
#         n = len(s)
#         DP = [[0]*(m+1) for _ in range(n+1) ]
#         for r in range(n + 1):
#             DP[r][0] = 1
#         for r in range(1,n+1):
#             for c in range(1,m+1):
#                 if s[r-1] == t[c-1]:
#                     DP[r][c] = DP[r-1][c]+DP[r-1][c-1]
#                 else:
#                     DP[r][c] = DP[r-1][c]  
#         return DP[n][m]
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(t)
        n = len(s)
        DP = [0]*(m+1)
        DP[0] = 1
        for r in range(1,n+1):
            newDP = [0]*(m+1)
            newDP[0] = 1
            for c in range(1,m+1):
                if s[r-1] == t[c-1]:
                    newDP[c] = DP[c]+DP[c-1]
                else:
                    newDP[c] = DP[c] 
            DP = newDP 
        return DP[m]
        
