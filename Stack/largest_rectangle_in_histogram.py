# 84
class Solution:
    def nse(self,nums):
        stack=[]
        n=len(nums)
        res=[n]*n
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                res[stack.pop()]=i
            stack.append(i)
        return res 
    def pse(self, nums):
        stack=[]
        n=len(nums)
        res=[-1]*n
        for i in range(n-1,-1,-1):
            while stack and nums[stack[-1]] > nums[i]:
                res[stack.pop()]=i
            stack.append(i)
        return res 

    def largestRectangleArea(self, heights: List[int]) -> int:
        pse = self.pse(heights)
        nse = self.nse(heights)
        max_count=0
        for i in range(len(heights)):
            # count = heights[i]*(i-pse[i]) + heights[i]*(nse[i]-i)
            count = heights[i]*(nse[i]-pse[i]-1)
            if count > max_count:
                max_count = count
        return max_count
