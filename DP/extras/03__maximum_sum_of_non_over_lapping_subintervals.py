
Problem: Maximum Sum of K Non-Overlapping Fixed-Length Subarrays

You are given an array A of N integers, and three integers K, L, and M.

You must select exactly K pairwise non-overlapping contiguous subarrays from A. Each selected subarray must have a length of exactly L.

For each selected subarray, you must evaluate its score using exactly one of the following two methods:

1. Standard Sum: The sum of all elements in the subarray.

2. Alternating Sum: The sum of the elements in the subarray with strictly alternating signs, starting with a positive sign.

For a subarray starting at index i:
A[i] - A[i+1] + A[i+2] - ... + (-1)^(L-1) * A[i+L-1]

You are permitted to use the Alternating Sum method for at most M of your K selected subarrays. The remaining selected subarrays must use the Standard Sum method.

Find the maximum possible total score achievable by optimally selecting the subarrays and their evaluation methods.

Input Format:
The first line contains an integer N, denoting the number of integers in array A.
The second line contains an integer K, denoting the exact number of subarrays to select.
The third line contains an integer L, denoting the exact length of each subarray.
The fourth line contains an integer M, denoting the maximum number of times the alternating sum can be applied.
The fifth line contains N space-separated integers representing array A.

Output:
Print the maximum possible total score.

Sample Input:
8
2
2
1
5 2 7 3 8 4 6 1
7 9 10 11 12 10 7
3 -5 4 -5 4 -2 5

Sample Output:
22

Explanation:

We need to select exactly 2 non-overlapping subarrays, each of length 2.

One optimal selection is:

Subarray 1: [7, 3]
Standard Sum = 7 + 3 = 10

Subarray 2: [8, 4]
Standard Sum = 8 + 4 = 12

Total Score = 10 + 12 = 22

We used 0 alternating sums, which is within the allowed maximum M = 1.

Therefore, the maximum possible score is 22.
# 5 2 7 3 8 4 6 1
# 7 9 10 11 12 10 7
# 3 -5 4 -5 4 -2 5

from functools import lru_cache
def maximumScore(N, K, L, M, A):
    def asum(index):
        ans = A[index]
        sign = -1
        for i in range(index+1,index+L):
            ans = ans + sign*A[i]
            sign *=-1
        return ans
    @lru_cache(None)
    def dfs(ind,k,m):
        if ind >=N-L+1:
            return 0
        if k == 0:
            return 0
        take_sum = sum(A[ind:ind+L])+dfs(ind+L,k-1,m)
        take_asum = float('-inf')
        if m!=0:
            take_asum = asum(ind)+dfs(ind+L,k-1,m-1)
        not_take = dfs(ind+1,k,m)
        return max(take_sum,take_asum,not_take)
    return dfs(0,K,M)


def brute_force(N, K, L, M, A):
    # Reference solution for validating test cases
    windows = []

    for i in range(N - L + 1):
        standard = sum(A[i:i+L])
        alternating = sum(
            A[i+j] * (1 if j % 2 == 0 else -1)
            for j in range(L)
        )
        windows.append((standard, alternating))

    best = float('-inf')

    def dfs(ind, count, alt_count, total):
        nonlocal_best = None

        nonlocal_dummy = 0

        if count == K:
            nonlocal_holder[0] = max(nonlocal_holder[0], total)
            return

        if ind >= len(windows):
            return

        if len(windows) - ind < K - count:
            return

        # Select using standard sum
        dfs(ind + L, count + 1, alt_count,
            total + windows[ind][0])

        # Select using alternating sum
        if alt_count < M:
            dfs(ind + L, count + 1, alt_count + 1,
                total + windows[ind][1])

        # Skip current window
        dfs(ind + 1, count, alt_count, total)

    nonlocal_holder = [float('-inf')]
    dfs(0, 0, 0, 0)

    return nonlocal_holder[0]


test_cases = [
    (8, 2, 2, 1, [5, 2, 7, 3, 8, 4, 6, 1]),
    (4, 1, 2, 1, [10, -10, 1, 1]),
    (6, 2, 2, 0, [1, 2, 3, 4, 5, 6]),
    (6, 2, 2, 1, [-5, -2, -3, -4, -1, -6]),
    (5, 2, 1, 1, [-5, 10, -2, 8, 3]),
    (9, 3, 2, 2, [10, -10, 8, -8, 6, -6, 4, -4, 2]),
    (6, 3, 2, 3, [1, 2, 3, 4, 5, 6]),
    (6, 2, 2, 1, [100, 200, 300, 400, 500, 600]),
    (4, 1, 2, 0, [5, 1, 2, 3]),
    (5, 1, 3, 1, [-2, 5, -1, 4, 3]),
]

print("========== TEST RESULTS ==========")

for i, (N, K, L, M, A) in enumerate(test_cases, 1):
    expected = brute_force(N, K, L, M, A)
    actual = maximumScore(N, K, L, M, A)

    status = "PASS" if actual == expected else "FAIL"

    print(f"\nTest Case {i}: {status}")
    print(f"Input: N={N}, K={K}, L={L}, M={M}, A={A}")
    print(f"Expected: {expected}")
    print(f"Actual:   {actual}")

print("\n========== TESTING COMPLETE ==========")
