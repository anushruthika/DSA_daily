# 1248. Count Number of Nice Subarrays
# Time Complexity: O(n)
# Reason:
# Sliding window traverses the array once O(n).. two times O(2n) = O(n)
# Space Complexity: O(1)

class Solution:
    def atmost(self,nums,k):
        if k<0:
            return 0
        tracker=0
        i=0
        j=0
        c =0
        while j<len(nums):
            if nums[j]%2!=0:
                tracker+=1
            while tracker >k:
                if nums[i]%2!=0:
                    tracker-=1
                i+=1
            c+=j-i+1
            j+=1
        return c
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atmost(nums,k) - self.atmost(nums,k-1)
