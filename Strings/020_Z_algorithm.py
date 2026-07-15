# https://www.youtube.com/watch?v=BhxJiqShYcQ
# https://www.naukri.com/code360/problems/z-algorithm_1112619

# Time Complexity: O(n + m)
# Space Complexity: O(n + m)

# For pattern matching using the Z Algorithm, create:
# combined = pattern + "$" + text

# Compute the Z-array on this combined string.
# Whenever:
# Z[i] == len(pattern)
# you found an occurrence of the pattern.

def zAlgorithm(s, p, n, m):
    t = p + '$' + s
    N = len(t)
    z = [0] * N

    l = r = 0
    ans = 0

    for i in range(1, N):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])

        while i + z[i] < N and t[z[i]] == t[i + z[i]]:
            z[i] += 1

        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1

        if z[i] == m:
            ans += 1

    return ans
