# Problem: Maximum Rods of Length L
# You are given N rods with lengths stored in an array rod, where rod[i] represents the length of the i-th rod.

# You are also given:
# - L — the target rod length.
# - K — the maximum number of cuts allowed in total across all rods.
# You can cut a rod of length x into pieces of integer lengths.

# If you make c cuts on a rod, it is split into c + 1 pieces whose lengths sum to x.

# Rules:
# - Any piece with length less than L is discarded.
# - Any piece with length at least L can yield at most one rod of exact length L.
# - Any extra length beyond L is wasted.
# - You can use at most K cuts in total.
# Find the maximum number of rods of exact length L that can be obtained.
# Input format
# First line contains three integers N, L, K.
# Second line contains N space-separated integers representing rod.


# Output format
# Print a single integer representing the maximum number of rods
# of exact length L that can be formed.


# Constraints
# 1 <= N <= 10^5
# 1 <= rod[i], L <= 10^9
# 0 <= K <= 10^14


# Sample
# Input:
# 3 5 2
# 12 6 4

# Output:
# 2


# Explanation
# Target length L = 5, maximum cuts K = 2.
# - Rod of length 6 can produce one rod of length 5 using 1 cut. The leftover length is 1.
# - Rod of length 12 can produce two rods of length 5 using 2 cuts. The leftover length is 2.
# - Rod of length 4 is shorter than 5, so it cannot produce a rod of length 5.
# We have only 2 cuts in total. We can use 1 cut on the rod of length 6 and 1 cut on the rod of length 12, producing 2 rods of length 5.

# Therefore, the answer is 2
