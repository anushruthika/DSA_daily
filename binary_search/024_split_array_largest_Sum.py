# 410. Split Array Largest Sum
# SAME as BOOK ALLOCATION


# Total TC
# = O(log(sum(arr) - max(arr))) × O(n)
# = O(n × log(sum(arr) - max(arr)))
class Solution:
    def possible(self,nums,k,val):
        cur_k =1
        cur_val = 0
        for i in range(0,len(nums)):
            if cur_val+nums[i]<=val:
                cur_val += nums[i]
            else:
                cur_k+=1
                cur_val = nums[i]
        return cur_k<=k
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        while low<=high:
            mid = low+(high-low)//2
            if self.possible(nums,k,mid):
                high = mid-1
            else:
                low = mid+1
        return low
