KMP algorithm: Knuth-Morris-Pratt KMP String Matching Algorithm
# https://www.geeksforgeeks.org/problems/search-pattern0205/1
# https://www.youtube.com/watch?v=V5-7GzOfADQ

# Time Complexity: O(n + m)
# Space Complexity: O(m)
#
# n = length of text
# m = length of pattern



# lps[i] = length of the longest proper prefix
#          that is also a suffix
#          for pattern[0:i+1]

# Example 1:
# Text    : ABABDABACDABABCABAB
# Pattern : ABABCABAB

# Pattern Indices:
# A B A B C A B A B
# 0 1 2 3 4 5 6 7 8

# LPS Array:
# 0 0 1 2 0 1 2 3 4

# Pattern occurs at index: 10


# Example 2:
# Text    : AABAACAADAABAABA
# Pattern : AABA

# Pattern Indices:
# A A B A
# 0 1 2 3

# LPS Array:
# 0 1 0 1

# Pattern occurs at indices: 0, 9, 12


class Solution:
    def buildLPS(self, pattern):
        n = len(pattern)
        lps = [0] * n

        length = 0
        i = 1

        while i < n:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps

    def search(self, pattern,text):
        # This is actually KMP, not Rabin-Karp.
        n = len(text)
        m = len(pattern)

        if m > n:
            return []

        lps = self.buildLPS(pattern)

        ans = []

        i = 0  # pointer for text
        j = 0  # pointer for pattern

        while i < n:
            if text[i] == pattern[j]:
                i += 1
                j += 1

            if j == m:
                ans.append(i - j)
                j = lps[j - 1]

            elif i < n and text[i] != pattern[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return ans
        
