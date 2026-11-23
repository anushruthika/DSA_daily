# Problem: Painting the Rooms
# You are given N rooms and an array litres of length N, where litres[i] represents the number of litres of paint required to paint the i-th room.

# All the paint is pooled together, so you need at least:
# \[
# T = \sum_{i=0}^{N-1} litres[i]
# \]

# litres of paint in total.

# You can buy paint any number of times using two pack options:
# - Single pack: Costs a and provides 1 litre of paint.
# - Bulk pack: Costs b and provides S litres of paint.
# You are allowed to buy more paint than strictly required if bulk packs are cheaper overall.

# Find the minimum total cost required to obtain at least T litres of paint.
# Input format
# - First line contains four integers: N, a, b, and S.
# - Second line contains N space-separated integers representing the array litres.
# Output format
# Print a single integer representing the minimum total cost.
# Constraints
# 1 <= N <= 10^5


# Example 1
# Input:
# 3 4 10 3
# 2 1 3

# Output:
# 20


# Explanation:

# Total paint required:
# T = 2 + 1 + 3 = 6 litres


# Each single pack costs 4, and each bulk pack costs 10 and provides 3 litres.

# Buying 2 bulk packs provides 6 litres.
# Total cost = 2 * 10 = 20


# Minimum cost = 20.
# Example 2
# Input:
# 3 3 12 5
# 2 1 4

# Output:
# 18


# Explanation:
# T = 2 + 1 + 4 = 7 litres


# Buy 1 bulk pack and 2 single packs.
# Paint obtained = 5 + 2 = 7 litres
# Total cost = 12 + 2 * 3 = 18


# Minimum cost = 18.
# Example 3
# Input:
# 4 5 8 4
# 3 2 1 3

# Output:
# 21


# Explanation:
# T = 3 + 2 + 1 + 3 = 9 litres


# Buy 2 bulk packs and 1 single pack.
# Paint obtained = 4 + 4 + 1 = 9 litres
# Total cost = 8 + 8 + 5 = 21


# Minimum cost = 21.
class Solution:
    def minCost(self, N, a, b, S, litres):
        T = sum(litres)

        # Buy everything using single packs
        single_cost = T * a

        # Buy bulk packs and cover the remainder with singles
        bulk_count = T // S
        remainder = T % S

        mixed_cost = bulk_count * b + remainder * a

        # Buy one extra bulk pack instead of singles for remainder
        extra_bulk_cost = (bulk_count + 1) * b

        return min(single_cost, mixed_cost, extra_bulk_cost)


test_cases = [
    # N, a, b, S, litres, expected
    (3, 4, 10, 3, [2, 1, 3], 20),
    (3, 3, 12, 5, [2, 1, 4], 18),
    (4, 5, 8, 4, [3, 2, 1, 3], 21),
    (2, 6, 10, 2, [2, 3], 26),
    (2, 3, 20, 4, [2, 4], 18),
    (1, 5, 12, 4, [3], 12),
]

sol = Solution()

for idx, (N, a, b, S, litres, expected) in enumerate(test_cases, 1):
    actual = sol.minCost(N, a, b, S, litres)

    if actual == expected:
        print(f"Test Case {idx}: PASS")
    else:
        print(f"Test Case {idx}: FAIL")
        print(f"Expected: {expected}")
        print(f"Actual:   {actual}")
