#  voting algorithm:
# time : o(n),
# space: o(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for i in nums:
            if count ==0:
                candidate = i
            if candidate == i:
                count+=1
            else:
                count -=1
        return candidate


# time : o(nlogn)- sorting,
# space: o(1)
# approach: sorted [1,1,1,2,2,2,2] nums[3] = 2 middle is the answer
# ceil: It returns the smallest integer greater than or equal to the given number. math.ceil(2.4) = 3
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[math.ceil(len(nums)//2)]


# time : o(n),
# space: o(n) to store dict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        max_vote = float('-inf')
        candidate = None
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
            if d[i]>max_vote:
                max_vote = d[i]
                candidate = i
        return candidate

