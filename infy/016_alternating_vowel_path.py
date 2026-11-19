# Q16. Alternating Vowel Paths
# You are given an integer n. Count the number of valid strings of length n that consist only of lowercase English vowels ('a', 'e', 'i', 'o', 'u').

# A string is valid if it satisfies both of the following conditions:

# 1. Directed transition rules

# It must follow these directed transition rules from one character to the next:
# - 'a' → 'e' only
# - 'e' → 'a' or 'i' only
# - 'i' → 'a', 'e', 'o', or 'u' only
# - 'o' → 'i' or 'u' only
# - 'u' → 'a' only
# 2. Alternating lexicographical direction

# The transitions must strictly alternate in lexicographical direction.

# If a transition moves to a lexicographically greater vowel (e.g., 'a' to 'e'), the immediately subsequent transition (if one exists) must move to a lexicographically smaller vowel.

def your_function(n):
    d = {"a":["e"],"e":["i","a"],"i":["a","e","u","o"],"o":["i","u"],"u":["a"]}
    def dfs(ind,prev,hl):
        if ind == n:
            return 1
        if ind == 0:
            s = 0
            for key in d:
                s+=dfs(ind+1,key,None)
            return s
        if hl == None:
            s = 0
            for key in d[prev]:
                if ord(prev)>ord(key):
                    s+=dfs(ind+1,key,-1)
                else:
                    s+=dfs(ind+1,key,1)
            return s
        s = 0
        for key in d[prev]:
            if hl == -1 and ord(prev)<ord(key):
                s+=dfs(ind+1,key,1)
            elif hl == 1 and ord(prev)>ord(key):
                s+=dfs(ind+1,key,-1)
        return s
    return dfs(0,None,None)

test_cases = [
    # (n, expected_output)
    (1, 5),
    (2, 10),
    (3, 12),
    (4, 14),
    (5, 16),
    (6, 18),
    (7, 20),
    (8, 22),
    (9, 24),
    (10, 26),
]


def test_your_solution(your_function):
    for n, expected in test_cases:
        actual = your_function(n)

        status = "PASS" if actual == expected else "FAIL"
        print(
            f"n={n}, expected={expected}, "
            f"actual={actual} -> {status}"
        )


# If your function is a standalone function:
test_your_solution(your_function)

# If your function is inside a class:
# sol = Solution()
# test_your_solution(sol.countVowelPaths)
