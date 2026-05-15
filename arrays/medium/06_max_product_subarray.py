# 152. Maximum Product Subarray

# Time Complexity: O(n)
# Space Complexity: O(1)
# only one logic: -neg*-neg = +pos
# kadanes algo for sum: we dont track negative values as they become even more negative, but multiplication later can become more possitive
# track max and min on traversing new value, when we find a negative value reverse max and min stating max*neg = most_min , min*-neg = most_max..
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = cur_max = cur_min = nums[0]
        for i in range(1,len(nums)):
            val = nums[i]
            if val<0:
                cur_max,cur_min = cur_min,cur_max
            cur_max = max(val,val*cur_max)
            cur_min = min(val,val*cur_min)
            res = max(res,cur_max)
        return res
