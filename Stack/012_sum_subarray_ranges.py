# 2104. Sum of Subarray Ranges

# TC: O(n)
# SC: O(n)
class Solution:
    def nse(self, arr):
        stack =[]
        n = len(arr)
        res = [n]*n
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if stack and arr[stack[-1]]<arr[i]:
                res[i] = stack[-1]
            stack.append(i)
        return res
    def pse(self, arr):
        stack =[]
        n = len(arr)
        res = [-1]*n
        for i in range(n):
            while stack and arr[stack[-1]]>arr[i]:
                stack.pop()
            if stack and arr[stack[-1]]<=arr[i]:
                res[i] = stack[-1]
            stack.append(i)
        return res
    def sumSubarrayMins(self, arr: List[int]) -> int:
        nse = self.nse(arr)
        pse = self.pse(arr)
        tot = 0
        for i in range(len(arr)):
            # number of subarrays on left
            left = i - pse[i]
            # number of subarrays on right
            right = nse[i] - i
            tot += left * right * arr[i]
        return tot
    def nge(self, arr):
        stack =[]
        n = len(arr)
        res = [n]*n
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]]<=arr[i]:
                stack.pop()
            if stack and arr[stack[-1]]>arr[i]:
                res[i] = stack[-1]
            stack.append(i)
        return res
    def pge(self, arr):
        stack =[]
        n = len(arr)
        res = [-1]*n
        for i in range(n):
            while stack and arr[stack[-1]]<arr[i]:
                stack.pop()
            if stack and arr[stack[-1]]>=arr[i]:
                res[i] = stack[-1]
            stack.append(i)
        return res
    def sumSubarrayMaxs(self, arr: List[int]) -> int:
        nge = self.nge(arr)
        pge = self.pge(arr)
        tot = 0
        for i in range(len(arr)):
            # number of subarrays on left
            left = i - pge[i]
            # number of subarrays on right
            right = nge[i] - i
            tot += left * right * arr[i]
        return tot 
    def subArrayRanges(self, nums: List[int]) -> int:
        return self.sumSubarrayMaxs(nums) - self.sumSubarrayMins(nums)






##################################################################################################################################################






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
