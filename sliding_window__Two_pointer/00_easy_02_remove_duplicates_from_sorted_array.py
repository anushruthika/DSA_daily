# 26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 1
        j = 1
        n = len(nums)
        while i<n:
            while i<n and nums[i] == nums[i-1]:
                i+=1
            if i<n:
                nums[j] = nums[i]
            else:
                break
            j+=1
            i+=1
        return j
