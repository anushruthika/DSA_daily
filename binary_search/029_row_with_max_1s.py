# https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1

# Time Complexity: O(n × log m)
# Reason:
# - There are n rows.
# - For each row, a binary search (lower bound) is performed on m columns.

# Space Complexity: O(1)
# Reason:
# - Only a few variables (low, high, mid, maxi, max_ind) are used.
# - No extra data structures are created.
class Solution:
    def lowerBound(self,row):
        low = 0
        high = len(row)-1
        while low<=high:
            mid = (low+high)//2
            if row[mid]<1:
                low = mid+1
            else:
                high = mid-1
        return low
    def rowWithMax1s(self, arr):
        maxi=0
        max_ind = -1
        row_len = len(arr[0])
        for i in range(len(arr)):
            lb = self.lowerBound(arr[i])
            if maxi<row_len-lb:
                maxi = row_len-lb
                max_ind = i
        return max_ind
