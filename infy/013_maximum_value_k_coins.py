# Q13. Maximum Value of K Coins From Piles
# Problem Statement
# You are given P piles of coins. The piles are represented as a 2D grid of size P × M, where M is the maximum number of coins in any single pile.
# - Each row represents a pile from top to bottom.
# - If a pile has fewer than M coins, the remaining spaces in its row are padded with -1.
# - You have a precision extraction tool that allows you to extract exactly one contiguous block (subarray) of valid coins from each pile.
# - You can also skip a pile entirely (extracting a block of length 0).
# - You must extract exactly K valid coins in total across all P piles.
# Return the maximum possible sum of the coins you can extract.
# Input Format
# P
# M
# K


# The remaining P lines describe the coin grid.

# Each row contains the coin values in that pile, with unused positions padded with -1.
# Sample Test Cases
# Test Case 1
# Input:
# 2
# 3
# 3
# 1 2 3
# 4 5 6


# Output:
# 15


# Test Case 2
# Input:
# 3
# 4
# 3
# 1 2 3 4
# 5 6 7 8
# 2 3 -1 -1


# Output:
# 21


# Test Case 3
# Input:
# 2
# 4
# 2
# 10 20 30 40
# 5 15 -1 -1


# Output:
# 55


# Test Case 4
# Input:
# 3
# 3
# 4
# -2 5 8
# 10 -1 -1
# 3 7 9


# Output:
# 29


# Test Case 5
# Input:
# 3
# 5
# 2
# -5 -2 10 20 30
# 4 8 12 -1 -1
# 15 25 35 45 55


# Output:
# 100
def solve(P, M, K, piles):
    best = [[0]*(K+1) for _ in range(P)]
    for p in range(P):
        for k in range(1,K+1):
            max_val = float('-inf')
            cur_sum = 0
            for m in range(M):
                if piles[p][m]==-1:
                    break
                if m<k:
                    cur_sum+=piles[p][m]
                else:
                    max_val = max(cur_sum,max_val)
                    cur_sum+=piles[p][m]
                    cur_sum-=piles[p][m-k]
            max_val = max(cur_sum,max_val)
            best[p][k] = max_val
    def dfs(pile,k_left):
        if pile==P and k_left==0:
            return 0
        if k_left == 0:
            return 0
        if pile == P:
            return float('-inf')
        
        max_val = float('-inf')
        # print("fe")
        for k in range(0,k_left+1):
            # print(k,k_left)
            if k<=k_left:
                x = dfs(pile+1,k_left-k)
                max_val = max(max_val, best[pile][k]+x)
                # print("yes",max_val,x,k,k_left)
        return max_val
    # print(best)
    return dfs(0,K)
    
# Format: (P, M, k, piles, expected_output)
tests = [
    # Test 1: Single pile
    (1, 3, 2,
     [[1, 2, 3]], 5),

    # Test 2: Two piles
    (2, 3, 3,
     [[1, 2, 3],
      [4, 5, 6]], 15),

    # # Test 3: Three piles with padding
    (3, 4, 3,
     [[1, 2, 3, 4],
      [5, 6, 7, 8],
      [2, 3, -1, -1]], 21),

    # Test 4: Large values
    (2, 4, 2,
     [[10, 20, 30, 40],
      [5, 15, -1, -1]], 70),

    # Test 5: Negative values
    (3, 3, 4,
     [[-2, 5, 8],
      [10, -1, -1],
      [3, 7, 9]], 34),

    # Test 6: Mixed positive and negative values
    (3, 5, 2,
     [[-5, -2, 10, 20, 30],
      [4, 8, 12, -1, -1],
      [15, 25, 35, 45, 55]], 100),

    # Test 7: One pile has only one valid coin
    (2, 4, 4,
     [[5, -1, -1, -1],
      [1, 2, 3, 4]], 14),

    # Test 8: Extract zero coins
    (3, 3, 0,
     [[1, 2, 3],
      [4, 5, -1],
      [-2, -1, -1]], 0),

    # Test 9: Extract from multiple piles
    (3, 4, 5,
     [[8, 1, 2, 3],
      [10, 20, -1, -1],
      [4, 5, 6, -1]], 49),
]

for i, (P, M, k, piles, expected) in enumerate(tests, 1):
    result = solve(P, M, k, piles)

    print(f"Test Case {i}: {'PASS' if result == expected else 'FAIL'}")
    print(f"P: {P}, M: {M}, k: {k}")
    print(f"Piles: {piles}")
    print(f"Expected: {expected}")
    print(f"Your Output: {result}")
    print("-" * 50)
