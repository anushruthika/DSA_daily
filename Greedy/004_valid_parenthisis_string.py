# 678. Valid Parenthesis String

# TC: O(n)
# Traverse the string once, updating low and high for each character.
# SC: O(1)
# Only two variables (low, high) are used regardless of input size.
class Solution:
    def checkValidString(self, s: str) -> bool:
        # low = minimum possible number of unmatched '('
        # high = maximum possible number of unmatched '('
        low = 0
        high = 0
        for i in s:
            if i == '(':
                low,high= low+1,high+1
            elif i==')':
                low,high = max(low-1,0),high-1
            else:
                low = max(low-1,0)
                high+=1
            if high<0:
                return False
        return low==0
