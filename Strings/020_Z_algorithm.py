# https://www.youtube.com/watch?v=BhxJiqShYcQ
# https://www.naukri.com/code360/problems/z-algorithm_1112619


def zAlgorithm(s, p, n, m):
    if n<m:
        return -1
    zstring = p+'$'+s
    z = [0]*(m+n+1)
    # print(z,zstring)
    
    i = 0
    # ans = []
    count = 0
    for i in range(m+1,m+n+1):
        ind = i
        j = 0
        while ind<m+n+1 and j<m and zstring[ind] == zstring[j]:
            j+=1
            ind+=1
        z[i] = ind-i
        if z[i] == m:
            count+=1
            # ans.append(i-m-1)
    # print(z)
    return count


            

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
