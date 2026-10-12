# 73. Set Matrix Zeroes

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        r = set()
        c = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    r.add(i)
                    c.add(j)
        for i in r:
            for j in range(n):
                matrix[i][j] = 0
        for j in c:
            for i in range(m):
                matrix[i][j] = 0
                
        
