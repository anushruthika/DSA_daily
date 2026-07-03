# 74. Search a 2D Matrix

### BRUTE 
# TC:O(n*m) SC:O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            for j in i:
                if j == target:
                    return 1
                elif j > target:
                    return 0 
# TC:O(nlogm) sc:O(1)
class Solution:
    def bs(self,arr,k):
        low = 0
        high = len(arr)-1
        while low<=high:
            mid = low+(high-low)//2
            if arr[mid] == k:
                return True
            elif arr[mid]<k:
                low = mid+1
            else:
                high = mid-1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0]<=target and row[-1]>=target:
                return self.bs(row,target)
        return False

##### OPTIMAL APPROACH
# TC: O(log(n*m)) SC: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        low = 0
        high = n*m-1
        while low<=high:
            mid = low+(high-low)//2
            row = mid//m 
            col = mid%m
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                low = mid+1
            else:
                high = mid-1
        return False
        
