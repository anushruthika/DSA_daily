# 2697. Lexicographically Smallest Palindrome

# TC: O(n) (reversing)
# SC: O(n) store new string
class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n = len(s)
        i =0
        j= n-1
        new_s = ''
        while i<j:
            if s[i]!=s[j]:
                if s[i]<s[j]:
                    new_s+=s[i]
                else:
                    new_s+=s[j]
            else:
                new_s+=s[i]
            i+=1
            j-=1
        if n%2!=0:
            return new_s+s[i]+new_s[::-1]
        else:
            return new_s+new_s[::-1]
