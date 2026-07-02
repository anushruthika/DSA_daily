# https://leetcode.com/problems/kth-missing-positive-number/

# # Brute Force
# TC: O(n)
# SC: O(1)

# # Binary Search (Optimal)
# TC: O(log n)
# SC: O(1)

# Brute Force
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for i in arr:
            if i<k:
                k+=1
            else:
                break
        return k

# upper bound on missing counter array then use arr[high] to compute answer based on formula
# PLEASE WATCH: https://www.youtube.com/watch?v=uZ0N_hZpyps
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low = 0
        high = len(arr)-1
        while low<=high:
            mid = low+(high-low)//2
            missing = arr[mid] - (mid+1)
            if missing<k:
                low = mid+1
            else:
                high = mid-1
        return high+k+1

# At the end of binary search:

# high = last index where missing < k

# Missing numbers before arr[high]:

# missing = arr[high] - (high + 1)

# We still need:

# k - missing

# numbers after arr[high].

# Answer

# = arr[high] + (k - missing)

# = arr[high] + k - (arr[high] - (high + 1))

# = arr[high] + k - arr[high] + high + 1

# = k + high + 1
