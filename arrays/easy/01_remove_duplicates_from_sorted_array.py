# 26. Remove Duplicates from Sorted Array

# Brute Force
# o(n**2) : while loop can run for n times if no duplicates. pop(i) takes time o(n)
# space:O(1) no extra space
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        while(i<(len(nums)-1)):
            # print(i,nums[i],nums[i+1])
            if nums[i] == nums[i+1]:
                nums.pop(i)
            else:
                i+=1
# Two pointer:
# tc: O(n)
# space: o(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        k = 1
        while(i<len(nums)):
            if nums[i]!=nums[i-1]:
                nums[k]=nums[i]
                k+=1
            i+=1
        return k
