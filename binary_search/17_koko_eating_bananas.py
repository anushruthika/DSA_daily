# 875. Koko Eating Bananas
## BRUTE force: 
# TC: O(n * max(piles))
# SC: O(1)

# OPTIMAL : Binary Search
## TC: O(n log(max(piles))) n is len(piles) sc:O(1)
class Solution:
    def tot_hr(self,piles,per_hr):
        tot_hr = 0
        for i in piles:
            tot_hr+= math.ceil(i/per_hr)
        return tot_hr
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high
        while low <= high:
            mid = low + (high - low) // 2
            tot_hr = self.tot_hr(piles, mid)

            if tot_hr <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
       
            
