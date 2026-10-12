# 54. Spiral Matrix
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m = len(matrix)
        n = len(matrix[0])
        top = 0
        left = 0
        right = n-1
        down = m-1
        res = []
        while left <=right and top<=down:
            # top row add
            i = left
            while i<=right:
                res.append(matrix[top][i])
                i+=1
            top+=1
            
            i = top
            while i<=down:
                res.append(matrix[i][right])
                i+=1
            right -=1
            
            if top<=down:
                i = right
                while i>=left:
                    res.append(matrix[down][i])
                    i-=1
                down-=1
            if left<=right:
                i = down
                while i>=top:
                    res.append(matrix[i][left])
                    i-=1
                left+=1
        return res

