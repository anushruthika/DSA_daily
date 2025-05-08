class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n,m=len(matrix),len(matrix[0])
        set_i, set_j =set(),set()
        for i in range(0,n):
            for j in range(0,m):
                if(matrix[i][j]==0):
                    set_i.add(i)
                    set_j.add(j)
        print(set_i,set_j)
        for i in set_i:
            matrix[i][:] =[0]*m
        for i in set_j:
            for j in range(0,n):
                matrix[j][i]=0
        return matrix
