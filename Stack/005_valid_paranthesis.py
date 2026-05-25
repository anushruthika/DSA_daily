# 20. Valid Parentheses

# TC: O(n)
# Each bracket is pushed and popped at most once.
# SC: O(n)
# Stack can store all opening brackets in worst case.

# Edge Cases:
# 1. Only opening bracket
# "["
# Output: False

# 2. Closing bracket before opening bracket
# "]"
# Output: False

# 3. Mismatched brackets
# "(]"
# Output: False

# 4. Properly nested brackets
# "{[]}"
# Output: True

# 5. Empty string
# ""
# Output: True
class Solution:
    def isValid(self, s: str) -> bool:
        p = {'{':'}','(':')','[':']'}
        stack = []
        for i in s:
            if i in p:
                stack.append(i)
                continue
            if not stack:
                return False
            x = stack.pop()
            if p[x] != i:
                return False
        return not stack
