class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        n=len(m)
        # if row=column, then only this method of transpose will work
        for i in range(0,n-1):
            for j in range(i+1,n):
                m[i][j],m[j][i]=m[j][i],m[i][j]
        for i in range(0,n):
            for j in range(0,n//2):
                m[i][j],m[i][n-j-1]=m[i][n-j-1],m[i][j]
        return m
