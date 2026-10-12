# 48. Rotate Image

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(m):
            for j in range(n//2):
                matrix[i][j],matrix[i][n-j-1]= matrix[i][n-j-1],matrix[i][j]
        
