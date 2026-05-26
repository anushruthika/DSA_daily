# 496. Next Greater Element I
# TC: O(n) SC:O(n) n:len(nums2) n>m m:len(nums1)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = defaultdict(lambda: -1)
        # stores max_until now
        stack = []
        n = len(nums2)
        for i in range(n-1,-1,-1):
            while stack and stack[-1] < nums2[i]:
                stack.pop()
            if stack and nums2[i]<stack[-1]:
                d[nums2[i]] = stack[-1]
            stack.append(nums2[i])
        return [d[i]  for i in nums1]
