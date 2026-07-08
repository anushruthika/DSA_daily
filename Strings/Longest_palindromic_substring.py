# | Algorithm            | Time    | Space   | Category                              |
# | -------------------- | ------- | ------- | ------------------------------------- |
# | Brute Force          | `O(n³)` | `O(1)`  | Enumeration                           |
# | DP                   | `O(n²)` | `O(n²)` | Dynamic Programming                   |
# | Expand Around Center | `O(n²)` | `O(1)`  | Two Pointers                          |
# | Manacher's           | `O(n)`  | `O(n)`  | String Algorithm / Symmetry Algorithm |

# Brute force TC: O(n**3) SC: O(n)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        i = 0
        n = len(s)
        ans = ''
        w =0
        while i<n-w:
            j = i+w
            while j<n:
                if s[i:j+1] == s[i:j+1][::-1]:
                    w = j-i+1
                    ans = s[i:j+1]
                j+=1
            i+=1
        return ans

