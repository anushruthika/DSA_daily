# # Q12. Combination Sum IV (Alternating Parity)

# ## Problem Statement

# You are given an array of distinct integers `nums` and an integer `target`.

# You need to return the number of ordered combinations (sequences) of `nums` that sum to `target` such that no two adjacent elements in the combination have the same parity (i.e., they must strictly alternate between even and odd).

# Different orderings count separately.

# Find the number of valid alternating-parity ordered combinations.

# Since the answer can be very large, return it modulo 10^9 + 7.



from functools import lru_cache

def solve(nums, target):
    N = len(nums)
    @lru_cache(None)
    def rec(cur_sum,prev):
        if cur_sum<0:
            return 0
        if cur_sum == 0:
            return 1
        s = 0
        for i in range(N):
            if prev is None or ((nums[prev]+nums[i])%2 != 0 and cur_sum-nums[i]>= 0):
                s+=rec(cur_sum-nums[i],i)
        return s
    return rec(target,None)

tests = [
    ([1, 2, 3], 4, 1),
    ([1, 2], 3, 2),
    ([2, 4], 6, 0),
    ([1, 2, 3], 5, 3),
    ([1], 3, 0),
    ([1, 2], 4, 1),
    ([1, 2, 3], 6, 4)
]

for nums, target, expected in tests:
    result = solve(nums, target)

    print(f"nums={nums}, target={target}")
    print(f"Expected: {expected}")
    print(f"Your output: {result}")
    print("PASS" if result == expected else "FAIL")
    print("----------------------")
