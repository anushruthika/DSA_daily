# 921. Minimum Add to Make Parentheses Valid

# brute: add either { or } at between every two characters.

# stack approach
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        # m- number of {
        count_m = 0
        # n- number of }
        count_n = 0
        for i in s:
            if i == '(':
                count_m+=1
                stack.append('(')
            else:
                if stack and stack[-1] == '(':
                    count_m -=1
                    stack.pop()
                else:
                    count_n+=1
                    stack.append(')')
        return len(stack)
  # optimized:
  class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        count_m = 0  # unmatched '('
        count_n = 0  # unmatched ')'

        for ch in s:
            if ch == '(':
                count_m += 1
            else:
                if count_m > 0:
                    count_m -= 1
                else:
                    count_n += 1

        return count_m+count_n
