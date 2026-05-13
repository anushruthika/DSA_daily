# 229. Majority Element II
# Boyer-Moore Voting Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count2 = count1 = 0
        cand1=cand2= None
        # choosing the candidate
        for num in nums:
            if num == cand1:
                count1+=1
            elif num ==cand2:
                count2+=1
            elif count1 == 0:
                cand1 = num
                count1 = 1
            elif count2 == 0:
                cand2 = num
                count2 = 1
            # someone who is not a candidate
            else:
                count1-=1
                count2-=1
        res = []
        if nums.count(cand1) > len(nums)//3:
            res.append(cand1)
        if cand1!=cand2 and nums.count(cand2) > len(nums)//3:
            res.append(cand2)
        return res

# TC: o(n) SC: o(n)
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = set()
        length = math.ceil(len(nums)//3)
        # default value is 0 if you need to modify
        # d=defaultdict(int,lambda:1)
        d=defaultdict(int)
        for i,v in enumerate(nums):
            d[v]+=1
            if v not in res and d[v]>length :
                res.add(v)
        return list(res)
