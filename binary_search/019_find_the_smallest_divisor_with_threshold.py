# 1283. Find the Smallest Divisor Given a Threshold

# Brute Force: O(n × max(nums))
# Optimal: O(n × log(max(nums)))
# Space: O(1)

# threshold>=len(nums) else not possible 
class Solution:
    def tot(self,nums,div):
        tot = 0
        for i in nums:
            tot+= math.ceil(i/div)
        return tot

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        ans = -1
        while low<=high:
            mid = low+ (high-low)//2
            tot = self.tot(nums,mid)
            if tot <= threshold:
                high = mid-1
                ans = mid
            else:
                low = mid+1
        return ans
            
