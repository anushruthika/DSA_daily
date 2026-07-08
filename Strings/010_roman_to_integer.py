# 13. Roman to Integer

# Time Complexity: O(n)
# - We traverse the string once, and each dictionary lookup is O(1).

# Space Complexity: O(1)
# - The dictionary has a fixed size of 7 entries, so it uses constant space.

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i = 0
        ans = 0
        n = len(s)
        while i<n:
            if i+1<n and roman[s[i+1]]>roman[s[i]]:
                ans+=roman[s[i+1]]-roman[s[i]]
                i=i+1
            else:
                ans+=roman[s[i]]
            i+=1
        return ans
