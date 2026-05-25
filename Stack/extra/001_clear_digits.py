# 3174. Clear Digits

# TC: O(n) SC: O(n)
class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for i in s:
            if i.isdigit():
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)
