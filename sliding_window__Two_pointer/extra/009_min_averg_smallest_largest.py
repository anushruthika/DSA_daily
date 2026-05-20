# 3194. Minimum Average of Smallest and Largest Elements

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        n = len(nums)
        i =0
        j= n-1
        nums.sort()
        m = float('inf')
        while i<j:
            # print(nums,(nums[i]+nums[j])/2,(nums[i]+nums[j]),nums[i],nums[j])
            m = min((nums[i]+nums[j])/2,m)
            i+=1
            j-=1   
        return m
