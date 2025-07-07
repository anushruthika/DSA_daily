# optimized implementation stack
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d={}
        for n in nums2:
            while stack and stack[-1]<n:
                d[stack.pop(-1)] = n
            stack.append(n)
        for j in stack:
            d[j] =-1
        return [d[i] for i in nums1]
# easier to understand stack implementation
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d={}
        for i in nums2[::-1]:
            while len(stack)>0 and i > stack[-1]:
                stack.pop(-1)
            if len(stack) == 0:
                d[i] = -1
            else:
                d[i] = stack[-1]
            stack.append(i)
        arr=[]
        for i in nums1:
            arr.append(d[i])
        return arr
# array implementation
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr=[]
        for i in nums1:
            x = nums2.index(i)
            flag=0
            for j in range(x, len(nums2)):
                if nums2[j] >i:
                    arr.append(nums2[j])
                    flag=1
                    break
            if flag==0:
                arr.append(-1)
        return arr
