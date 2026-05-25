# 1047. Remove All Adjacent Duplicates In String
# TC: O(n) SC:O(n)
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and stack[-1]!=i or not stack:
                stack.append(i)
            else:
                while stack and i == stack[-1]:
                    stack.pop()
        return "".join(stack)
