# Q19. K-Partition Minimising Parity-Imbalance Squared
# You are given an array A consisting of N positive integers.

# You must partition the array into exactly K contiguous, non-empty segments.

# For each segment, calculate its cost using the following formula:
# \[
# \text{Cost} = (\text{EvenCount} - \text{OddCount})^2
# \times \text{MaximumElement}
# \]

# Here:
# - EvenCount is the number of even integers in the segment.
# - OddCount is the number of odd integers in the segment.
# - MaximumElement is the largest integer in the segment.
# Your task is to find the minimum possible sum of costs across all K segments.
# Input format
# - First line: Integer N, the size of the array.
# - Second line: Integer K, the required number of segments.
# - Third line: N space-separated positive integers representing array A.
# Output format
# Print a single integer representing the minimum possible total cost.

# Examples
# Example 1
# Input:
# 3
# 1
# 1 2 3

# Output:
# 3


# Explanation:

# Only one segment is possible: [1, 2, 3].
# - Even count = 1
# - Odd count = 2
# - Maximum = 3
# Cost = (1 - 2)² × 3 = 3.

# Example 2
# Input:
# 4
# 2
# 1 2 3 4

# Output:
# 0


# Explanation:

# Optimal partition:
# [1, 2] | [3, 4]


# First segment: (1 - 1)² × 2 = 0

# Second segment: (1 - 1)² × 4 = 0

# Total = 0.

# Example 3
# Input:
# 5
# 2
# 2 1 4 3 6

# Output:
# 2



def your_function(N,K,arr):
    def dfs(ind,p):
        if ind == N and p>0:
            return float('inf')
        if p<0:
            return 0
        if p==0:
            ne = 0
            no = 0
            max_ = float("-inf")
            min_cost = float("inf")
            for i in range(ind,N-p):
                if arr[i]%2 == 0:
                    ne+=1
                else:
                    no+=1
                max_ = max(arr[i],max_)
            min_cost = min(min_cost,(((ne-no)**2)*max_))
            return min_cost 
        ne = 0
        no = 0
        max_ = float("-inf")
        min_cost = float("inf")
        for i in range(ind,N-p):
            if arr[i]%2 == 0:
                ne+=1
            else:
                no+=1
            max_ = max(arr[i],max_)
            min_cost = min(min_cost,(((ne-no)**2)*max_)+dfs(i+1,p-1))
        return min_cost
    return dfs(0,K-1)   


test_cases = [
    # (N, K, A, expected_output)

    (3, 1, [1, 2, 3], 3),
    (3, 2, [1, 2, 3], 1),
    (4, 2, [1, 2, 3, 4], 0),
    (5, 2, [1, 2, 3, 4, 5], 1),
    (5, 3, [1, 2, 3, 4, 5], 1),

    (4, 1, [2, 4, 6, 8], 128),
    (4, 2, [1, 3, 5, 7], 40),
    (5, 2, [2, 1, 4, 3, 6], 2),

    (6, 3, [1, 2, 3, 4, 5, 6], 0),
    (5, 3, [2, 2, 2, 2, 2], 18),
    (5, 2, [1, 1, 1, 1, 1], 13),
    (3, 3, [7, 2, 9], 18),
]


def test_your_solution(your_function):
    for n, k, arr, expected in test_cases:
        actual = your_function(n, k, arr)

        status = "PASS" if actual == expected else "FAIL"

        print(
            f"N={n}, K={k}, A={arr}, "
            f"Expected={expected}, Actual={actual} -> {status}"
        )


# Test your standalone function:
test_your_solution(your_function)

# If using a class:
# sol = Solution()
# test_your_solution(sol.minimumCost)min
