# 283. Move Zeroes

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        i = 0
        n = len(nums)
        while i<n:
            if nums[i] == 0:
                i+=1
                continue
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j+=1
