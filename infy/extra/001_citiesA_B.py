# greedy idea is to initially assign everyone to City A, then move the N employees with the lowest additional cost to City B.
def solve(N, A, B):
    cost = sum(A)
    l = [min(A[i],B[i])+B[i]-A[i] for i in range(2*N)]
    l.sort()
    for i in range(N):
        cost+=l[i]
    return cost


# (N, A, B, expected output)
test_cases = [
    (1, [5, 2], [3, 10], 8),
    (1, [10, 20], [5, 5], 20),
    (2, [1, 100, 50, 50], [10, 1, 20, 20], 93),
    (2, [10, 20, 30, 40], [5, 10, 15, 20], 100),
    (2, [5, 5, 5, 5], [5, 5, 5, 5], 30),
    (3, [10, 20, 30, 40, 50, 60],
        [5, 15, 25, 35, 45, 55], 240),
    (3, [100, 1, 100, 1, 100, 1],
        [1, 100, 1, 100, 1, 100], 9)
]

for i, (N, A, B, expected) in enumerate(test_cases, 1):
    actual = solve(N, A, B)

    status = "PASS" if actual == expected else "FAIL"

    print(f"Test Case {i}: {status}")
    print(f"N = {N}")
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"Expected: {expected}")
    print(f"Actual:   {actual}")
    print("------------------------")
