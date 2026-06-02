# 402. Remove K Digits
# TC: O(n) SC: O(n)
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for i in num:
            while stack and k and stack[-1]>i:
                stack.pop()
                k-=1
            stack.append(i)
        # edge case: num = "9" k = 1 res ="0" and not res= "9"
        stack=stack[:len(stack)-k]
        # edge case: num = "12" k = 2 res = "0" and not res="" 
        res="".join(stack).lstrip("0") 
        return res if res else "0"
        
