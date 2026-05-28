# TC: O(n)
# SC: O(n)
# 907. Sum of Subarray Minimums

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
            # in general pse we will use >= but as in nse we include '=' we should not include here.  
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
        MOD = 10**9 + 7

        for i in range(len(arr)):

            # number of subarrays on left
            left = i - pse[i]

            # number of subarrays on right
            right = nse[i] - i

            tot += left * right * arr[i]

        return tot % MOD


class Solution(object):
    def sumSubarrayMins(self, arr):
        stack=[]
        min_=0
        n=len(arr)
        for i in range(n+1):
            while stack and (i==n or arr[stack[-1]]>=arr[i]):
                j = stack.pop()
                left_boundary = stack[-1] if stack else -1
                min_+=arr[j]*(j-left_boundary)*(i-j)
            stack.append(i)
        # The sum of the array is taken modulo (10^9 + 7) to avoid overflow and adhere to constraints.
        return min_%(10**9 + 7)

        
