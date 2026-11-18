# # Q8. Tug Of War Captain

# ## Problem Statement

# You are given `N` kids, where the i-th kid has a strength of `s[i]`. The kids will line up to grab a rope one at a time, in the order that you choose.

# When a kid grabs the rope, they must join the side (left or right) that currently has the lower total strength.

# If the two sides currently have equal total strength (including at the very beginning, when both sides have 0 strength), the kid can choose to join either side.

# Before the process begins, you must appoint exactly one kid as the captain. The captain's strength is doubled for the entire process.

# Your goal is to choose the captain and the order in which the kids join the rope to minimize the absolute difference between the total strength of the left side and the right side (the final imbalance).

# Find the minimum possible final imbalance.

# ## Input Format

# - The first line contains an integer `N`, denoting the number of kids.
# - Each of the N subsequent lines contains an integer `s[i]`.

# ## Constraints

# - 1 ≤ N ≤ 10^5
# - 1 ≤ s[i] ≤ 10^9

# ## Examples

# ### Example 1

# **Input:**
# ```text
# 2
# 1
# 2
# ```

# **Output:**
# ```text
# 0
# ```

# **Explanation:**

# Choose the kid with strength 1 as captain. Their effective strength becomes 2.

# - Kid 1 joins the left side: Left = 2, Right = 0.
# - Kid 2 must join the right side: Left = 2, Right = 2.

# Final imbalance = |2 - 2| = 0.



import heapq

def solve(N, A):
    ans = float('inf')
    for captain in range(N):
        pq = [(0,0),(0,1)] # 0-A, 1-B
        arr = sorted([A[captain]*2]+A[0:captain]+A[captain+1:N],reverse = True)
        for strength in arr:
            sum_,team = heapq.heappop(pq)
            heapq.heappush(pq,(sum_+strength,team))
        # print(pq,arr)
        ans = min(ans,abs(pq[0][0]-pq[1][0]))
    return ans

# Format: (N, A, expected_output)
tests = [
    (2, [1, 2], 0),
    (2, [10, 20], 0),

    (3, [1, 2, 3], 0),
    (3, [5, 10, 15], 0),
    (3, [1, 1, 2], 1),
    (3, [10, 10, 10], 0),

    (4, [1, 2, 3, 4], 1),
    (4, [1, 1, 1, 1], 1),
    (4, [5, 10, 15, 20], 5),
    (4, [2, 8, 3, 9], 0),
    (4, [10, 1, 1, 1], 6),
    (4, [7, 7, 7, 7], 7),

    (5, [1, 10, 20, 30, 40], 2),
    (5, [5, 5, 5, 5, 5], 0),
    (5, [1, 2, 8, 9, 15], 1),

    (6, [1, 2, 3, 4, 5, 6], 0),
    (6, [10, 20, 30, 40, 50, 60], 0),
    (6, [1, 1, 1, 10, 10, 10], 1),

    (7, [1, 5, 10, 15, 20, 25, 30], 1),
    (8, [2, 4, 6, 8, 10, 12, 14, 16], 0),
    (10, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10], 10),
]

for i, (N, A, expected) in enumerate(tests, 1):
    result = solve(N, A)

    print(f"Test Case {i}: {'PASS' if result == expected else 'FAIL'}")
    print(f"N: {N}")
    print(f"A: {A}")
    print(f"Expected: {expected}")
    print(f"Your Output: {result}")
    print("-" * 40)


