class Solution(object):

    def sumSubarrayMax(self, arr):
        stack=[]
        max_=0
        n=len(arr)
        for i in range(n+1):
            while stack and (i==n or arr[stack[-1]]<=arr[i]):
                j = stack.pop()
                left_boundary = stack[-1] if stack else -1
                max_+=arr[j]*(j-left_boundary)*(i-j)
            stack.append(i)
        return max_
        
    def sumSubarrayMin(self, arr):
        stack=[]
        min_=0
        n=len(arr)
        for i in range(n+1):
            while stack and (i==n or arr[stack[-1]]>=arr[i]):
                j = stack.pop()
                left_boundary = stack[-1] if stack else -1
                min_+=arr[j]*(j-left_boundary)*(i-j)
            stack.append(i)
        return min_
    def subArrayRanges(self, nums):
        return (self.sumSubarrayMax(nums) - self.sumSubarrayMin(nums))
