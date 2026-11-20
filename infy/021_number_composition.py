Q21. Number of Compositions of N with Parts in 
You are given two integers N and K.

A valid sequence is an ordered sequence of positive integers satisfying the following conditions:
1. Each element (part) must be between 1 and K, inclusive.
2. The sum of all elements must be exactly N.
The value of a valid sequence is its length (the number of elements in the sequence).

Your task is to calculate the sum of the lengths of all valid sequences.

Since the answer can be large, return it modulo:
\[
10^9 + 7
\]

Input format
- First line: Integer N, the target sum.
- Second line: Integer K, the maximum allowed part.
Output format
Print the sum of the lengths of all valid sequences modulo \(10^9+7\).
Examples
Example 1
Input:
3
2

Output:
7


Explanation:

All valid sequences are:
Sequence	Length
[1, 1, 1]	3
[1, 2]	2
[2, 1]	2

Total = 3 + 2 + 2 = 7.

Example 2
Input:
4
2

Output:
15


Explanation:
Sequence	Length
[1, 1, 1, 1]	4
[1, 1, 2]	3
[1, 2, 1]	3
[2, 1, 1]	3
[2, 2]	2

Total = 4 + 3 + 3 + 3 + 2 = 15.

Example 3
Input:
5
3

Output:
43





def your_function(N,K):
    def dfs(target,count):
        if target>N:
            return 0
        if target == N:
            return count
        s = 0
        for i in range(1,K+1):
            s+= dfs(target+i,count+1)
        return s
    return dfs(0,0)
            

test_cases = [
    # (N, K, expected_output)
    (1, 1, 1),
    (2, 1, 2),
    (3, 2, 7),
    (4, 2, 15),
    (4, 3, 19),
    (5, 2, 30),
    (5, 3, 43),
    (5, 5, 48),
    (6, 2, 58),
    (6, 3, 94),
    (6, 6, 112),
]


def test_your_solution(your_function):
    for n, k, expected in test_cases:
        actual = your_function(n, k)

        status = "PASS" if actual == expected else "FAIL"

        print(
            f"N={n}, K={k}, "
            f"Expected={expected}, Actual={actual} -> {status}"
        )


# Standalone function:
test_your_solution(your_function)

# Class-based solution:
# sol = Solution()
# test_your_solution(sol.countCompositions)
