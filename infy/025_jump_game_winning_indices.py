# Q25. Jump Game — Sum of Winning Indices
# Problem statement
# You are given an array nums of length N, where nums[i] represents the maximum forward jump length from index i.

# An index i is considered a winning index if you can eventually reach the last index (N - 1) starting from i.

# Find the sum of all winning indices.
# Input format
# - The first line contains an integer N, the number of elements in the array.
# - The second line contains N space-separated integers representing nums[i].
# Constraints
# - \(1 \le N \le 10^4\)
# - \(0 \le nums[i] \le 10^5\)
# Example 1
# Input
# 5
# 2 3 1 1 4


# Explanation

# The last index is 4.
# - Index 0: Can jump to index 1 or 2, and eventually reach index 4. Winning.
# - Index 1: Can jump directly to index 4. Winning.
# - Index 2: Can jump to index 3, then index 4. Winning.
# - Index 3: Can jump directly to index 4. Winning.
# - Index 4: Already at the last index. Winning.
# Winning indices: 0, 1, 2, 3, 4

# Sum = 0 + 1 + 2 + 3 + 4 = 10

# Output
# 10


# Example 2
# Input
# 5
# 3 2 1 0 4


# Explanation

# The last index is 4.
# - Index 0: Can reach indices 1, 2, or 3, but cannot reach index 4.
# - Index 1: Can reach index 3, where the jump length is 0.
# - Index 2: Can reach index 3, where the jump length is 0.
# - Index 3: Cannot move forward.
# - Index 4: Already at the last index. Winning.
# Winning index: 4

# Sum = 4

# Output
# 4


# Example 3
# Input
# 4
# 0 0 0 0


# Explanation

# Only the last index is winning because all earlier indices have a jump length of 0.

# Winning index: 3

# Output
# 3


# Example 4
# Input
# 1
# 0


# Explanation

# The array has only one element. Index 0 is already the last index, so it is winning.

# Sum = 0

# Output
# 0


# Important: Sum the indices of winning positions, not the values in the array. Indices are zero-based.


class Solution:
    def sumWinningIndices(self, nums):
        N = len(nums)
        winning_indicies = [False]*N
        ans = N-1
        def func(ind):
            left = ind
            right = ind
            max_ind = 0
            cor_ind = ind
            path = []
            while left<=right and max_ind<N:
                for i in range(left,right+1):
                    if (i+nums[i])>=max_ind:
                        max_ind = i+nums[i]
                        cor_ind = i
                left = right +1
                right = max_ind
                path.append(cor_ind)
            if max_ind>=N-1:
                for p in path:
                    winning_indicies[p] = True
        for i in range(N-1):
            if winning_indicies[i] == False:
                func(i)
            if winning_indicies[i] == True:
                ans+=i
        
        return ans
                


test_cases = [
    # Example 1: All indices can reach the last index
    {
        "nums": [2, 3, 1, 1, 4],
        "expected": 10
    },

    # Example 2: Only the last index is winning
    {
        "nums": [3, 2, 1, 0, 4],
        "expected": 4
    },

    # Example 3: All jumps are zero
    {
        "nums": [0, 0, 0, 0],
        "expected": 3
    },

    # Example 4: Single-element array
    {
        "nums": [0],
        "expected": 0
    },

    # Example 5: Direct jump to the last index
    {
        "nums": [4, 0, 0, 0, 0],
        "expected": 4
    },

    # Example 6: Only indices 2, 3, 4 can win
    {
        "nums": [0, 0, 2, 1, 0],
        "expected": 9
    },

    # Example 7: Every index can reach the last index
    {
        "nums": [1, 1, 1, 1, 0],
        "expected": 10
    },

    # Example 8: Jump length exceeds array size
    {
        "nums": [100, 0, 0, 0],
        "expected": 3
    },
]


sol = Solution()

for i, test in enumerate(test_cases, 1):
    actual = sol.sumWinningIndices(test["nums"])

    if actual == test["expected"]:
        print(f"Test {i}: PASS")
    else:
        print(
            f"Test {i}: FAIL | "
            f"nums={test['nums']} | "
            f"Expected={test['expected']} | "
            f"Actual={actual}"
        )
