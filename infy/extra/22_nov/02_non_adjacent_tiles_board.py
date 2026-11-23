# Non-Adjacent Single Tiles on a 2 × N Board
# You are given a grid of size 2 × N (2 rows and N columns).

# You can completely cover the grid using the following tiles, without gaps or overlaps:
# - Dominoes: Cover 2 orthogonally adjacent cells, either horizontally (1 × 2) or vertically (2 × 1).
# - Single tiles: Cover exactly 1 cell (1 × 1).
# There is one restriction:

# No two single (1 × 1) tiles may be orthogonally adjacent. They cannot share a horizontal or vertical edge. Diagonal touching is allowed.

# Find the total number of valid ways to tile the 2 × N grid.

# Since the answer can be large, return it modulo:
# \[
# 10^9+7
# \]

# Input format
# A single integer N.
# Output format
# Print a single integer: the number of valid tilings modulo 10^9 + 7.
# Constraints
# - N can be large.
# Sample examples
# Example 1
# Input:
# 1

# Output:
# 1


# Explanation: The 2 × 1 board can only be covered by one vertical domino.
# Example 2
# Input:
# 2

# Output:
# 2


# Explanation: There are 2 valid ways:
# Way 1:          Way 2:

# D D             H H
# D D             H H


# D represents a domino. H represents a horizontal domino occupying two cells.
# Example 3
# Input:
# 3

# Output:
# 5


# Explanation: There are 5 valid tilings of the 2 × 3 board, including:
# S D D
# D D S


# Here, S represents a single tile. The two single tiles are diagonally touching, which is allowed.
# Example 4
# Input:
# 4

# Output:
# 11


# Explanation: There are 11 valid ways to tile a 2 × 4 board while ensuring no two single tiles share an edge.
class Solution:
    def countWays(self, N):
        # Write your logic here
        pass


test_cases = [
    (1, 1),
    (2, 2),
    (3, 5),
    (4, 11),
    (5, 21),
    (6, 43),
    (7, 85),
    (8, 171),
]

sol = Solution()

for n, expected in test_cases:
    actual = sol.countWays(n)

    if actual == expected:
        print(f"N={n}: PASS")
    else:
        print(f"N={n}: FAIL | Expected={expected}, Actual={actual}")
