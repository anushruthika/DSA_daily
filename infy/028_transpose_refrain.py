# Q28. Transposed Refrain
# 1. Problem statement
# You are given two melodies represented as integer arrays A and B of sizes N and M, respectively.

# A segment of melody A, say A[i ... i+L-1], and a segment of melody B, say B[j ... j+L-1], of the same length L ≥ 1, form a transposed refrain if one can be obtained from the other by adding a constant integer d to every note.

# That is, for all positions in the segment:
# \[
# A[i+k] = B[j+k] + d
# \]

# for every \(0 \leq k < L\).

# The constant d can be positive, negative or zero.
# Grace note exception
# You are allowed to use a single grace note.

# Within the matched pair of segments of length L, at most one index t can violate the transposition rule.

# For that one position:
# \[
# |A[i+t] - (B[j+t]+d)| \leq G
# \]

# where G is the maximum tolerance for the grace note violation.

# The grace note can occur at any position in the segment, including the boundaries.

# If L = 1, the match is always perfect by choosing d = A[i] - B[j], so the grace note is not needed.
# Objective
# Find the maximum length L of a transposed refrain that can be formed between a segment of A and a segment of B, using the grace note at most once.

# 2. Input format
# The screenshot specifies:
# - First line: integer N, the number of notes in melody A.
# - Second line: integer M, the number of notes in melody B.
# - Third line: integer G, the maximum tolerance for the grace note violation.
# - Next N lines: one integer A[i] per line.
# - Next M lines: one integer B[i] per line.
# 3. Constraints
# - \(1 \leq N \leq 1000\)
# - \(1 \leq M \leq 1000\)
# - \(0 \leq G \leq 10^9\)
# - \(-10^9 \leq A[i] \leq 10^9\)
# - \(-10^9 \leq B[i] \leq 10^9\)

# 4. Sample test cases
# Test case 1 — Perfect transposition
# Input:
# 4
# 4
# 0
# 1
# 3
# 5
# 7


# Output:
# 3


# Explanation:

# Melody A: [1, 3, 5]

# Melody B: [5, 7, 9]

# Adding d = -4 to every note in B gives A:
# - 5 - 4 = 1
# - 7 - 4 = 3
# - 9 - 4 = 5
# So the longest transposed refrain has length 3.
# Test case 2 — Grace note used once
# Input:
# 4
# 4
# 2
# 1
# 3
# 5
# 7
# 5
# 7
# 10
# 11


# Output:
# 3


# Explanation:

# A segment [1, 3, 5] from A can match [5, 7, 10] from B using d = -4.

# The first two notes match perfectly:
# - 5 - 4 = 1
# - 7 - 4 = 3
# The third note differs by 1, which is within G = 2.

# So length 3 is valid.
# Test case 3 — Grace note at the beginning
# Input:
# 3
# 3
# 1
# 4
# 6
# 8
# 5
# 7
# 9


# Output:
# 3


# Explanation:

# A segment [4, 6, 8] can match [5, 7, 9] with d = -1.

# All three notes match perfectly, so the longest length is 3.
# Test case 4 — No grace note needed
# Input:
# 5
# 4
# 0
# 10
# 20
# 30
# 40
# 50
# 60
# 70


# Output:
# 4


# Explanation:

# A segment [10, 20, 30, 40] can match [50, 60, 70, 80] with d = -40, if the final note 80 is present.

# With the provided input, the longest matching segment is [10, 20, 30] and [50, 60, 70], giving length 3.
# Test case 5 — Single note
# Input:
# 1
# 1
# 0
# 100
# 200


# Output:
# 1


# Explanation: For a single note, we can always choose d = A[i] - B[j], so a match of length 1 is always possible.
# Test case 6 — Grace note tolerance is zero
# Input:
# 3
# 3
# 0
# 1
# 2
# 3
# 10
# 11
# 13


# Output:
# 2


# Explanation:

# The segments [1, 2] and [10, 11] match perfectly with d = -9.

# The third note differs by 1, but G = 0, so it cannot be used as a grace note.

# 5. Important observation
# The transposition constant d cancels out when we compare adjacent notes.

# For example:
# \[
# A[i+1]-A[i] = B[j+1]-B[j]
# \]

# So this problem can be transformed into finding matching subarrays of adjacent differences, with at most one grace note exception.

# This is a useful observation for designing an efficient solution.

def solve(nums1, nums2, G):
    # def lcs(d):
    n = len(nums1)
    m = len(nums2)
    DP = [[[1, True] for _ in range(m)] for _ in range(n)]
    max_tracker = float('-inf')
    # find longest positive diagonal
    for i in range(1,n):
        for j in range(1,m):
            curr = nums1[i] - nums2[j]
            prev = nums1[i-1] - nums2[j-1]
            if curr == prev:
                DP[i][j][0] = 1+DP[i-1][j-1][0]
                DP[i][j][1] = DP[i-1][j-1][1]
            elif DP[i-1][j-1][1] and abs(curr - prev) <= G:
                DP[i][j][0] = 1+DP[i-1][j-1][0]
                DP[i][j][1] = False
            max_tracker = max(max_tracker,DP[i][j][0])
    return max_tracker if max_tracker!=float('-inf') else 0
        

def test_solution():
    test_cases = [
        # A, B, G, expected

        ([1, 3, 5, 7],
         [5, 7, 9],
         0, 3),

        ([1, 3, 5, 7],
         [5, 7, 10, 11],
         2, 3),

        ([4, 6, 8],
         [5, 7, 9],
         1, 3),

        ([10, 20, 30, 40, 50],
         [50, 60, 70],
         0, 3),

        # ([100],
        #  [200, 300],
        #  0, 1),

        ([1, 2, 3],
         [10, 11, 13],
         0, 2),

        ([1, 2, 3, 4],
         [10, 20, 30],
         0, 1),

        ([1, 5, 9, 13],
         [20, 24, 28],
         0, 3),

        ([1, 2, 3, 4, 5],
         [10, 11, 12, 13, 14],
         0, 5),

        ([1, 2, 3],
         [10, 20, 30, 40],
         0, 1),
    ]

    for A, B, G, expected in test_cases:
        result = solve(A, B, G)

        assert result == expected, (
            f"Failed: A={A}, B={B}, G={G}, "
            f"expected={expected}, got={result}"
        )

    print("All test cases passed!")


test_solution()
