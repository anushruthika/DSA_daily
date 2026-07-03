# https://www.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1

# Time Complexity: O(log(min(n1, n2)))
# Reason:
# - Binary search is performed only on the smaller array.
# - Each iteration halves the search space and all partition checks are O(1).

# Space Complexity: O(1)
# Reason:
# - Only a constant number of variables (low, high, mid, ind, l1, r1, l2, r2) are used.
# - No extra data structures are created.
class Solution:
    def kthElement(self, nums1, nums2, k):
        # code here
        n1 = len(nums1)
        n2 = len(nums2)
        # consider that n1<n2
        if n1>n2:
            nums1,nums2 = nums2,nums1
            n1,n2 = n2,n1
        # low = max(k - n2, 0) and high = min(k, n1) ensure that both partitions 
        # (mid in nums1 and k - mid in nums2) always remain within valid array bounds.
        low = max(k-n2,0)
        high = min(k,n1)

        tot = n1+n2
        while low<=high:
            mid = low+(high-low)//2
            ind = k-mid
            l1 = float('-inf') if mid == 0 else nums1[mid-1]
            r1 = float('inf')  if mid == n1 else nums1[mid]

            l2 = float('-inf') if ind == 0 else nums2[ind-1]
            r2 = float('inf')  if ind == n2 else nums2[ind]
            if l1<=r2 and l2<=r1:
                    return max(l1, l2)
            if l1>r2:
                high = mid-1
            elif l2>r1:
                low = mid+1
