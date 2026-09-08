class Solution:
    def longCommSubstr(self, s1, s2):
        n,m = len(s1),len(s2)
        DP =[[0]*(m+1) for _ in range(n+1)]
        ans = 0
        for r in range(1,n+1):
            for c in range(1,m+1):
                if s1[r-1] == s2[c-1]:
                    DP[r][c]= 1+DP[r-1][c-1]
                    ans = max(ans,DP[r][c])
                else:
                    DP[r][c] = 0
        return ans
        
        
