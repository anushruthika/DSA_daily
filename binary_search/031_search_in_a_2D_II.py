# 240. Search a 2D Matrix II

# TC:O(n+m) 
# reason: at max we traverse m steps down and n steps towards left
# SC: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        row = 0
        col = m-1
        while row<n and col>=0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col]<target:
                row+=1
            else:
                col-=1
        return False
