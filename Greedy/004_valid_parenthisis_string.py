# 678. Valid Parenthesis String
# TC: O(3^k) - Each '*' creates 3 branches, worst case: s = "********"
# SC: O(n)

class Solution:
    def checkValidString(self, s: str) -> bool:
        def dfs(ind,balance):
            if balance<0:
                return False
            if ind == len(s):
                return balance == 0
            if s[ind] == '(':
                return dfs(ind+1,balance+1)
            elif s[ind] == ')':
                return dfs(ind+1,balance-1)
            else:
                return dfs(ind+1,balance+1) or dfs(ind+1,balance) or dfs(ind+1,balance-1)
        return dfs(0,0)

############# MEMOTISATION YET TO ADD

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
