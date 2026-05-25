# 2696. Minimum String Length After Removing Substrings
# TC: O(n) SC: O(n)
class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for i in s:
            if i =='B' and stack and stack[-1] == 'A':
                    stack.pop()
            elif i == 'D'and stack and stack[-1] == 'C':
                    stack.pop()
            else:
                stack.append(i)
        return len(stack)
                
