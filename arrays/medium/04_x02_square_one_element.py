# https://www.geeksforgeeks.org/problems/maximum-sum-subarray--143510/1

class Solution:
    def maximumSubarray(self, arr: list[int]) -> int:
        """ code here """
        # 4   -2   0   3
        # 16  16  16
        # 4    2
        # 16  14  
        # 1. 4+4 , 16+-2? = 14
        # 2. 
        max_sum = arr[0]**2
        keep = arr[0]
        square = arr[0]**2
        n = len(arr)
        for i in range(1,n):
            square = max(keep+arr[i]**2,square+arr[i],arr[i]**2)
            keep = max(keep+arr[i],arr[i])
            max_sum = max(square,max_sum,keep)
        return max_sum
