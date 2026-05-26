# 503. Next Greater Element II
# TC: O(2n) = O(n) SC: O(n) res
class Solution:
    def nextGreaterElements(self, nums2: List[int]) -> List[int]:
        stack = []
        n = len(nums2)
        res = [-1]*n
        for i in range(2*n-1,-1,-1):
            while stack and stack[-1] <= nums2[i%n]:
                stack.pop()
            if stack and nums2[i%n]<stack[-1]:
                res[i%n] = stack[-1]
            stack.append(nums2[i%n])
        return res
