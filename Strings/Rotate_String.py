class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            if s[i:]+s[:i] == goal:
                return True
        return False
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if goal in s+s and len(goal)==len(s):
            return True
        return False
