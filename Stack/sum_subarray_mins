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






        
