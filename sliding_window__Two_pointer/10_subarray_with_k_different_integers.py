# 992. Subarrays with K Different Integers
# Time Complexity: O(n)
# Sliding window traverses the array once.

# Space Complexity: O(k)
# Hashmap stores at most k distinct elements in the window.
from collections import defaultdict
class Solution:
    def atmost(self,nums,k):
        if k<0:
            return 0
        d=defaultdict(int)
        i=0
        j=0
        count = 0
        while j<len(nums):
            d[nums[j]]+=1
            while len(d)>k:
                d[nums[i]]-=1
                if d[nums[i]] == 0:
                    del d[nums[i]]
                i+=1
            count+= j-i+1
            j+=1
        return count
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atmost(nums,k) - self.atmost(nums,k-1)
