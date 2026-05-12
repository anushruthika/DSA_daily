# 485. Max Consecutive Ones
# o(n) time complexity o(1) space
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        cur_count = 0
        for i in nums:
            if i == 1:
                cur_count+=1
            else: 
                cur_count = 0
            if cur_count > count:
                count = cur_count
            
        return count 
