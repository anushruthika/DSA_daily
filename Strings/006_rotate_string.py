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
