# 1011. Capacity To Ship Packages Within D Days

# Brute Force: O(n × (sum(weights) - max(weights)))
# Optimal: O(n × log(sum(weights) - max(weights)))
# Space: O(1)

class Solution:
    def tot_days(self,weights,cap):
        tot_days = 1
        cur_cap = 0
        for i in weights:
            if cur_cap+i>cap:
                tot_days+=1
                cur_cap =i
            else:
                cur_cap+=i
        return tot_days
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        ans = -1
        while low<=high:
            mid = low+(high-low)//2
            tot_days = self.tot_days(weights,mid)
            if tot_days<=days:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans
