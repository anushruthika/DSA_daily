# 162. Find Peak Element

##### BRUTE FORCE
# TC:O(n) SC:O(1)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return 0
        for i in range(n):
            if i+1<=n-1 and nums[i]>nums[i+1]:
                return i
        if nums[n-1]>nums[n-2]:
            return n-1

####### OPTIMAL :BINARY SEARCH
# TC: O(logn) SC:O(1)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return 0
        if nums[n-1]>nums[n-2]:
            return n-1
        if nums[0]>nums[1]:
            return 0
        low = 1
        high = len(nums)-2
        while low<=high:
            mid = low+(high-low)//2
            if nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
                return mid
            # increasing curve
            if nums[mid-1]<nums[mid]:
                low = mid+1
            # decreasing curve
            elif nums[mid]>nums[mid+1]:
                high = mid-1
            # saddle point (the ambiguous case): where both mid-1>mid and mid+1>mid
            # neither decreasing nor increasing 
            # meaning the peak can be in both left and right
            else:
                # anything works
                low=mid+1
                # high = mid-1
        return -1

