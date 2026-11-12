# # Q1. Maximum Points Covered by a Length-L Window

# ## Problem Statement

# You are given an array `pts` of `N` integers representing point positions on a number line. You are also given a window length `L` and a modulo factor `K`.

# You must select a subset of points from `pts` that satisfies the following two conditions:

# 1. All points in the selected subset must yield the exact same remainder when divided by `K`.
# 2. The difference between the maximum position and minimum position in the selected subset must be less than or equal to `L`.

# Find the maximum number of points you can include in a valid subset.

# ## Input Format

# - The first line contains an integer `N`, denoting the total number of points.
# - The second line contains an integer `L`max, denoting the maximum allowed distance between the smallest and largest point in the subset.
# - The third line contains an integer `K`, denoting the modulo factor.
# - The fourth line contains `N` space-separated integers representing the point positions in array `pts`.

# ## Output Format

# Print a single integer representing the maximum number of points that can be included in a valid subset.

# ## Sample Test Case 1

# Input:

# ```text
# 7
# 5
# 3
# 1 4 7 2 5 8 10
# ```

# Output:

# ```text
# 3
# ```

# Explanation:

# Remainder groups when divided by 3:

# - Remainder 1: `[1, 4, 7, 10]`
# - Remainder 2: `[2, 5, 8]`

# For remainder 1, the maximum number of points within a window of length 5 is 2.

# For remainder 2, we can select `[2, 5, 8]`, but the difference is `8 - 2 = 6`, which exceeds 5. So the maximum valid selection is 2.

# Actually, the answer for this input is 2.

# ## Sample Test Case 2

# Input:

# ```text
# 6
# 4
# 2
# 1 3 5 7 9 11
# ```

# Output:

# ```text
# 3
# ```

# Explanation:

# All points have remainder 1 when divided by 2.

# We can select `[1, 3, 5]`, whose difference is `5 - 1 = 4`.

# Maximum subset size = 3.

# ## Sample Test Case 3

# Input:

# ```text
# 5
# 10
# 5
# 2 7 12 17 22
# ```

# Output:

# ```text
# 3
# ```

# Explanation:

# All points have remainder 2 when divided by 5.

# We can select `[2, 7, 12]`, whose difference is `12 - 2 = 10`.

# Maximum subset size = 3.



from collections import defaultdict
def maximumPoints(pts, L, K):
    N = len(pts)
    groups = defaultdict(list)
    
    for i in range(N):
        groups[pts[i]%K].append(pts[i])
    max_wind = 0
    for rem in groups:
        l = sorted(groups[rem])
        # print(l)
        i = 0
        j = 0
        while j<len(l):
            while i<len(l) and l[j]-l[i]>L:
                i+=1
            # print(j,i)
            max_wind = max(max_wind,j-i+1)
            j+=1
        
    return max_wind


test_cases = [
    # Basic examples
    ([1, 4, 7, 2, 5, 8, 10], 5, 3, 2),
    ([1, 3, 5, 7, 9, 11], 4, 2, 3),
    ([2, 7, 12, 17, 22], 10, 5, 3),

    # Already sorted
    ([1, 2, 3, 4, 5], 3, 1, 4),

    # All same remainder
    ([1, 4, 7, 10, 13], 6, 3, 3),

    # Multiple remainder groups
    ([1, 2, 3, 4, 5, 6, 7, 8], 3, 2, 2),

    # Duplicate positions
    ([2, 2, 2, 5, 5, 8, 8], 3, 3, 5),

    # Negative positions
    ([-8, -5, -2, 1, 4, 7], 6, 3, 3),

    # Window length zero
    ([1, 2, 3, 4, 5], 0, 2, 1),

    # Large window
    ([1, 5, 9, 13, 17], 100, 4, 5),

    # Single element
    ([10], 5, 3, 1),

    # Different remainders
    ([1, 6, 11, 16, 2, 7, 12], 10, 5, 3),
]


def brute_force(pts, L, K):
    if not pts:
        return 0

    best = 0

    for remainder in range(K):
        group = [x for x in pts if x % K == remainder]

        for left in range(len(group)):
            for right in range(left, len(group)):
                if max(group[left:right+1]) - min(group[left:right+1]) <= L:
                    best = max(best, right - left + 1)

    return best


print("========== TEST RESULTS ==========")

for i, (pts, L, K, expected) in enumerate(test_cases, 1):
    actual = maximumPoints(pts, L, K)
    if actual == expected:
        status = "PASS"  
    else :
        status = "FAIL"
    print(f"\nTest Case {i}: {status}")
    print("Array:", pts)
    print("L:", L, "K:", K)
    print("Expected:", expected)
    print("Actual:", actual)
    

print("\n========== TESTING COMPLETE ==========")
