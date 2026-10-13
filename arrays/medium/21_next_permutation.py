# 31. Next Permutation

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind = -1
        n = len(nums)
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                ind = i
                break
        if ind == -1:
            nums[:] = nums[::-1]
            return
        for i in range(n-1,ind,-1):
            if nums[ind]<nums[i]:
                nums[i],nums[ind] = nums[ind],nums[i]
                break
        nums[ind+1:] = nums[n:ind:-1]
        
