# Use KMP on s + "#" + reverse(s) to find the length of the longest palindromic prefix, then prepend the reverse of the remaining suffix.

# 214. Shortest Palindrome
# Time Complexity: O(n)
# Space Complexity: O(n)

# s = "aabba"
# aabba#abbaa
# lps: [0,1,0,0,1,0,1,0,0,1,2]
# ans: abb + aa bba => aa is repeating thus no need to add. answer: 2

# s = "abcd"
# abcd#dcba
# lps: [0,0,0,0,0,0,0,0,1]
# ans: dcb + a bcd => a is repeating thus no need to add. answer: 1


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s

        rev = s[::-1]
        t = s + "#" + rev

        n = len(t)
        lps = [0] * n

        length = 0
        i = 1

        while i < n:
            if t[i] == t[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length:
                length = lps[length - 1]
            else:
                i += 1

        longest = lps[-1]

        return rev[:len(s) - longest] + s
        
