# Q15. Last Stone Weight II (Resonance Variant)
# Problem Statement
# You are given an integer array stones representing the weights of N stones in a sequence, and an integer R representing a resonance value.

# You must assign each stone to either Set A or Set B.

# The total weight of a set is calculated as:
# 1. The sum of the weights of all stones assigned to that set.
# 2. Plus R for every pair of originally adjacent stones (stones at indices i and i + 1) that are placed in the same set.
# Task: Find the minimum possible absolute difference between the total weight of Set A and Set B.
# Input Format
# - First line: Integer N, number of stones.
# - Second line: Integer R, resonance value.
# - Next N lines: One integer stones[i] per line.

# Example 1
# N = 3R = 2stones = [1, 2, 3]



# One possible assignment:
# - Set A: stones at indices 0 and 1 → [1, 2]
# - Set B: stones at index 2 → [3]
# Set A total:

# 1 + 2 + 2 (resonance) = 5

# Set B total:

# 3

# Difference = |5 - 3| = 2

          
from functools import lru_cache
def solve(N, R, stones):
    # Implement your DP here
    # cur_ind, prev_ind_a
    ans = [float('inf')]
    @lru_cache(None)
    def dfs(ind,prev,dif):
        if ind== 0:
            dfs(ind+1,0,stones[ind])
            dfs(ind+1,-1,-stones[ind])
            return
        if ind == N:
            ans[0] = min(ans[0],abs(dif))
            return
        # take A 
        # check prev
        if prev+1 ==ind:
            dfs(ind+1,ind,stones[ind]+R+dif)
        else:
            dfs(ind+1,ind,stones[ind]+dif)
        # not take A 
        if prev+1 != ind:
            dfs(ind+1,prev,dif - (stones[ind]+R)) 
        else:
            dfs(ind+1,prev,dif -(stones[ind]))
    dfs(0,None,0)
    return ans[0]
        
        
        


test_cases = [
    # (N, R, stones, expected_output)

    # Test 1: Basic example
    (3, 2, [1, 2, 3], 2),

    # Test 2: Three stones with resonance
    (3, 3, [2, 4, 6], 3),

    # Test 3: Alternating assignments
    (4, 1, [1, 2, 3, 4], 1),

    # Test 4: Single stone
    (1, 5, [10], 10),

    # Test 5: Two stones
    (2, 3, [4, 6], 2),

    # Test 6: Equal weights
    (4, 2, [1, 1, 1, 1], 0),

    # Test 7: Larger resonance value
    (4, 5, [2, 3, 4, 5], 2),

    # Test 8: Equal weights
    (4, 2, [5, 5, 5, 5], 0),

    # Test 9: Larger input
    (5, 3, [3, 7, 2, 8, 4], 3),

    # Test 10: Zero resonance
    (4, 0, [1, 2, 7, 8], 0),
]


for i, (N, R, stones, expected) in enumerate(test_cases, 1):
    result = solve(N, R, stones)

    status = "PASS" if result == expected else "FAIL"

    print(
        f"Test {i}: {status} | "
        f"Expected: {expected}, Got: {result}"
    )
