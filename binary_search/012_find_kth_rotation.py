# https://www.geeksforgeeks.org/problems/rotation4723/1
# TC: O(log n)
# SC: O(1)
# same as 11_minimum_in_a_sorted_array.py but keep track of index
class Solution:
    def findKRotation(self, nums):
        # code here
        low = 0
        high = len(nums)-1
        ans = float('inf')
        ind = -1
        while low<=high:
            if nums[low] <= nums[high]:
                if nums[low]<ans:
                    ans = nums[low]
                    ind = low
                break
            mid = low+(high-low)//2
            if nums[low]>nums[mid]:
                if nums[mid]<ans:
                    ans = nums[mid]
                    ind = mid
                high = mid-1
            else:
                if nums[low]<ans:
                    ans = nums[low]
                    ind = low
                low = mid+1
        return ind
