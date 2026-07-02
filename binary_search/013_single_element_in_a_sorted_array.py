# 540. Single Element in a Sorted Array

# Brute force: check your right and left if element not present return element
# TC: O(n) SC:O(1)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if not((i-1>=0 and nums[i] == nums[i-1]) or (i+1<n and nums[i+1]==nums[i])):
                return nums[i]


############## OPTIMAL BINARY SEARCH APPROACH
# # edge cases: 
# 1. only one element in array
# 2. single element in begining or end. (if not , do binary search only in the 1-> n-2 th element )
## note : always add edge cases: mid+1<n and mid-1>=0
# TC:O(logn) SC:O(n)

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n-1] != nums[n-2]:
            return nums[n-1]
        low = 1
        high = n-2
        while low<=high:
            
            mid = low+(high-low)//2
            if mid+1<n and nums[mid]!= nums[mid+1] and mid-1>=0 and nums[mid]!=nums[mid-1]:
                return nums[mid]
            if (mid%2==0 and mid+1<n and nums[mid+1] == nums[mid]) or (mid%2!=0 and mid-1>=0  and nums[mid-1]==nums[mid]):
                low = mid+1
            else:
                high = mid-1
        return -1  
