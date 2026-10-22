# 31. Next Permutation
# 7402687
# 1. find pivot: (6) =>  find nums[i]<nums[i+1] from end -> ind = i. first minimum from end
# 2. if ind =None return reversed arr(corner case: 321)
# 3. find suc: (7) => find first element greater than nums[ind] from end within [8,7]
# 4. Swap nums[ind] nums[suc] => 7402786
# 5. reverse 86 - 68 => nums[ind+1:n] = nums[n-1,ind,-1] 
# ans: 7402768
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
        
