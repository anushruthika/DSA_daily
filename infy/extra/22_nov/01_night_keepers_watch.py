# Problem: Night Keeper's Watch

# A keeper guards a palace for N consecutive nights, indexed from 0 to N-1.

# On each night, the keeper can either:
# - Rest, earning 0 points.
# - Stay alert, earning matrix[i][0] points.

# You are given an N x 2 matrix:
# - matrix[i][0] represents the points earned if the keeper stays alert on night i.
# - matrix[i][1] represents the weather condition on night i:
#     1 means storm.
#     0 means safe.

# The keeper must follow two rules:

# 1. Storm Rule:
#    If matrix[i][1] == 1, the keeper must stay alert on night i.

# 2. Fatigue Rule:
#    In every W consecutive nights, the keeper must rest at least once.
#    The keeper cannot stay alert for W consecutive nights.

# Return the maximum total points the keeper can earn over all N nights.
# If it is impossible to satisfy both rules, return -1.


# Example 1:

# Input:
# N = 5
# W = 2

# matrix = [
#     [5, 0],
#     [1, 0],
#     [4, 1],
#     [3, 0],
#     [6, 0]
# ]

# Output:
# 15

# Explanation:
# The keeper stays alert on nights 0, 2, and 4.

# Night 0: Alert -> 5 points
# Night 1: Rest  -> 0 points
# Night 2: Alert -> 4 points
# Night 3: Rest  -> 0 points
# Night 4: Alert -> 6 points

# Total points = 5 + 4 + 6 = 15


# Example 2:

# Input:
# N = 4
# W = 3

# matrix = [
#     [3, 0],
#     [8, 0],
#     [2, 0],
#     [7, 0]
# ]

# Output:
# 18

# Explanation:
# The keeper stays alert on nights 0, 1, and 3.

# Night 0: Alert -> 3 points
# Night 1: Alert -> 8 points
# Night 2: Rest  -> 0 points
# Night 3: Alert -> 7 points

# Total points = 3 + 8 + 7 = 18


# Example 3:

# Input:
# N = 3
# W = 1

# matrix = [
#     [5, 0],
#     [4, 1],
#     [6, 0]
# ]

# Output:
# -1

# Explanation:
# When W = 1, every night must contain a rest.
# However, night 1 has a storm, so the keeper must stay alert.
# Both rules cannot be satisfied.
# Therefore, return -1.

class Solution:
    def maxPoints(self, N, W, matrix):
        
        def func(ind,w_left):
            if ind == N-1:
                if w_left>0:
                    return matrix[ind][0]
                elif matrix[ind][1] == 1:
                    return float('-inf')
                return 0
            if w_left<0:
                return float('-inf')
            if w_left == 0 and matrix[ind][1] == 1:
                return float('-inf')
            take = float('-inf')
            if w_left>0:
                take = matrix[ind][0] + func(ind+1,w_left-1)
            not_take = float('-inf')
            if matrix[ind][1] != 1: 
                not_take = func(ind+1,W-1)
            return max(take,not_take)
        return max(-1,func(0,W-1))


test_cases = [
    # W = 1: every night must be rest, so safe nights earn 0
    {
        "N": 1,
        "W": 1,
        "matrix": [[7, 0]],
        "expected": 0
    },
    {
        "N": 1,
        "W": 1,
        "matrix": [[7, 1]],
        "expected": -1
    },

    # W = N
    {
        "N": 2,
        "W": 2,
        "matrix": [[3, 0], [8, 0]],
        "expected": 8
    },
    {
        "N": 3,
        "W": 3,
        "matrix": [[1, 0], [5, 0], [4, 0]],
        "expected": 9
    },
    {
        "N": 4,
        "W": 4,
        "matrix": [[10, 0], [2, 0], [7, 0], [3, 0]],
        "expected": 20
    },

    # W = 2
    {
        "N": 3,
        "W": 2,
        "matrix": [[4, 0], [9, 0], [2, 0]],
        "expected": 9
    },
    {
        "N": 4,
        "W": 2,
        "matrix": [[6, 0], [5, 0], [8, 0], [3, 0]],
        "expected": 14
    },
    {
        "N": 4,
        "W": 2,
        "matrix": [[6, 1], [5, 0], [8, 0], [3, 1]],
        "expected": 9
    },
    {
        "N": 4,
        "W": 2,
        "matrix": [[2, 1], [9, 0], [4, 0], [7, 0]],
        "expected": 9
    },

    # W = 3
    {
        "N": 5,
        "W": 3,
        "matrix": [[2, 0], [10, 0], [7, 0], [9, 0], [4, 0]],
        "expected": 25
    },
    {
        "N": 6,
        "W": 3,
        "matrix": [[5, 0], [1, 1], [8, 0], [6, 0], [4, 1], [9, 0]],
        "expected": 22
    },
    {
        "N": 7,
        "W": 3,
        "matrix": [[2, 0], [9, 0], [3, 0], [8, 0], [5, 0], [7, 0], [4, 0]],
        "expected": 30
    },
]
sol = Solution()

for idx, tc in enumerate(test_cases, 1):
    actual = sol.maxPoints(
        tc["N"],
        tc["W"],
        tc["matrix"]
    )

    if actual == tc["expected"]:
        print(f"Test Case {idx}: PASS")
    else:
        print(f"Test Case {idx}: FAIL")
        print("Expected:", tc["expected"])
        print("Actual:", actual)
