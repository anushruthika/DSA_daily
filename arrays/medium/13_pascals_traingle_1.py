# 118. Pascal's Triangle

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1],[1,1]]
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return res
        for i in range(2,numRows):
            l = [1]
            for j in range(1,i):
                l.append(res[i-1][j-1]+res[i-1][j])
            l.append(res[i-1][i-1])
            res.append(l)
        return res

                
