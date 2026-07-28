# 5. Longest Palindromic Substring

# | Algorithm            | Time    | Space   | Category                              |
# | -------------------- | ------- | ------- | ------------------------------------- |
# | Brute Force          | `O(n³)` | `O(1)`  | Enumeration                           |
# | DP                   | `O(n²)` | `O(n²)` | Dynamic Programming                   |
# | Expand Around Center | `O(n²)` | `O(1)`  | Two Pointers                          |
# | Manacher's           | `O(n)`  | `O(n)`  | String Algorithm / Symmetry Algorithm |

# edge case:
# CASE 1: 
# odd case: 
# s = "babad"  output=bab
# even case:
# s = "cbbd" output= bb

# len(s) == 0
# s = "" output = ""
# len(s) == 1
# s = "a" output= "a"


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

# Brute force For loop:
class Solution:    
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n==0 or n==1:
            return s
        width = 0
        for i in range(n):
            for j in range(i,n):
                if width<j-i+1 and s[i:j+1] == s[i:j+1][::-1]:
                    ans = s[i:j+1]
                    width=j-i+1
        return ans
            

# Expand around center
TC: O(n**2) Sc: O(n)
class Solution:
    def expand_from_center(self,left,right,s):
        while left>=0 and right<len(s) and s[left] == s[right]:
            left -=1
            right+=1
        return s[left+1:right]
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        max_str = ""
        for i in range(len(s)):
            odd = self.expand_from_center(i,i,s)
            even = self.expand_from_center(i,i+1,s)
            if len(max_str) < len(odd):
                max_str = odd
            if len(max_str) < len(even):
                max_str = even
        return max_str

# TC:O(n**2) SC:O(1)
class Solution: 
    def expand_from_center(self,s,left,right):
        while left>=0 and right<len(s) and s[left] == s[right]:
            left-=1
            right+=1
        return right-left-1,right-1,left+1
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n==0 or n==1:
            return s
        ans_left = 0
        ans_right = 0
        for center in range(n):
            len_odd,ro,lo = self.expand_from_center(s,center,center)
            len_even,re,le = self.expand_from_center(s,center,center+1)
            if len_odd > ans_right-ans_left+1:
                ans_right = ro
                ans_left = lo
            if len_even > ans_right-ans_left+1:
                ans_right = re
                ans_left = le
        return s[ans_left:ans_right+1]



