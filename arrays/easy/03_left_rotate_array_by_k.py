# 189. Rotate Array

# Time: O(n) => slicing o(n)and list contenationo(n)
# space: O(n) => Those slices create new temporary lists, so extra memory is used.

def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    nums[:] = nums[-(k:=k%len(nums)):]+nums[:-k]



# Tc: O(n) => slicing is O(n)
# SC : O(1) => no temporary lists created
class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n

        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
