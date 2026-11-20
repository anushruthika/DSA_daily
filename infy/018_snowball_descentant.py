# Q18. Snowball Descent
# You are given a triangular mountainside with N rows, where row i contains exactly i cells.

# Each cell (i, j) contains a non-negative integer d[i][j], representing its snow depth.

# A snowball starts above the apex of the mountain with an initial mass M. It enters cell (1, 1) and rolls down the mountain.

# From any cell (i, j), you can move to either:
# - Cell (i + 1, j)
# - Cell (i + 1, j + 1)
# The process continues until the snowball exits below row N.

# When the snowball passes through a cell with snow depth d, its mass increases by:min(d,current mass)

# Therefore, its new mass becomes:
# \[
# \text{new mass} = \text{current mass} + \min(d,\text{current mass})
# \]

# Find the maximum final mass the snowball can achieve after exiting row N.
# Input format
# - First line: Integer N, the number of rows.
# - Second line: Integer M, the initial mass of the snowball.
# - Next N lines: Row i contains i space-separated integers representing the snow depths.
# Output format
# Print a single integer representing the maximum achievable final mass.

# Examples
# Example 1
# Input:
# 3
# 2
# 1
# 2 3
# 4 5 6

# Output:
# 12


# Explanation:

# One possible path is:
#        1       Mass: 2 + min(1, 2) = 3
#       /
#      3         Mass: 3 + min(3, 3) = 6
#     /
#    6           Mass: 6 + min(6, 6) = 12


# Final mass = 12.

# Example 2
# Input:
# 2
# 3
# 1
# 2 4

# Output:
# 8


# Explanation:
# - Initial mass = 3
# - Enter cell with depth 1: mass becomes 4.
# - Choose cell with depth 4: mass becomes 8.
# Maximum final mass = 8.



def your_function(N,M,triangle):
    def dfs(i,j,mass):
        if i == N:
            return mass
        x = mass+min(mass,triangle[i][j])
        return max(dfs(i+1,j,x),dfs(i+1,j+1,x))
    return dfs(0,0,M)

test_cases = [
    # (N, M, triangle, expected_output)

    # Test 1: Single cell
    (1, 5, [[3]], 8),

    # Test 2: Two rows
    (2, 3, [[1], [2, 4]], 8),

    # Test 3: Three rows
    (3, 2, [[1], [2, 3], [4, 5, 6]], 12),

    # Test 4: Zero snow in lower rows
    (3, 1, [[10], [0, 0], [0, 0, 0]], 2),

    # Test 5: Different paths have different snow depths
    (3, 4, [[0], [100, 1], [0, 0, 100]], 10),

    # Test 6: Four rows
    (4, 2, [[1], [2, 3], [4, 5, 6],
           [7, 8, 9, 10]], 22),

    # Test 7: Mixed snow depths
    (4, 5, [[3], [1, 8], [2, 0, 4],
           [9, 1, 7, 3]], 27),

    # Test 8: Initial mass is already large
    (3, 10, [[1], [1, 1], [1, 1, 1]], 13),

    # Test 9: Snow depth much larger than mass
    (3, 2, [[100], [100, 100],
            [100, 100, 100]], 16),

    # Test 10: All cells have zero snow
    (4, 7, [[0], [0, 0], [0, 0, 0],
            [0, 0, 0, 0]], 7),
]


def test_your_solution(your_function):
    for n, m, triangle, expected in test_cases:
        actual = your_function(n, m, triangle)

        status = "PASS" if actual == expected else "FAIL"

        print(
            f"N={n}, M={m}, "
            f"Expected={expected}, Actual={actual} -> {status}"
        )


# Standalone function:
test_your_solution(your_function)

# Class-based solution:
# sol = Solution()
# test_your_solution(sol.maximumMass)
