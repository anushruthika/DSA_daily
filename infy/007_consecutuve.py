
MOD = 10**9 + 7

def solve(N, K):
    if N == 1 or N==k or N<K:
        # because same starting and ending
        return 0
    def dfs(ind,count,first):
        if ind == N-1:
            return dfs(ind-1,count,0)+dfs(ind-1,count-1,1)
        left = dfs(ind-1,K,first)
        right = 0
        if count != 0:
            right = dfs(ind-1,count-1,first)
            
            


# (N, K, expected output)
test_cases = [
    (4, 2, 4),
    (3, 2, 2),
    (2, 2, 2),
    (5, 2, 6),
    (4, 1, 0),
    (1, 2, 0),
    (4, 3, 6),
    (5, 3, 12)
]

for i, (N, K, expected) in enumerate(test_cases, 1):
    actual = solve(N, K)

    status = "PASS" if actual == expected else "FAIL"

    print(f"Test Case {i}: {status}")
    print(f"N = {N}, K = {K}")
    print(f"Expected: {expected}")
    print(f"Actual:   {actual}")
    print("------------------------")
