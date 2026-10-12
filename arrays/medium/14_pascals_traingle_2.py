# 119. Pascal's Triangle II

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        res = [1]
        if rowIndex == 0:
            return res
        for i in range(1,rowIndex+1):
            l = [1]
            for j in range(1,i):
                l.append(res[j-1]+res[j])
            l.append(res[i-1])
            res = l
        return res
