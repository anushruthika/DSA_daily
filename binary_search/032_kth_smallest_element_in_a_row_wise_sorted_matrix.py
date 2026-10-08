# 378. Kth Smallest Element in a Sorted Matrix

# Please watch: https://m.youtube.com/watch?v=F22d27HJsxg&pp=ygUoa3RoIHNtYWxsZXN0IGVsZW1lbnQgaW4gYW4gc29ydGVkIG1hdHJpeNIHCQk1DAGHKiGM7w%3D%3D

class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        # low = min(matrix)
        # high = max(matrix)
        n = len(matrix)
        # given n*n matrix thus lr = lc = n
        low = matrix[0][0]
        high = matrix[n-1][n-1]
        while low <high:
            mid = low+ (high-low)//2
            row = n-1
            col = 0
            rank = 0
            while row>=0 and col<n:
                if matrix[row][col]<=mid:
                    # It means elements to the left and top are lower than it. but the left elements top is being summed up one by one thus currently top of this is only the minimum and add to rank.
                    rank+=row+1
                    # elements next to this in this row can be lower or equal thus move right
                    col+=1
                else:
                    row-=1
            if rank <k:
                low = mid+1
            else:
                high = mid
        return low
