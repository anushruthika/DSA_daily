# 796. Rotate String

# | Approach                         | Time      | Space    |
# | -------------------------------- | --------- | -------- |
# | Try every rotation (Brute Force) | **O(n²)** | **O(n)** |
# | `goal in (s+s)` (Optimal)        | **O(n)**  | **O(n)** |
# | KMP / Z Algorithm / Rabin-Karp   | **O(n)**  | **O(n)** |

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

# same solution with explanation
# Edge cases:
# s = '' t = '' output : True
# s = 'abd' t = 'ab' output: False because len of strings dont match
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        m = len(goal)
        if  n != m:
            return False
        if n == 0 :
            return True

        # space complexity O(2n) = O(n)
        # "abcde"+"abcde" = "abcdeabcde"
        s = s+s 

        # Time complexity O(2n) as size of s = 2n - O(n)
        # if goal in s:
        #     return True
        for i in range(n*2-n):
            if goal == s[i:i+n]:
                return True
        return False
        
