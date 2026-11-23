# Divisibility of Array Elements
# Difficulty: Hard
# Topic: Arrays
# Exam: Infosys SP / DSE
# Problem statement
# You are given two integers, N and K.

# Count the total number of integer arrays of length K that satisfy all the following conditions:
# 1. Range constraint: Every element a[i] lies within [1, N].
# 2. Strictly increasing and distinct: All elements must be unique and strictly increasing:
#    \[
#    a[i] < a[i+1]
#    \]
#    for all 0 ≤ i < K-1.
# 3. Divisibility constraint: For every consecutive pair of elements, the next element must be divisible by the previous element:
#    \[
#    a[i+1] \bmod a[i] = 0
#    \]
#    for all 0 ≤ i < K-1.
# Return the total count modulo 10000.
# Input format
# A single line containing two space-separated integers N and K.
# Output format
# Print the total number of valid arrays modulo 10000.

# Examples
# Example 1
# Input
# 5 2


# Output
# 5


# Explanation

# The valid arrays are:
# [1, 2]
# [1, 3]
# [1, 4]
# [1, 5]
# [2, 4]


# There are 5 valid arrays.
# Example 2
# Input
# 5 3


# Output
# 1


# Explanation

# The only valid array is:
# [1, 2, 4]


# There are 1 valid array.
# Example 3
# Input
# 4 2


# Output
# 4


# Explanation

# The valid arrays are:
# [1, 2]
# [1, 3]
# [1, 4]
# [2, 4]


# There are 4 valid arrays.
# Example 4
# Input
# 6 3


# Output
# 3


# Explanation

# The valid arrays are:
# [1, 2, 4]
# [1, 2, 6]
# [1, 3, 6]


# There are 3 valid arrays.
# Example 5
# Input
# 5 1


# Output
# 5


# Explanation

# When K = 1, every single-element array from [1] to [5] is valid:
# [1], [2], [3], [4], [5]


# There are 5 valid arrays.

class Solution:
    def countArrays(self, N, K):
        def dfs(num,k_left,prev):
            if k_left == 0:
                return 1
            if num==N:
                if k_left==1 and num%prev == 0:
                    return 1
                return 0
            take = 0
            if num%prev == 0:
                take = dfs(num+1,k_left-1,num)
            not_take = dfs(num+1,k_left,prev)
            # print(take,not_take,num,prev,k_left)
            return take+not_take
        return dfs(1,K,1)   
            
        pass


test_cases = [
    # Sample examples
    (5, 2, 5),
    (5, 3, 1),
    (4, 2, 4),
    (6, 3, 3),
    (5, 1, 5),

    # Edge cases
    (1, 1, 1),
    (1, 2, 0),
    (2, 2, 1),
    (3, 2, 2),
    (3, 3, 0),

    # Additional cases
    (4, 3, 1),
]


sol = Solution()

for i, (N, K, expected) in enumerate(test_cases, 1):
    actual = sol.countArrays(N, K)

    if actual == expected:
        print(f"Test {i}: PASS")
    else:
        print(
            f"Test {i}: FAIL | "
            f"N={N}, K={K} | "
            f"Expected={expected}, Actual={actual}"
        )
