# 4. Median of Two Sorted Arrays

## BRUTE FORCE
# Merge sort and median 
# TC: o((n1+n2)log(n1+n2)) SC:O(1)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        x=len(nums1)

        if(x%2!=0):
            return nums1[x//2 ]
        else:
            return round((nums1[(x//2)-1]+nums1[(x//2)])/2,5)


####### OPTIMAL
# Binary search on the smaller array to find a partition such that all elements on the left are less than or equal to all elements on the right; 
# then the median is determined from the partition boundaries.

# Time Complexity: O(log(min(n1, n2)))
# Reason:
# - Binary search is performed only on the smaller array.
# - Each iteration halves the search space.

# Space Complexity: O(1)
# Reason:
# - Only a few variables (low, high, mid, l1, r1, l2, r2) are used.
# - No extra data structures are created.


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        # consider that n1<n2
        if n1>n2:
            nums1,nums2 = nums2,nums1
            n1,n2 = n2,n1
        low = 0
        high = n1
        tot = n1+n2
        # For odd total length, the left partition should contain one extra element.
        median = (tot+1)//2
        while low<=high:
            mid = low+(high-low)//2
            ind = median-mid
            l1 = float('-inf') if mid == 0 else nums1[mid-1]
            r1 = float('inf')  if mid == n1 else nums1[mid]

            l2 = float('-inf') if ind == 0 else nums2[ind-1]
            r2 = float('inf')  if ind == n2 else nums2[ind]
            if l1<=r2 and l2<=r1:
                if tot%2 == 0:
                    return (max(l1,l2)+min(r1,r2))/2
                else:
                    return max(l1, l2)
            if l1>r2:
                high = mid-1
            elif l2>r1:
                low = mid+1
