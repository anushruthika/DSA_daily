# https://www.geeksforgeeks.org/problems/search-pattern-rabin-karp-algorithm--141631/1

# Average Time: O(n + m)
# Worst Time: O(nm) (many hash collisions)
# Auxiliary Space: O(1)
# Including output: O(number_of_matches) → worst case O(n)

# space
| Space            |          |
| ---------------- | -------- |
| Auxiliary        | **O(1)** |
| Including output | **O(n)** |


# 1. Rabin-Karp is a string matching algorithm that uses hashing to find a pattern inside a text.
# 2. Instead of comparing the pattern with every substring character by character, it compares their hash values.
#   Hashing allows us to reject most non-matching substrings by comparing their hash values in O(1) time instead of comparing m characters each time, 
#   reducing the average complexity from O(nm) to O(n+m).


# HASHING

# 2. Polynomial Rolling Hash (used in Rabin-Karp)
# Hash(s)
# =
# (s[0] × p⁰ +
#  s[1] × p¹ +
#  s[2] × p² +
#  ...
#  s[n−1] × pⁿ⁻¹) mod m

# where:

# s[i] = mapped character value
# p = prime base (31, 53, etc.)
# m = large prime modulus (10⁹+7, 10⁹+9)

# Example:

# Hash("abc")
# =
# 1×31⁰ + 2×31¹ + 3×31²
# =
# 1 + 62 + 2883
# =
# 2946

# eG: 
# Text    = "ababcabc"
# Pattern = "abc"
# op: [2,5]

# contraints: Both the strings consist of lowercase English alphabets. thus base = 26 
# if lower and upper case then base = 26+26
# m =  2^31 to limit answer within integer range.
# d = {'a':1,'b':2,'c':3}
# hash("abc")
# = 1 × 26² + 2 × 26¹ + 3 × 26⁰ % 2^31
# = 676 + 52 + 3
# = 731

class Solution:
    def rabinKarp(self, text, pattern):
        n = len(text)
        m = len(pattern)

        if m > n:
            return []

        base = 26
        mod = 10**9 + 7
        power = pow(base, m - 1, mod)

        ph = 0  # pattern hash
        th = 0  # text window hash

        # Initial hashes
        for i in range(m):
            ph = (
                ph * base
                + (ord(pattern[i]) - ord('a') + 1)
            ) % mod

            th = (
                th * base
                + (ord(text[i]) - ord('a') + 1)
            ) % mod

        ans = []

        # Sliding window
        for i in range(n - m + 1):

            # Hash matches
            if ph == th:
                # Verify actual strings to avoid collisions
                # if text[i:i + m] == pattern:
                ans.append(i)

            # Compute next window hash
            if i < n - m:

                left = ord(text[i]) - ord('a') + 1
                right = ord(text[i + m]) - ord('a') + 1

                th = (
                    (
                        th
                        - left * power
                    ) % mod
                )

                th = (
                    th * base
                    + right
                ) % mod

        return ans
