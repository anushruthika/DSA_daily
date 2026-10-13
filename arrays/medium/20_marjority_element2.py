# 229. Majority Element II
# 
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        # only two elements can at max occur more than n//3 times
        
        n = len(nums)
        count1 = 0
        count2 = 0
        cand1 = None
        cand2 = None
        res = []
        for num in nums:
            if num == cand1:
                count1+=1
            elif num == cand2:
                count2+=1
            elif count1 == 0:
                cand1=num
                count1 = 1
            elif count2 == 0:
                cand2 = num
                count2 = 1
            else:
                count1-=1
                count2-=1
        if cand1!=None and nums.count(cand1)>n//3:
            res.append(cand1)
        if cand1!=cand2 and cand2!=None and nums.count(cand2)>n//3:
            res.append(cand2)
        return res
