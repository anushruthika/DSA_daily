class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack=[]
        res=[]
        for i in range(len(nums)):
            # append the element i, but if nums[i]> than the stack elements delete those elements
            # which tells the stack[0] has the maximum element in the window
            while stack and nums[stack[-1]]<=nums[i]:
                stack.pop(-1)
            stack.append(i)
            if stack[0]<=i-k:
                stack.pop(0)
            if i>=k-1:
                res.append(nums[stack[0]])
        return res
